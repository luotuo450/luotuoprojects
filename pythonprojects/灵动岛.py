import tkinter as tk  # 导入 tkinter 库，用于创建图形用户界面
import time  # 导入 time 库，用于处理时间相关的操作
import psutil  # 导入 psutil 库，用于获取系统信息，如电池状态

ChargingStatus = []  # 创建一个空列表，用于存储充电状态

while True:  # 无限循环，用于持续监测电池状态
    battery = psutil.sensors_battery()  # 获取电池信息
    plugged = battery.power_plugged  # 检查是否连接了外部电源
    percent = battery.percent  # 获取电池剩余电量百分比

    if plugged:  # 如果连接了外部电源，将 plugged 设置为 1
        plugged = 1

    if plugged == False:  # 如果未连接外部电源，将 plugged 设置为 0
        plugged = 0

    ChargingStatus.append(plugged)  # 将当前的充电状态添加到 ChargingStatus 列表中

    if len(ChargingStatus) > 3:  # 如果 ChargingStatus 列表中的元素数量超过 3
        if (
            ChargingStatus[-1] == 1 and ChargingStatus[-2] == 0
        ):  # 如果当前状态为充电，且前一个状态为未充电
            print("开始充电")  # 打印开始充电的消息
            root = tk.Tk()  # 创建一个新的 tkinter 窗口
            root.title("灵动岛")  # 设置窗口标题为“灵动岛”
            root.geometry("183x20+680+0")  # 设置窗口大小和位置
            root.overrideredirect(True)  # 隐藏窗口边框
            label = tk.Label(
                root,
                text="开始充电...当前电量" + str(percent) + "%",
                font=("HarmonyOS Sans SC", 12),
            )  # 创建一个标签，显示开始充电的消息和当前电量百分比
            label.pack()  # 将标签添加到窗口中
            root.after(2000, lambda: root.destroy())  # 等待 3 秒后销毁窗口
            root.mainloop()  # 进入 tkinter 主事件循环

        elif (
            ChargingStatus[-1] == 0 and ChargingStatus[-2] == 1
        ):  # 如果当前状态为未充电，且前一个状态为充电
            print("停止充电")  # 打印停止充电的消息
            root = tk.Tk()  # 创建一个新的 tkinter 窗口
            root.title("灵动岛")  # 设置窗口标题为“灵动岛”
            root.geometry("183x20+680+0")  # 设置窗口大小和位置
            root.overrideredirect(True)  # 隐藏窗口边框
            label = tk.Label(
                root,
                text="停止充电...当前电量" + str(percent) + "%",
                font=("HarmonyOS Sans SC", 12),
            )  # 创建一个标签，显示停止充电的消息和当前电量百分比
            label.pack()  # 将标签添加到窗口中
            root.after(2000, lambda: root.destroy())  # 等待 3 秒后销毁窗口
            root.mainloop()  # 进入 tkinter 主事件循环
    time.sleep(0.1)  # 暂停 0.1 秒，避免过于频繁地检查电池状态
