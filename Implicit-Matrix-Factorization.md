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


## Matrix Factorization ##

Matrix factorization is a common and effective way to implement a recommendation system. Using the bellow-mentioned user-item dataset (Figure 1), matrix factorization attempts to learn ways to quantitatively characterize both users and items in a lower-dimensional space (as opposed to looking at every item the user has ever rated), such that these characterizations can be used to predict user behavior and preferences for a known set of possible items. In recent years, matrix factorization has become increasingly popular due to its accuracy and scalability.

Using the data set of user-item pairings, one can create a matrix such that all rows represent different users, all columns represent different items, and each entry at location (i, j) in the matrix represents user i’s rating for item j.

![Figure_1](https://github.com/ucalyptus/Spotify-Recommendation-Engine/blob/master/images/1_NS47i4lrDJUC1P3B-cdRtA.png)

So, we know that we can decompose a matrix by finding two matrices that can be multiplied together to form our original matrix.
When these two separate matrices are created, they each carry separate information about song title, items(songs), and the relationships between them. Namely, one of the matrices will store information that characterizes song title, while the other will store information about the charastics of songs. In fact, every row of the user (left) matrix is a vector of size k that quantitatively describes a single song, while every column of the item (right) matrix is a vector of size k that characterizes a single song parameters. The size of these vectors, k, is called the latent dimensionality (or embedding size), and is a hyperparameter that must be tuned in the matrix factorization model — a larger latent dimentionality will allow for the model to capture more complex relationships and store more information.

The following figure (Figure 2) dipict the matrix factorisation in user-item form.
![Figure 2](https://github.com/ucalyptus/Spotify-Recommendation-Engine/blob/master/images/1_gNYLtTeeCOkpwJGeOaWhjg.png)
