import MeCab
from janome.dic import UserDictionary
from janome import sysdic 
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer

import numpy as np 


PART_OF_SEARCH = ("名詞", "形容詞", "動詞", "形容動詞")

#文章の分割
def split_word(text, to_stem=False):
    tagger = MeCab.Tagger('mecabrc')
    results = tagger.parse(text)

    #品詞を分解，それぞれカウント
    words_results = results.split('\n')
    words = []
    for i in words_results:
        if i == 'EOS' or i == '':
            break
        i = i.replace('\t', ',')
        i_elms = i.split(',')

        if i_elms[1] not in PART_OF_SEARCH:
            continue
        if to_stem and i_elms[7] != '*':
            words.append(i_elms[7])
        else:
            words.append(i_elms[0])
    return words

#基本形に返す
def words_stems(text):
    stems = split_word(text, to_stem=True)
    return stems

#原型を返す
def words_terms(text):
    terms = split_word(text, to_stem=False)
    return terms
