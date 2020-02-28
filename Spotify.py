import pandas as pd
import sympy
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity

sympy.init_printing()

data = pd.read_csv("top50.csv", encoding="ISO-8859-1")
data.index = [data["Track.Name"]]

data = data[
    [
        "Beats.Per.Minute",
        "Energy",
        "Danceability",
        "Loudness..dB..",
        "Liveness",
        "Valence.",
        "Length.",
        "Acousticness..",
        "Speechiness.",
        "Popularity",
    ]
]


def index_to_instance(df, index=None):
    if index:
        return XYZ(df)[index][1]
    else:
        return XYZ(df)


def XYZ(df):
    return sorted(
        list(zip(list(df.index.codes[0].data), list(df.index.levels[0].array)))
    )


def value_to_index_map(array):
    array1 = zip(array, range(len(array)))
    return array1


index_to_instance(data, 10)


class RecSysContentBased:
    def __init__(self):
        pass

    def fit(self, train):
        self.train_set = train
        df1 = cosine_similarity(train)
        self.similarity = df1
        self.distances = pairwise_distances(train, metric="euclidean")

    def evaluate(self, user):
        d = sorted(value_to_index_map(self.distances[user]))
        idx = range(len(d))
        inst = list(index_to_instance(self.train_set, d[i][1]) for i in idx)
        return inst

    def predict(self):
        pass

    def test(self, testset):
        pass


model = RecSysContentBased()
model.fit(data)
print(
    "Top 5 Songs closest to {0} are: \n{1}".format(
        index_to_instance(data, 10), pd.Series(model.evaluate(10)[1:6])
    )
)
