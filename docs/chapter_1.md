# Chapter 1 ： TDD 與問題說明



## 1-1. 測試驅動（TDD）三階段開發過程

1. 紅（red）。 編寫失敗的測試。
2. 綠 （green）。 編寫必要且足以通過測試的程式碼。
3. 重構 （refactor）。 對程式碼內部結構進行變動，目的是在不改變它可見行為這個前提下，提高它可理解性，並降低修改它的成本。



## 1-2. 問題是？

假設我們必須建立一個電子試算表來管理具有一種以上貨幣的資金，例如說是為了管理股票投資組合 ： 

| 股票    | 股票交易所 | 股數 | 每股價格   | 總金額        |
| :------ | ---------- | ---- | ---------- | ------------- |
| IBM     | NASDAQ     | 100  | 124 美元   | 12400 美元    |
| BMW     | DAX        | 400  | 75 歐元    | 30000 歐元    |
| Samsung | KSE        | 300  | 68000 韓元 | 20400000 韓元 |

需要的功能 ： 

1. 簡單的算術運算 :
   - 5 美元 * 2 = 10 美元
   - 10 歐元 * 2 = 20 歐元
   - 4002 韓元 / 4 = 1000.5 韓元
2. 貨幣之間進行轉換 : 
   - 5 美元 + 10 歐元 = 17 美元
   - 1 美元 + 1100 韓元 = 2200 韓元



### 5 美元 * 2 = 10 美元 : 

```python
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
```



