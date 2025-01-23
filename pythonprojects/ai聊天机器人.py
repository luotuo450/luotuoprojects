import requests
import urllib.parse


def chat_with_bot(message):
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + urllib.parse.quote(
        message
    )
    response = requests.get(url)
    data = response.json()
    if data["result"] == 0:
        return data["content"].replace("{br}", "\n")
    else:
        return "出现错误，无法回复。"


while True:
    user_input = input("你：")
    bot_reply = chat_with_bot(user_input)
    print("机器人：", bot_reply)
