# 导入库
import pyperclip as pc
import pyautogui as pg
import keyboard as kb
import time

message = input("请输入你想要疯狂发送的信息：")
pc.copy(message)
kb.wait("ctrl")
while True:
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    time.sleep(0.1)
