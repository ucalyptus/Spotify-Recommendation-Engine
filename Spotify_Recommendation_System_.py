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

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
# %matplotlib inline
from IPython import get_ipython
# %config InlineBackend.figure_format = 'retina'
from IPython.display import set_matplotlib_formats
get_ipython().run_line_magic('matplotlib', 'inline')
set_matplotlib_formats('retina')

cid = "ffbef2bcb4b84e80b3a0039a2906cb01"
secret = "6c57daa1247f4abe96f38635d38869a0"
username = "francocasadei"
redirect_uri = "https://developer.spotify.com/dashboard/applications/ffbef2bcb4b84e80b3a0039a2906cb01"
scope = "user-library-read playlist-modify-public playlist-read-private"

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)

else:
    print("Can't get token for", username)


# https://open.spotify.com/user/francocasadei/playlist/6aWL6tZgIycyz98WgigfsG
sourcePlaylistID = "6aWL6tZgIycyz98WgigfsG"
sourcePlaylist = sp.user_playlist(username, sourcePlaylistID)
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]
track_ids = []
track_names = []


for i in range(0, len(songs)):
    if songs[i]["track"]["id"] is not None:
        track_ids.append(songs[i]["track"]["id"])
        track_names.append(songs[i]["track"]["name"])


features = []


for i in range(0, len(track_ids)):
    audio_features = sp.audio_features(track_ids[i])
    for track in audio_features:
        features.append(track)


playlist_df = pd.DataFrame(features, index=track_names)
# francocasadei@yahoo.it:astrolabio
playlist_df = playlist_df[
    [
        "id",
        "acousticness",
        "danceability",
        "duration_ms",
        "energy",
        "instrumentalness",
        "key",
        "liveness",
        "loudness",
        "mode",
        "speechiness",
        "tempo",
        "valence",
    ]
]
playlist_df.shape
playlist_df["ratings"] = [
    10,
    9,
    9,
    10,
    8,
    6,
    8,
    4,
    3,
    5,
    7,
    5,
    5,
    8,
    8,
    10,
    4,
    6,
    8,
    2,
    4,
    5,
    6,
    9,
]
X_train = playlist_df.drop(["id", "ratings"], axis=1)
y_train = playlist_df["ratings"]
sns.set(style="white")
X_scaled = StandardScaler().fit_transform(X_train)
pca = decomposition.PCA().fit(X_scaled)
plt.figure(figsize=(10, 7))
plt.plot(np.cumsum(pca.explained_variance_ratio_), color="k", lw=2)
plt.xlabel("Number of components")
plt.ylabel("Total explained variance")
plt.xlim(0, 12)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.axvline(8, c="b")
plt.axhline(0.95, c="r")
plt.show()

# Fit your dataset to the optimal pca
pca = decomposition.PCA(n_components=8)
X_pca = pca.fit_transform(X_scaled)
v = TfidfVectorizer(sublinear_tf=True, ngram_range=(1, 6), max_features=10000)
X_names_sparse = v.fit_transform(track_names)
X_names_sparse.shape
X_train_last = csr_matrix(hstack([X_pca, X_names_sparse]))
skf = StratifiedKFold(n_splits=2, shuffle=True, random_state=42)

knn_params = {"n_neighbors": range(1, 10)}
knn = KNeighborsClassifier(n_jobs=-1)
knn_grid = GridSearchCV(knn, knn_params, cv=skf, n_jobs=-1, verbose=True)
knn_grid.fit(X_train_last, y_train)
knn_grid.best_params_, knn_grid.best_score_

tree = DecisionTreeClassifier()
tree_params = {"max_depth": range(1, 11), "max_features": range(4, 19)}
tree_grid = GridSearchCV(tree, tree_params, cv=skf, n_jobs=-1, verbose=True)
tree_grid.fit(X_train_last, y_train)
tree_grid.best_estimator_, tree_grid.best_score_
rec_tracks = []

for i in playlist_df["id"].values.tolist():
    rec_tracks += sp.recommendations(seed_tracks=[i], limit=int(len(playlist_df) / 2))[
        "tracks"
    ]

rec_track_ids = []
rec_track_names = []

for i in rec_tracks:
    rec_track_ids.append(i["id"])
    rec_track_names.append(i["name"])

rec_features = []

for i in range(0, len(rec_track_ids)):
    rec_audio_features = sp.audio_features(rec_track_ids[i])
    for track in rec_audio_features:
        rec_features.append(track)

rec_playlist_df = pd.DataFrame(rec_features, index=rec_track_ids)
rec_playlist_df = rec_playlist_df[
    [
        "acousticness",
        "danceability",
        "duration_ms",
        "energy",
        "instrumentalness",
        "key",
        "liveness",
        "loudness",
        "mode",
        "speechiness",
        "tempo",
        "valence",
    ]
]
tree_grid.best_estimator_.fit(X_train_last, y_train)
rec_playlist_df_scaled = StandardScaler().fit_transform(rec_playlist_df)
X_test_pca = pca.transform(rec_playlist_df_scaled)
X_test_names = v.transform(rec_track_names)
X_test_last = csr_matrix(hstack([X_test_pca, X_test_names]))
y_pred_class = tree_grid.best_estimator_.predict(X_test_last)
rec_playlist_df["ratings"] = y_pred_class
rec_playlist_df = rec_playlist_df.sort_values("ratings", ascending=False)
rec_playlist_df = rec_playlist_df.reset_index()
recs_to_add = rec_playlist_df[rec_playlist_df["ratings"] >= 9]["index"].values.tolist()
playlist_recs = sp.user_playlist_create(
    username,
    name="PCA + tf-idf + DT - Recommended Songs for Playlist - {}".format(
        sourcePlaylist["name"]
    ),
)
sp.user_playlist_add_tracks(username, playlist_recs["id"], recs_to_add)
