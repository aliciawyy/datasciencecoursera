import os
import pprint
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
from rx import Observable

TWITTER_CREDENTIAL_FILE = os.path.expanduser("~/.config/twitter/credentials")
"""
twitter credential file example

consumer_key:xxx
consumer_secret:xxx
access_token:xxx
access_token_secret:xxx
"""


def get_twitter_credentials():
    credentials = {}
    with open(TWITTER_CREDENTIAL_FILE) as f:
        for x in f.readlines():
            k, v = x.strip().split(':')
            credentials[k] = v
    return credentials


def tweets_for(topics):

    def observe_tweets(observer):
        class TweetListener(StreamListener):
            def on_data(self, raw_data):
                observer.on_next(raw_data)
                return True

            def on_error(self, status_code):
                observer.on_error(status_code)

        l = TweetListener()
        keys = get_twitter_credentials()
        auth = OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
        auth.set_access_token(keys["access_token"],
                              keys["access_token_secret"])
        stream = Stream(auth, l)
        stream.filter(track=topics)

    return Observable.create(observe_tweets).share()

topics = ["SP500", "Trump"]

disposable = tweets_for(topics).map(lambda d: json.loads(d)) \
    .filter(lambda m: "text" in m) \
    .map(lambda m: m["text"].strip()) \
    .subscribe(pprint.pprint)

time.sleep(5)
disposable.dispose()
