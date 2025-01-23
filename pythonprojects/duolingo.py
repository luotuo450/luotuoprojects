import pyautogui as pg
import time as t

t.sleep(3)
for i in range(100):
    pg.click(x=830, y=363)
    t.sleep(3)
    for a in range(15):
        pg.press("1")
        pg.press("enter")
        t.sleep(0.1)
        pg.press("enter")
        t.sleep(0.1)
    for b in range(1, 5):
        for c in range(5, 9):
            pg.press(str(b))
            t.sleep(0.1)
            pg.press(str(c))
    t.sleep(0.05)
    pg.press("enter")
    t.sleep(0.1)
    for a in range(14):
        pg.press("2")
        pg.press("enter")
        t.sleep(0.1)
        pg.press("enter")
        t.sleep(0.1)
    t.sleep(10)
    pg.press("enter")
    for _count in range(20):
        pg.press("up")
    t.sleep(0.1)
