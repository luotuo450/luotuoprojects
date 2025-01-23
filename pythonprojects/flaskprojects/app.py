from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():

    return "随便写一点吧"


if __name__ == "__main__":

    app.run()
