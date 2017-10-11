"""
Module that contains simple in memory storage implementation
"""


class Storage(object):
    _tweets = [{
                'id': 1,
                'name' : 'mladen',
                'tweet' : 'baba'}
               ]

    @classmethod
    def get_tweets(cls):
        return cls._tweets

    @classmethod
    def get_tweet(cls, tweet_id):
        try:
            return cls._tweets[tweet_id]
        except:
            return None

    @classmethod
    def post_tweet(cls, tweet):
        cls._tweets.append(tweet)

    @classmethod
    def del_tweet(cls, tweet_id):
        try:
            del cls._tweets[tweet_id]
            return 'Deleted'
        except:
            return None

