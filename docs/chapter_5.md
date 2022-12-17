# Chapter 5：功能和重新設計

## 5-1. 混合貨幣

問題：貨幣的異質性組合要求我們在程式碼中建立一個新的抽象化：將金錢從一種貨幣轉換成另一種貨幣。

這邊我們建立一些關於貨幣轉換的基本規則，首先考慮幾件事：

1. 轉換總是與一對貨幣相關。
   - 我們希望所有轉換都是獨立。
2. 轉換是利用明確的匯率從一種貨幣換抱另一種貨幣。
   - 匯率：每單位的「來源」貨幣所獲得的「目的」貨幣的單位數量。
3. 一對貨幣之間的兩種匯率可能是也可能不是彼此的算術倒數。
4. 一種貨幣可能對另一種貨幣沒有明確的匯率。
   - 貨幣不可轉換的原因很多：經濟、政治或軍事。



實做方法 ： **一次針對一個測試驅動場景！**

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
        self._eur_to_usd = 1.2  # 匯率被定義成一個適當命名的變數

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def __convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            return aMoney.amount * self._eur_to_usd  # 匯率變數用於轉換貨幣

    def evaluate(self, currency):
        total = functools.reduce(operator.add,
                                 map(lambda m: self.__convert(m, currency), self.moneys), 0)
        return Money(total, currency)
```



