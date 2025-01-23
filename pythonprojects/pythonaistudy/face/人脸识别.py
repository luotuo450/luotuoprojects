import cv2
import os
import sys
from PIL import Image
import numpy as np

img_path_num = 1
face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")


def save_image():
    global img_path_num
    global face_cascade
    global cap
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame1 = cap.read()
        # 增加 scaleFactor 以减少检测到的人脸数量
        faces = face_cascade.detectMultiScale(frame1, scaleFactor=1.15, minNeighbors=6)
        for x, y, w, h in faces:
            frame2 = cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)
            frame = frame1[y : y + h, x : x + w]
        cv2.imshow("frame", frame1)
        while True:
            save_img_path = os.path.join("./train/{}.jpg".format(img_path_num))
            if not os.path.exists(save_img_path):
                break
            img_path_num += 1
        if cv2.waitKey(1) & 0xFF == ord("s"):
            cv2.imwrite(save_img_path, frame)
            img_path_num += 1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


def getImagesAndLabels(path):
    # 创建空的列表
    faceSamples = []
    # 创建空的id标签列表
    ids = []
    # 获取图片具体路径
    img_paths = [os.path.join(path, f) for f in os.listdir(path)]
    # 加载人脸分类器
    face_cascade = cv2.CascadeClassifier(
        "haarcascade/haarcascade_frontalface_default.xml"
    )
    # 遍历图片路径列表
    for img_path in img_paths:
        # 打开图片
        PIL_img = Image.open(img_path).convert("L")
        # 将图片转换为numpy数组
        img_numpy = np.array(PIL_img, "uint8")
        # 识别图片中的人脸
        faces = face_cascade.detectMultiScale(
            img_numpy, scaleFactor=1.1, minNeighbors=5
        )
        # 获取每张图片的id标签
        id = int(os.path.split(img_path)[-1].split(".")[0])
        for x, y, w, h in faces:
            # 将人脸截取并保存
            face_img = img_numpy[y : y + h, x : x + w]
            # 将截取的图片添加到列表中
            faceSamples.append(face_img)
            # 将id标签添加到列表中
            ids.append(id)
    return faceSamples, ids


path = r"./train"
# 获取图像数组和id标签数组
save_image()
faces, ids = getImagesAndLabels(path)
# 创建训练器
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 训练模型
recognizer.train(faces, np.array(ids))
# 保存模型
recognizer.save("trainner.yml")
cap.release()

# 人脸识别
import cv2
import numpy as np
import os
import ctypes
import time
import pyautogui as pg

pg.FAILSAFE = False
user32 = ctypes.windll.user32
luojiaqi = []
# 创建训练器
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 加载训练集
recognizer.read("trainner.yml")
# 调用摄像头
cap = cv2.VideoCapture(0)

while True:
    # 获取人脸图像
    flag, img = cap.read()
    # 调整图像大小
    img = cv2.resize(img, (1280, 960))
    # 如果没有图像，退出循环
    if not flag:
        print("无法获取图像")
        break
    # 灰度化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 初始化分类器
    face_detector = cv2.CascadeClassifier(
        "haarcascade/haarcascade_frontalface_default.xml"
    )
    # 检测人脸
    faces = face_detector.detectMultiScale(gray, 1.1, 10)
    for x, y, w, h in faces:
        # 画出矩形框
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # 把检测到人脸的区域截取出来，送入分类器进行识别的对应id,conf(置信度,越低越好)
        id, conf = recognizer.predict(gray[y : y + h, x : x + w])
        # 判断对应的id代表着什么人
        if type(id) == int and id >= 1 and id <= img_path_num - 1:
            # 如果置信度小于65，则判断是骆家祺
            if conf < 65:
                # 在矩形框的左上角显示“骆家祺”
                cv2.putText(
                    img,
                    "骆家祺",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    1,
                )
            # 如果置信度大于或等于65
            else:
                # 在矩形框的左上角显示“不是骆家祺”
                cv2.putText(
                    img,
                    "不是骆家祺",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    1,
                )
            # 在矩形框的左下角显示置信度
            cv2.putText(
                img,
                "conf:" + str(conf)[:4],
                (x, y + h + 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                1,
            )
    # 显示图像
    cv2.imshow("windows", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
print(img_path_num)
# 释放资源
cap.release()
cv2.destroyAllWindows()
