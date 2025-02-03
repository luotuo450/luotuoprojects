import requests
import os

print("您的模型有：")
os.system("ollama list")
model = input("请选择模型：")
host = "xxx"
port = "xxx"
url = f"http://127.0.0.1:11434/api/chat"  # 更改成你的接口地址
headers = {"Content-Type": "application/json"}
user = 0
while user != "exit":
    user = input("请输入对话内容：")
    if user == "exit":
        break
    data = {
        "model": model,  # 模型选择
        "options": {
            "temperature": 0  # 为0表示不让模型自由发挥，输出结果相对较固定，>0的话，输出的结果会比较放飞自我
        },
        "stream": False,  # 流式输出
        "messages": [{"role": "system", "content": user}],  # 对话列表
    }
    response = requests.post(url, json=data, headers=headers, timeout=60)
    res = response.json()
    a = res["message"]
    print(a["content"])
