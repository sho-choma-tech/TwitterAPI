import tweepy
import json, os, datetime
import re
import emoji
import pandas as pd 
import numpy as np 

from google.cloud import language 
from google.cloud.language import enums 
from google.cloud.language import types 

#環境変数設定
credpath = '/content/drive/My Drive/************/*******************.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credpath

#from google.colab import drive 
#drive.mount('/content/drive')


#データの取得
df_data = pd.read_csv('/content/drive/My Drive/3IS_Project/sample_data.csv')
df_data = df_data[['投稿日', 'ID', 'User_name', 'text', 'favorite', 'retweet_count', 'followers']]

#絵文字の削除
def remove_emoji(text_str):
    return ''.join(c for c in text_str if c not in emoji.UNICODE_EMOJI)


def text_sentiment(text_content, lang='ja'):
    '''
    #Analyzing Sentiment in a String

    # parameter:
    # text: The text content to analyze, string, required
    # lang: language (e.g. en, ja), string, default = 'ja'
    '''

    client = language.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT
    
    # For list of supported languages 
    # https://cloud.google.com/natural-language/docs/languages
    document = {"content" : text_content, "type" : type_, "language" : lang}
    encoding_type = enums.EncodingType.UTF8
    responce = client.analyze_sentiment(document, encoding_type=encoding_type)

    return responce


def tweet_emotion(df, data_path, upadate=True, csv=True):

  """
  #parameter 
  -------------
  df: required, dataframe (columns=['投稿日', 'ID', 'User_name', 'Screen_name', 'text', 'favorite', 'retweet_count', 'followers', 'follows', 'user_mentions'])
  data_path: required, str, path of the output csv files
  update: default=True, bool
  csv: default=True, bool

  return 
  -------------
  dataframe (columns=['投稿日', 'ID', 'User_name', 'text', 'favorite', 'retweet_count', 'followers'])
  """
  del_pattern = re.compile(r"(https?://[\w/:%#\$&\?\(\)~\.=\+\-]+|(RT )?\@[\w]+|\n)")
  tz_jst = datetime.timezone(datetime.timedelta(hours=9))

  out_latest = data_path + 'emotion_data.csv'

  ts = pd.to_datetime(df_data['投稿日'], utc=True)

  arr = []
  col_name = list(df_data.columns) + ['score', 'magnitude']
  for idx, i in df.iterrows:
      txt = del_pattern.sub('', i.tweet)
      ret = text_sentiment(txt).document_sentiment
      lst = [r for r in i] + [round(ret.score, 1), round(ret.magnitude, 1)]
      arr.append(lst)

    res = pd.DataFrame(arr, columns=col_name)

    if upadate and csv and os.path.isfile(out_latest):
        p = os.stat(out_latest)
        dt = datetime.datetime.fromtimestamp(p.st_mtime, tz_jst).strftime('%Y%m%d%H%M')
        os.rename(out_latest, '{}tweet_emotion.csv{}'.format(data_path, dt))
    else:
        pass

    if csv:
        res.to_csv(out_latest)
    
    return res 

