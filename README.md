# TwitterAPI

## 概要
- GCPやTwitter APIを利用してタイムラインの感情レベルを指標化
- パッケージや辞書にはないスラングや俗語の評価の拡張を行う

## データ準備

```
┣ data/
    ┣ emotion_score/  - 感情レベルを定量的にスコア化されたデータ
    ┃     ┣ ...
    ┃     ┗　hoge.csv
    ┃
    ┗　original_data/  - Twitter APIを利用して取得した元データ
          ┣ ... 
          ┗ hoge.csv 
```

## ディレクトリ構成
```
┣　data /    - 元データや感情スコアデータの管理ファイル
    ┣ emotion_score/  
    ┃     ┣ ...
    ┃     ┗　hoge.csv
    ┃
    ┗　original_data/  
          ┣ ... 
          ┗ hoge.csv 
          
┣ emotion_gcp/  - Google Natural languageの実行やAPI権限ファイル
    ┣ get_emotion.py     
    ┗ My_Project..._XXX.json 
    
┣ tweet_morpheme/   - 形態素解析の実行ファイル
    ┣ dic
       ┗ ... 
    ┣　neologd
       ┗ ...
    ┣　neologd.csv   -　形態素解析用ファイル
    ┗　morpheme.py
    
┣ tweet_data/   - Twitter APIの権限やデータ取得の実行ファイル
    ┣　config.py
    ┣　get_tweet.py 
    
┣ tweet_data/   - Fast Text,ルールベースの実行ファイル
    ┣　fast_text.py
    ┣　negaposi.py 
    ┗　util.py
    
    
```

## 開発環境


## Reference
- [内容資料：slide share](https://www.slideshare.net/shokazari/twitter-249510624)
