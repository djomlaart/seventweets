"""
Module that contains simple in memory storage implementation
"""


class Storage(object):
    _tweets = {1: 'baba'}
    _counter = 1

    @classmethod
    def get_tweets(cls):
        return cls._tweets

    @classmethod
    def get_tweet(cls, tweet_id):
        return cls._tweets.get(tweet_id, None)

    @classmethod
    def post_tweet(cls, tweet):
        cls._counter += 1
        cls._tweets[cls._counter] = tweet

    @classmethod
    def del_tweet(cls, tweet_id):
        return cls._tweets.pop(tweet_id, None)
