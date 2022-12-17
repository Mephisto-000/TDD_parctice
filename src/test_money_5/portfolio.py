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
