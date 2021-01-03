import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('model2.vec', binary=False)

posi_list = ['優れる', '良い','喜ぶ','褒める', 'めでたい','賢い','善い', '適す','天晴',
 '祝う', '功績','賞','嬉しい','喜び','才知','徳', '才能','素晴らしい','芳しい','称える',
 '適切','崇める','助ける','抜きんでる','清水','雄雄しい','仕合せ','幸い','吉兆','秀でる']

nega_list = ['悪い', '死ぬ', '病気', '酷い', '罵る', '浸ける', '卑しい',
 '下手', '苦しむ', '苦しい', '付く', '厳しい', '難しい', '殺す', '難い', '荒荒しい',
 '惨い', '責める', '敵', '背く', '嘲る', '苦しめる', '辛い', '物寂しい', '罰', '不貞腐る',
 '寒い', '下らない', '残念', 'うざい']

def posi_nega_score(x):
    #ポジティブ度合いの判定
    posi = []
    for i in posi_list:
        try:
            n = model.similarity(i, x)
            posi.append(n)
        except:
            continue
    try:
        posi_mean = sum(posi)/len(posi)
    except:
        posi_mean = 0

    #ネガティブ度合いの判定
    nega = []
    for i in nega_list:
        try:
            n = model.similarity(i, x)
            nega.append(n)
        except:
            continue
    try:
        nega_mean = sum(nega)/len(nega)
    except:
        nega_mean = 0
    if posi_mean > nega_mean:
        return posi_mean
    if nega_mean > posi_mean:
        return -nega_mean
    else:
        return 0

print(posi_nega_score('うざい'))