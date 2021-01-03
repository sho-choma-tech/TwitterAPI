import pandas as pd 
import numpy as np
import os, re 

import MeCab
from janome.dic import UserDictionary
from janome import sysdic
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *

uzai_data = pd.read_csv('../data/uzai_data.csv')
uzai_data = uzai_data.rename(columns={'Unnamed: 0':'index'})

user_dict = UserDictionary('neologd.csv', 'utf8', 'ipadic', sysdic.connections)
user_dict.save('neologd')

t = Tokenizer(udic='userdic.csv', udic_enc='utf8')
char_filters = [UnicodeNormalizeCharFilter()]
analyzer = Analyzer(char_filters=char_filters, tokenizer=t)

uzai_words_list = []
for i, row in uzai_data.iterrows():
    for t in analyzer.analyze(row[4]):
        surf = t.surface           #形態素
        base = t.base_form         #基本形
        pos = t.part_of_speech     #品詞
        reading = t.reading        #読み
        phonetic = t.phonetic      #振り仮名

        uzai_words_list.append([i, surf, base, pos, reading, phonetic])

uzai_words_list = pd.DataFrame(uzai_words_list, columns=['index', '単語', '基本形', '品詞', '読み', '振り仮名'])

uzai_morpheme_data = pd.merge(uzai_data, uzai_words_list, how='left', on='index')
uzai_morpheme_data['品詞'] = uzai_morpheme_data['品詞'].apply(lambda x: x.split(',')[0])