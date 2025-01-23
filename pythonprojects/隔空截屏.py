import cv2
import mediapipe as mp
import pyautogui
import time
import os
import numpy as np  # 添加这一行

acb = 0
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


def is_fist(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    if (
        index_tip.y > landmarks[6].y
        and middle_tip.y > landmarks[10].y
        and ring_tip.y > landmarks[14].y
        and pinky_tip.y > landmarks[18].y
    ):
        return True
    else:
        return False


prev_landmarks = None
swipe_count = 0
swipe_direction = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_fist(hand_landmarks.landmark):
                screenshot_path = "D:\\下载\\screenshot" + str(acb) + ".png"
                while os.path.exists(screenshot_path):
                    acb += 1
                    screenshot_path = "D:\\下载\\screenshot" + str(acb) + ".png"
                pyautogui.screenshot(screenshot_path)
                print("截屏")

                # 显示纯白图像
                white_image = np.ones((1200, 1920, 3), dtype=np.uint8) * 255
                cv2.imshow("White Screen", white_image)
                cv2.moveWindow("White Screen", 0, 0)
                cv2.waitKey(100)  # 显示 0.1 秒
                cv2.destroyWindow("White Screen")  # 关闭白色图像窗口

                acb += 1
                time.sleep(1)  # 防止连续截屏

            else:
                swipe_count = 0
                swipe_direction = None

            prev_landmarks = hand_landmarks.landmark

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
