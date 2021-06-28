# TwitterAPI

## データ準備

```
┣ data/
    ┣ emotion_score/  - 感情レベルを定量的にスコア化されたデータ
    ┃      ┣ Donald_Trump_emotion.csv - ドナルド・トランプ氏に関するツイート
    ┃      ┣ uzai_emotion.csv - 「うざい」が含まれているツイート（ネガティブ分析）
    ┃      ┗　 warota_emotion.csv - 「ワロタ」が含まれているツイート（ポジティブ分析）             
    ┗　original_data/  - Twitter APIを利用して取得した元データ
           ┣ Donald_Trump_data.csv 
           ┣ uzai_data.csv 
           ┣ warota_data.csv 
           ┗　 sample.csv  - テスト用で取得したデータ
```

## Reference
- [内容資料：slide share](https://www.slideshare.net/shokazari/twitter-249510624)
