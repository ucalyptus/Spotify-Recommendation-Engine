import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse import csr_matrix, hstack

from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import cosine_distances
from sklearn.metrics import pairwise_distances

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

# %matplotlib inline
from IPython import get_ipython
# %config InlineBackend.figure_format = 'retina'
from IPython.display import set_matplotlib_formats
# %matplotlib notebook
from IPython import get_ipython

import sympy
from sympy import Matrix, init_printing
from scipy.sparse.linalg import svds, eigs

from time import time

import surprise
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate


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
        return list(index_to_instance(self.train_set, d[i][1]) for i in range(len(d)))

    def predict(self):
        pass

    def test(self, testset):
        pass
