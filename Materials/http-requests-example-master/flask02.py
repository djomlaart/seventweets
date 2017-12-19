from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "Yes, this is index page."


@app.route("/hello/", methods=['GET'])
def hello():
    return "Hello!"


if __name__ == "__main__":
    app.run()
