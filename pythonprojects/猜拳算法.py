import cv2
import mediapipe as mp
import random

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
position = []
# coding:utf-8
cap = cv2.VideoCapture(0)  # 打开摄像头

# 初始化计数器
total_rounds = 10
round_count = 0
win_count = 0
lose_count = 0
draw_count = 0
last_valid_gesture = None  # 记录上一次的有效手势
waiting_for_valid = True  # 是否在等待有效手势

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
                position.append([x, y])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)  # 画出关键点
    if len(position) % 21 == 0 and len(position) > 0:
        shouwan = position[-21]
        muzhi = position[-17]
        shizhi = position[-13]
        zhongzhi = position[-9]
        sizhi = position[-5]
        xiaozhi = position[-1]
        youxiao = 0
        user_gesture = None
        if (
            results.multi_hand_landmarks
            and ((shouwan[1] - muzhi[1]) + (muzhi[0] - shouwan[0])) / 2 > 100
            and (shouwan[1] - shizhi[1]) > 120
            and (shouwan[1] - zhongzhi[1]) > 120
            and (shouwan[1] - sizhi[1]) > 120
            and (shouwan[1] - xiaozhi[1]) > 100
        ):
            user_gesture = "布"
            youxiao = 1
        if (
            (shouwan[1] - shizhi[1]) < 110
            and (shouwan[1] - zhongzhi[1]) < 110
            and (shouwan[1] - sizhi[1]) < 110
            and (shouwan[1] - xiaozhi[1]) < 110
        ):
            user_gesture = "石头"
            youxiao = 1
        if (
            ((shouwan[1] - muzhi[1]) + (muzhi[0] - shouwan[0])) / 2 < 115
            and (shouwan[1] - shizhi[1]) > 120
            and (shouwan[1] - zhongzhi[1]) > 120
            and (shouwan[1] - sizhi[1]) < 110
            and (shouwan[1] - xiaozhi[1]) < 110
        ):
            user_gesture = "剪刀"
            youxiao = 1
        if youxiao == 0:
            waiting_for_valid = True  # 识别到无效手势，设置等待有效手势标志

        if user_gesture and waiting_for_valid:
            print(f"你出了{user_gesture}")  # 只打印识别到无效手势之后立刻出的那个手势
            ai_gesture = random.choice(["石头", "剪刀", "布"])
            print(f"AI出了{ai_gesture}")
            if user_gesture == ai_gesture:
                print("平局")
                draw_count += 1
            elif (
                (user_gesture == "石头" and ai_gesture == "剪刀")
                or (user_gesture == "剪刀" and ai_gesture == "布")
                or (user_gesture == "布" and ai_gesture == "石头")
            ):
                print("你赢了")
                win_count += 1
            else:
                print("你输了")
                lose_count += 1
            round_count += 1
            if round_count >= total_rounds:
                print(
                    f"总共{total_rounds}局，平局{draw_count}次，赢{win_count}次，输{lose_count}次"
                )
                print(f"平局百分比: {draw_count/total_rounds*100:.2f}%")
                print(f"赢的百分比: {win_count/total_rounds*100:.2f}%")
                print(f"输的百分比: {lose_count/total_rounds*100:.2f}%")
                break
            waiting_for_valid = False  # 进行一局后，取消等待有效手势标志

    cv2.imshow("Gesture Recognition", frame)  # 显示结果
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
