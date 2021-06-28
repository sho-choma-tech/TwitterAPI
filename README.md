# TwitterAPI

## 

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
┣ emotion_gcp/
    ┣ get_emotion.py     - Google Natural languageの実行
    ┗ My_Project..._.json  - API権限ファイル
┣ 
    ┃
    ┗　original_data/  - Twitter APIを利用して取得した元データ
          ┣ ... 
          ┗ hoge.csv 
```

## Reference
- [内容資料：slide share](https://www.slideshare.net/shokazari/twitter-249510624)
