import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)  # 打开摄像头
while True:
    ret, frame = cap.read()  # 读取视频帧
    if not ret:
        break
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 转换颜色空间
    results = hands.process(image)  # 手势识别
    # 处理识别结果
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )  # 用于指定地标如何在图中连接。
            for point in hand_landmarks.landmark:
                x = int(point.x * frame.shape[1])
                y = int(point.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)  # 画出关键点
    cv2.imshow("Gesture Recognition", frame)  # 显示结果
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
