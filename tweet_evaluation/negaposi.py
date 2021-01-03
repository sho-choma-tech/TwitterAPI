import util
import numpy as np
import numba
from sklearn.feature_extraction.text import CountVectorizer

data = np.array([
        ['まじで酷すぎ本当にうざったい', -4]
        , ['これは本当によかった', 5]
        , ['面白すぎまじでワロタ', 5]
        , ['金の無駄。二度と買わない', -5]
        , ['まじ卍', 4]
    ])

@numba.jit
def cvectizer(docs):
    vectizer = CountVectorizer(analyzer=util.words_terms)
    x = vectizer.fit_transform(docs)
    return x, vectizer

@numba.jit
def PosiNega(x, ratings):
    row, col = x.shape
    PosiNegaByRow = np.zeros((row, col))
    PosiNegaByCol = np.zeros(col)
    for row_, rate in zip(range(row), ratings):
        for col_ in range(col):
            ans = rate * np.log10( x[row_, col_] / np.sum( x[row_, :] )  +1  )
            PosiNegaByRow[row_][col_] = ans
    PosiNegaByCol = np.sum(PosiNegaByRow, axis=0)
    return PosiNegaByCol

x, vectizer = cvectizer(data[:,0])

#単語ごとの極性を算出する
#文章に紐付けさたスコアの値
ratings = data[:, 1].astype(np.int)

#それぞれの形態素毎に対するスコア指標
posinega_arr = PosiNega(x, ratings)

#print(posinega_arr)

#print(data[:, 0])

polar_dict = np.array((vectizer.get_feature_names(), posinega_arr)).T