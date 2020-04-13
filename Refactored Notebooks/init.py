import utils.py
import api.py

if token:
    sp = spotipy.Spotify(auth=token)

else:
    print("Can't get token for", username)

get_ipython().run_line_magic('matplotlib', 'notebook')

model = RecSysContentBased()
model.fit(data)

print(
    "Top 5 Songs closest to {0} are: \n{1}".format(
        index_to_instance(data, 10), pd.Series(model.evaluate(10)[1:6])
    )
)
