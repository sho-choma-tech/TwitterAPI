# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np 

import tweepy
import emoji
import json, re, os, datetime

import config
from requests_oauthlib import OAuth1Session

#絵文字の削除
def remove_emoji(stc_str):
    return ''.join(c for c in stc_str if c not in emoji.UNICODE_EMOJI)

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth, wait_on_rate_limit=True)

"""
search_word = 'sample -filter:retweets - filter:replies'
for i in range(1, 50):
    if i == 1:
        tweets = api.search(q=search_word, count=100, lang='ja', tweet_mode='extended')
    else:
        tweets = api.search(q=search_word, count=100, lang='ja', tweet_mode='extended', max_id=next_max_id-1)
    for tweet in  tweets:
        search_word = search_word
        date_time = tweet.created_at
        user_id = tweet.user.id_str
        tweet_id = tweet.id_str
        like = tweet.favorite_count
        retweet = tweet.retweet_count
        tweet = remove_emoji(tweet.full_text)

    results_info = pd.Series([search_word, date_time, user_id, tweet_id, like, retweet, tweet], index=df_twitter.columns)

    if re.search('sample', tweet) == None:
        pass
    else:
        df_twitter = df_twitter.append(results_info, ignore_index=True)

df_twitter
"""


#検索キーワード
search_word = "TENET -filter:retweets -filter:replies"

df_twitter = pd.DataFrame(columns=['search_word', 'date_time', 'user_id', 'tweet_id', 'like', 'retweet', 'tweet'])

try:
    responses = api.search(q=search_word, count=1, result_type='result_type', lang='ja', tweet_mode='extended')
except tweepy.error.TweepError as tweepy_error:
    print(tweepy_error)

next_max_id = responses[-1].id

i = 0

while True:
    print("検索ページ" + str(i))

    try:
        responses = api.search(q=search_word, count=100, max_id=next_max_id-1, lang='ja', tweet_mode='extended')
        if len(responses) > 0:
            next_max_id = responses[-1].id 
        else:
            print("これ以上は取得できません。検索ツイートが７日以上か、検索のボリュームが少なすぎます。")
            break

        for tweet in responses:
            search_word = search_word
            date_time = tweet.created_at
            user_id = tweet.user.id_str
            tweet_id = tweet.id_str
            like = tweet.favorite_count
            retweet = tweet.retweet_count
            tweet = remove_emoji(tweet.full_text)

        results_info = pd.Series([search_word, date_time, user_id, tweet_id, like, retweet, tweet], index=df_twitter.columns)

        if re.search("TENET", tweet) == None:
            pass
        else:
            df_twitter = df_twitter.append(results_info, ignore_index=True)

    except tweepy.error.TweepError as tweepy_error:
        print(tweepy_error) 
        break
    except tweepy.error.RateLimitError as limit_error:
        print("検索の上限に達しました")
        break

    i += 1
    if (i == 50):
        print("上限に達しました。上限は１５分後にリセットされます。")
        break
print ("Finish Search")