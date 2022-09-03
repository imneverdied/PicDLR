import requests
import os

# 網頁連續編號圖片下載

# 設定[資料夾名稱]/[網址前段]/[總頁數]/[數字補0]/[圖片格式]後即可下載
資料夾名稱 = "設定資料夾名稱"
網址前段 = "圖片網址前段"
總頁數 = 30  # 總頁數
圖片格式 = ".jpg"
數字補0 = 1

# 數字補0參數說明:
# 1:不用補0
# 2:補到2位
# 3:補到3位數
def 下載(資料夾名稱, 網址前段, 總頁數, 圖片格式, 數字補0):
    for i in range(總頁數):  # 第一頁~最後一頁
        input_image = str(i+1).zfill(數字補0)  # 編號補0到 X 位
        if not os.path.exists(資料夾名稱):
            os.mkdir(資料夾名稱)  # 建立資料夾
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                'refer': 'https://www.manhuagui.com/'}
            img = requests.get(
                f"{網址前段}{input_image}{圖片格式}", headers=headers)  # 下載圖片
        except Exception as e:
            print(repr(e))
        # 開啟資料夾及命名圖片檔
        try:
            with open(資料夾名稱+"\\" + str(input_image) + 圖片格式, "wb") as file:
                print("已下載", 資料夾名稱 + str(input_image) + 圖片格式)
                file.write(img.content)  # 寫入圖片的二進位碼
        except:
            print(print("沒有", 資料夾名稱 + str(input_image) + 圖片格式))

    print("下載完畢")


下載("xxx單行本 第1卷", "網址", 200, ".jpg", 3)
