#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py

import tweepy
import logging
from config import create_api
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            # This tweet is a reply or written by me, so ignore it
            return
        # if not tweet.favorited:
        # Mark it as Liked
        # try:
        # tweet.favorite()
        # except Exception as e:
        # logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted and tweet.user.verified:
            # Retweet if from verified account and not banned anywhere
            try:
                print(tweet.text, tweet.user.name, tweet.user.screen_name)
                tweet.retweet()
                exit() # interim solution to kill the bot
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    main(
        [
            "Insomnia",
            "Insomniac",
            "Sleep Coach",
            "sleep is very important",
            "SAD lamp",
            "SADlamp",
            "Sleep deprivation",
            "Sleep hygiene",
            "importance of sleep",
            "how many hours of sleep",
            "sleep is important",
            "the affect of sleep",
        ]
    )
