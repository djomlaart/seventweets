from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/hello/")
def hello_again():
    return " ".join([
        "You have gone to:",
        request.url,
        "Your request headers were:",
        str(request.headers)
    ])

if __name__ == '__main__':
    app.run()