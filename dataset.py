import utils.py
import api.py


init_printing()
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


tracks = sourcePlaylist["tracks"]
songs = tracks["items"]
track_ids = []
track_names = []
features = []


for i in range(0, len(songs)):
    if songs[i]["track"]["id"] is not None:
        track_ids.append(songs[i]["track"]["id"])
        track_names.append(songs[i]["track"]["name"])


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


rec_tracks = []
rec_track_ids = []
rec_track_names = []
rec_features = []


for i in playlist_df["id"].values.tolist():
    rec_tracks += sp.recommendations(seed_tracks=[i], limit=int(len(playlist_df) / 2))[
        "tracks"
    ]


for i in rec_tracks:
    rec_track_ids.append(i["id"])
    rec_track_names.append(i["name"])


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
