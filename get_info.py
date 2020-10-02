# -*- coding: utf-8 -*-
import tweepy
import emoji
import os, config
import json
import argparse, re

import numpy as np
import pandas as pd

def emoji_remove(stc_str):
     return ''.join(c for c in stc_str if c not in emoji.UNICODE_EMOJI)


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth, wait_on_rate_limit=True)

#DataFrame
tweet_df = pd.DataFrame(columns=['search_word', 'created_at', 'user_id', 'tweet_id', 'like', 'retweet', 'tweet'])

search_word = '東京理科 -filter:retweets -filter:replies'

for i in range(1, 50):

    if i == 1:
        tweets = api.search(q=search_word, count=10, lang='ja', tweet_mode='extended') #文字数が多いツイートを省略しないようにする.
    else:
        tweets = api.search(q=search_word, count=10, lang='ja', tweet_mode='extended', max_id = next_max_id - 1)

    #tweets = api.search(q=search_word, lang='ja', tweet_method='extended')
    for tweet in tweets:
        search_word = search_word
        created_at = tweet.created_at
        user_id = tweet.user.id_str
        tweet_id = tweet.id_str
        like = tweet.favorite_count
        retweet = tweet.retweet_count
        tweet = emoji_remove(tweet.full_text)

        result_info = pd.Series([search_word, created_at, user_id, tweet_id, like, retweet, tweet], index=tweet_df.columns)
        next_max_id = tweets[-1].id

        if re.search('東京理科', tweet) == None:
            pass
        else:
            tweet_df =  tweet_df.append(result_info, ignore_index=True)


tweet_df