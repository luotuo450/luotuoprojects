# https://oral-calculation.netlify.app/#/welcome
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
from pynput.keyboard import Controller, Key, Listener
import pyautogui as pg
import time
import pyperclip as pc

# 配置 Tesseract 路径
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # 根据实际情况修改路径
)


def capture_screen(bbox=(862, 420, 992, 459)):
    """捕获屏幕的指定区域"""
    img = ImageGrab.grab(bbox=bbox)
    return img


def preprocess_image(img):
    """预处理图像以提高 OCR 准确率"""
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh


def ocr_image(img):
    """使用 OCR 识别图像中的文本"""
    text = pytesseract.image_to_string(img, lang="eng")
    return text.strip()


def parse_expression(text):
    """解析 OCR 识别的文本为算式，并将 s 或 S 替换成 5"""
    # 替换 s 或 S 为 5
    text = text.replace("s", "5").replace("S", "5")
    # 假设文本是简单的算式，如 "1 + 2"
    return text


def calculate_expression(expression):
    """计算算式的值"""
    try:
        result = eval(expression)
    except Exception as e:
        print(f"计算错误: {e}")
        result = None
    return result


def type_result(result):
    """模拟键盘输入结果"""
    keyboard = Controller()
    # 等待一秒确保焦点正确
    keyboard.type(str(int(result)))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print("输入完成")


def main():
    # 捕获屏幕
    img = capture_screen()
    # 预处理图像
    processed_img = preprocess_image(img)
    # OCR 识别
    text = ocr_image(processed_img)
    print(f"识别到的文本: {text}")
    # 解析算式
    expression = parse_expression(text)
    print(f"解析后的算式: {expression}")
    # 计算结果
    result = calculate_expression(expression)
    if result is not None:
        print(f"计算结果: {result}")
        # 输入结果
        type_result(result)
        print(type(result))
        # 复制结果到剪贴板
        pc.copy(str(result))
    else:
        print("无法计算结果")


def on_press(key):
    """监听键盘事件，按下 Alt 键时停止程序"""
    if key == Key.alt:
        print("Alt 键被按下，程序停止")
        return False  # 停止监听


if __name__ == "__main__":
    with Listener(on_press=on_press) as listener:
        while True:
            time.sleep(0.1)
            main()
            if not listener.running:
                break
