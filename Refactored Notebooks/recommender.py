import utils.py
import api.py
import dataset.py

get_ipython().run_line_magic('matplotlib', 'inline')

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

X_train_last = csr_matrix(hstack([X_pca, X_names_sparse]))
skf = StratifiedKFold(n_splits=2, shuffle=True, random_state=42)

knn_params = {"n_neighbors": range(1, 10)}
knn = KNeighborsClassifier(n_jobs=-1)
knn_grid = GridSearchCV(knn, knn_params, cv=skf, n_jobs=-1, verbose=True)
knn_grid.fit(X_train_last, y_train)


tree = DecisionTreeClassifier()
tree_params = {"max_depth": range(1, 11), "max_features": range(4, 19)}
tree_grid = GridSearchCV(tree, tree_params, cv=skf, n_jobs=-1, verbose=True)
tree_grid.fit(X_train_last, y_train)


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
