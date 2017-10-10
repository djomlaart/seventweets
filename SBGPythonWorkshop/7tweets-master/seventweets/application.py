"""
Module contains Flask application and routes 
"""
from flask import Flask, jsonify, request
from storage import Storage

app = Flask(__name__)


@app.route("/tweets", methods=['GET'])
def get_tweets():
    return jsonify(Storage.get_tweets()), 200


@app.route("/tweets/<int:tweet_id>", methods=['GET'])
def get_tweet(tweet_id):
    tweet = Storage.get_tweet(tweet_id)
    return [tweet_id, jsonify(tweet)], 200 if tweet else 404


@app.route("/tweets/", methods=['POST'])
def post_tweet():
    tweet = str(request.data)
    Storage.post_tweet(tweet)
    return jsonify(tweet), 201


@app.route("/tweets/<int:tweet_id>", methods=['DELETE'])
def del_tweet(tweet_id):
    tweet = Storage.del_tweet(tweet_id)
    print(tweet)
    return jsonify(None), 204 if tweet else 404