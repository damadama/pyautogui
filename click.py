import pyautogui    

# 参考リンク先
# https://qiita.com/konitech913/items/301bb63c8a69c3fcb1bd

# クリックしたい位置の座標を確認
print(pyautogui.position())

# positionで分かった座標を入力
# pyautogui.click(723,31)

#画像も指定できる 
pyautogui.click("hyouji.png")


