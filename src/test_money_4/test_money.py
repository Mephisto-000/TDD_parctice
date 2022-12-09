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
        portfolio = Portfolio()  # 宣告一個空的 Portfolio 物件
        portfolio.add(fiveDollars, tenDollars)  # 向此 Portfolio 物件添加多個具有相同貨幣的 Money 物件
        self.assertEqual(fifthDollars, portfolio.evaluate("USD"))  # 以相同貨幣來評估 Portfolio 並將結果與期望的 Money 物件進行比較


if __name__ == "__main__":
    unittest.main()
