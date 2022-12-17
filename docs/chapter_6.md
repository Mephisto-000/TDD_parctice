# Chapter 6：製作事物的雜湊（圖）

我們需要的是一個雜湊圖（hashmap），它允許我們在給定「來源」貨幣和「目的」貨幣的情況下查找匯率。

匯率表：

| 來源 | 目的 | 匯率    |
| :--- | ---- | ------- |
| 歐元 | 美元 | 1.2     |
| 美元 | 歐元 | 0.82    |
| 美元 | 韓元 | 1100    |
| 韓元 | 美元 | 0.00090 |
| 歐元 | 韓元 | 1344    |
| 韓元 | 歐元 | 0.00073 |

$\star$ 當我們引入額外的貨幣時，我們將看到**轉換優先前提（transformation priority premise, TPP）**的作用。

## 程式碼

### test_money.py

```python
import unittest
from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision,
                         originalMoney.divide(4))

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifthDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifthDollars, portfolio.evaluate("USD"))

    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portfolio.evaluate("USD")
        self.assertEqual(expectedValue, actualValue,
                         "%s != %s" % (expectedValue, actualValue))

    def testAdditionOfDollarsAndWons(self):
        oneDollar = Money(1, "USD")
        elevenHundredWon = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, "KRW")
        actualValue = portfolio.evaluate("KRW")
        self.assertEqual(expectedValue, actualValue,
                         "%s != %s" % (expectedValue, actualValue))


if __name__ == "__main__":
    unittest.main()
```

### money.py

```python
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self):
        return f"{self.currency} {self.amount:0.2f}"

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)
```

### portfolio.py

```python
import functools
import operator
from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def __convert(self, aMoney, aCurrency):
        exchangeRates = {'EUR->USD': 1.2,
                         'USD->KRW': 1100}
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = aMoney.currency + '->' + aCurrency
            return aMoney.amount * exchangeRates[key]

    def evaluate(self, currency):
        total = functools.reduce(operator.add,
                                 map(lambda m: self.__convert(m, currency), self.moneys), 0)
        return Money(total, currency)
```

