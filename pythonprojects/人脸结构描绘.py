import cv2
import dlib

# 初始化dlib的人脸检测器和特征提取器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    r"D:\luotuo projects\python projects\shape_predictor_68_face_landmarks.dat"
)

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break
    # 把图像转为8bit
    frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    # 将帧转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    faces = detector(gray)

    # 遍历检测到的人脸
    for face in faces:
        # 获取人脸的边界框
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # 绘制人脸边界框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 获取人脸特征点
        shape = predictor(gray, face)
        for i in range(0, 68):
            x = shape.part(i).x
            y = shape.part(i).y
            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

    # 显示结果
    cv2.imshow("Face Detection", frame)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
