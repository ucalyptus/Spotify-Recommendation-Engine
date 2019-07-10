## Behind the scenes of Spotify's in-house Recommendation API

A common task of recommender systems is to improve
customer experience through personalized recommendations based on prior implicit feedback. These systems passively track different sorts of user behavior, such as purchase history, watching habits and browsing activity, in order to model user preferences. Unlike the much more extensively researched explicit feedback, we do not have any
direct input from the users regarding their preferences. In
particular, we lack substantial evidence on which products
consumer dislike. In this work we identify unique properties of implicit feedback datasets. We propose treating the
data as indication of positive and negative preference associated with vastly varying confidence levels. This leads to a
factor model which is especially tailored for implicit feedback recommenders. We also suggest a scalable optimization procedure, which scales linearly with the data size. The
algorithm is used successfully within a recommender system
for television shows. It compares favorably with well tuned
implementations of other known methods. In addition, we
offer a novel way to give explanations to recommendations
given by this factor model.



