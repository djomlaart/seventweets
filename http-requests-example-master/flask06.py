from flask import Flask
from blueprints.blueprint import our_bp

app = Flask(__name__)
app.register_blueprint(our_bp)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
