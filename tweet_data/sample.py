# -*- coding: utf-8 -*-

import tweepy
import pandas as pd
import datetime
from time import sleep
import argparse
import config
import emoji

'''
#コマンドラインオプションの設定
parser = argparse.ArgumentParser(description='Twitter APIでツイートを取得')
parser.add_argument('-q', help='検索クエリ')
parser.add_argument('--cnt', default=100, help='取得件数、デフォルト100件')
args = parser.parse_args()
'''

search_words = "誹謗中傷"

#APIの認証
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET


auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

#ツイート取得
tweet_data = []

try:
    responses = api.search(q=search_words, count=1, result_type="result_type", lang="ja", tweet_mode='extended')
except tweepy.error.TweepError as tweepy_error:
    print(tweepy_error)

next_max_id = responses[-1].id

i = 0

while True:
    print('検索ページ' + str(i))

    try:
        responses = api.search(q=search_words, count=100, max_id = next_max_id-1, lang="ja", tweet_mode='extended')
        if len(responses) > 0:
            next_max_id = responses[-1].id
        else:
            print("これ以上は取得できません。検索ツイートが７日以上か、検索のボリュームが少なすぎます。")
            break

        for tweets in responses:
            user_mentions = []
            if tweets.entities['user_mentions']:
                for name in tweets.entities['user_mentions']:
                    user_mentions.append(name['screen_name'])

            mention_names = ','.join(user_mentions)

            tweet_data.append([tweets.created_at.strftime('%Y/%m/%d'),
                           tweets.id, tweets.user.name, tweets.user.screen_name,
                           tweets.full_text.replace('\n', ''), tweets.favorite_count,
                           tweets.retweet_count, tweets.user.followers_count, tweets.user.friends, mention_names])
    except tweepy.error.TweepError as tweepy_error:
        print(tweepy_error)
        break
    except tweepy.error.RateLimitError as limit_error:
        print("検索の上限に達しました")
        break

    i += 1
    if (i == 10):
        print("上限に達しました。上限は１５分後にリセットされます。")
        break
print ("Finish Search")

columns = ["投稿日", "ID", "User_name", "Screen_name", "text", "favorite", "retweet_count", "followers", "follows", "user_mentions"]

df = pd.DataFrame(tweet_data)
df.columns = columns

df