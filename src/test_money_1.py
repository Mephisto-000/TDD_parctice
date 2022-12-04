import unittest  # 匯入 TestCase 超類別(superclass)所需的 unittest 套件


class Dollar:
    def __init__(self, amount):  # 每當建立 Dollar 物件時，都會呼叫 __init__ 函數
        self.amount = amount  # 將 self.amount 變數初始化為給定的參數

    def times(self, multiplier):  # times 方法會接受一個參數
        return Dollar(self.amount * multiplier)  # 簡單的實作中，限定總是傳回 10 美元


class TestMoney(unittest.TestCase):  # 我們所要測試的類別，他必須是 unittest.TestCase 類別的子類別(subclass)
    def testMultiplication(self):  # 方法的名稱必須以 test 開頭，才能作為測試的方法
        fiver = Dollar(5)  # 代表 "5美元" 的物件
        tenner = fiver.times(2)  # 被測的方法 : times
        self.assertEqual(10, tenner.amount)  # 在 assertEqual 敘述中將實際值與期望值進行比較


if __name__ == "__main__":
    unittest.main()
