import pyperclip as pc
import pyautogui as pg
import keyboard as kb
import time

user_input = input("请输入你想要疯狂发消息的文本: ")
pc.copy(user_input)
print("文本已复制到剪贴板，按下ctrl键开始")
kb.wait("ctrl")
while True:
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    time.sleep(0.01)
