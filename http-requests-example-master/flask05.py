from flask import Flask
app = Flask(__name__)


@app.route("/hello/")
def hello_again():
    return "This page is a lie!", 404

if __name__ == '__main__':
    app.run()
