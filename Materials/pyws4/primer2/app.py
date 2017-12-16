import pg8000
from flask import Flask, Response

app = Flask(__name__)
conn = pg8000.connect(user="radionica", password="P4ss", host="radionica-postgres")
cursor = conn.cursor()
cursor.execute("CREATE TEMPORARY TABLE tweets (id SERIAL, message TEXT)")
cursor.execute("INSERT INTO tweets (message) VALUES (%s), (%s), (%s)", (
    "Don’t Panic.",
    "It is a mistake to think you can solve any major problems just with potatoes!",
    "It is an important and popular fact that things are not always what they seem."
))
conn.commit()

@app.route('/')
def random_tweet():
    cursor.execute("SELECT * FROM tweets ORDER BY RANDOM() LIMIT 1")
    return Response(cursor.fetchall()[0][1], mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
