import requests
import os

# 網頁連續編號圖片下載

# 須設定[資料夾名稱]/[網址前段]/[總頁數]/[數字補0]即可下載
資料夾名稱 = "設定資料夾名稱"
網址前段 = "圖片網址前段"
總頁數 = 30  # 總頁數
數字補0 = 1
# 數字補0參數說明:
# 1:不用補0
# 2:補到2位
# 3:補到3位數

for i in range(總頁數):  # 第一頁~最後一頁
    input_image = str(i+1).zfill(數字補0)  # 編號補0到 X 位
    if not os.path.exists(資料夾名稱):
        os.mkdir(資料夾名稱)  # 建立資料夾
    img = requests.get(
        f"{網址前段}{input_image}.jpg")  # 下載圖片

    with open(資料夾名稱+"\\" + str(input_image) + ".png", "wb") as file:  # 開啟資料夾及命名圖片檔
        print("已下載", 資料夾名稱 + str(input_image) + ".png")
        file.write(img.content)  # 寫入圖片的二進位碼

print("下載完畢")
