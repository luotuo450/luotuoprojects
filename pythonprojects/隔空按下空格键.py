import cv2
import mediapipe as mp
import pyautogui
import time
import warnings

warnings.filterwarnings("ignore")
pyautogui.FAILSAFE = False

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6)  # 调整为0.8或更高
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


def is_fist(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    if (
        index_tip.y > landmarks[6].y + 0.01  # 增加一个小的偏移量
        and middle_tip.y > landmarks[10].y + 0.01
        and ring_tip.y > landmarks[14].y + 0.01
        and pinky_tip.y > landmarks[18].y + 0.01
    ):
        return True
    else:
        return False


consecutive_frames = 2  # 连续帧数阈值
fist_count = 0  # 记录连续检测到拳头的帧数

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
                fist_count += 1
                if fist_count >= consecutive_frames:
                    pyautogui.press("space")
                    fist_count = 0  # 重置计数器
                    time.sleep(0.01)
            else:
                fist_count = 0  # 重置计数器

            prev_landmarks = hand_landmarks.landmark
    time.sleep(0.01)

    # 显示窗口

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
