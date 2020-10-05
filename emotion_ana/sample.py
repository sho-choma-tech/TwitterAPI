# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = '''
今日はガチ勢の友人と一緒にボルダリングをした。休日だけあってとても混んでいたが、その分他の人の登り方を参考にしたり、アドバイスを受けることができた。  
おかげで、今まではどう登ればいいのかわからなかった壁の登り方がわかり、実際に登ることができたのでとても気分が良い。  
また、上手い人の登り方を見ていると「自分の課題」も浮き彫りになるので、とても参考になる。  
平日は自分が登ることがメインで、休日は人の登り方を参考にじっくり登る、といった使い分けができそうだ。  
'''

document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document)

for sentence in sentiment.sentences:
    print(sentence.text.content, sentence.sentiment.score, sentence.sentiment.magnitude)