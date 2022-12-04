import unittest
import functools  # 提供 reduce 函數
import operator  # 提供 add 函數


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(operator.add,
                                 map(lambda m: m.amount, self.moneys), 0)  # reduce 最後一個參數是累加結果的初始值
        return Money(total, currency)


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuros(self):
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
        portfolio = Portfolio()  # 宣告一個空的 Portfolio 物件
        portfolio.add(fiveDollars, tenDollars)  # 向此 Portfolio 物件添加多個具有相同貨幣的 Money 物件
        self.assertEqual(fifthDollars, portfolio.evaluate("USD"))  # 以相同貨幣來評估 Portfolio 並將結果與期望的 Money 物件進行比較


if __name__ == "__main__":
    unittest.main()
