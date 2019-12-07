![](https://ucalyptus.github.io/Spotify-Recommendation-Engine/spotify.gif)

***
## Music recommender system.
## Steps for Layman
### 1.This is my input data
![This is my playlist I feed it to ](images/playlist_screenshot.png)
### 2.Spotify has inhouse functions to  extract track details.
![After I use Spotify API to fetch tracks and arrange it into a df ](https://developer.spotify.com/assets/WebAPI_intro.png)
### 3.This is the extracted dataframe
![Dataframe](images/dataframe_screenshot.png)
### 4.I do Data Analysis and use well known statistical techniques.

## Requirements
* spotipy
```bash
 pip install spotipy
```
## Voila! ,we convert this into a simple data analytics problem.Thanks to this Python wrapper Spotipy


*[Read more about Spotify's recommendation algorithm](Implicit-Matrix-Factorization.md)*

## Statistical techniques Involved:
### 1.Term Frequency Inverse Document Frequency
[Extracting Keywords with TF-IDF and Python’s Scikit-Learn](https://kavita-ganesan.com/extracting-keywords-from-text-tfidf/#.XeUx9ugzbcc) 
[TF-IDF from scratch in python on real world dataset](https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089)

### 2.Principal Component Analysis
[DeZyre - Principal Component Analysis](https://www.dezyre.com/data-science-in-python-tutorial/principal-component-analysis-tutorial#:~:targetText=Principal%20Component%20Analysis%20Tutorial,-As%20you%20get&targetText=The%20main%20idea%20of%20principal,up%20to%20the%20maximum%20extent.)

### 3.Stratified K Fold Cross Validation
[A Gentle Introduction to k-fold Cross-Validation](https://machinelearningmastery.com/k-fold-cross-validation/) 
[SciKit Learn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html)

### 4.KNN
[Machine Learning Basics with the K-Nearest Neighbors Algorithm](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)

### 5.Decision Tree Classifier
[Understanding Decision Trees for Classification (Python)](https://towardsdatascience.com/understanding-decision-trees-for-classification-python-9663d683c952)

### 6.Random Forest Classifier
[An Implementation and Explanation of the Random Forest in Python](https://towardsdatascience.com/an-implementation-and-explanation-of-the-random-forest-in-python-77bf308a9b76) 

[Spotify Developer](https://beta.developer.spotify.com/documentation/web-api/) for more info  
[Gitter Link](https://gitter.im/Spotify-Recommendation-Engine/community) to join the chat room and contribute


### Contributing
 1. Fork the repository.
![image](https://user-images.githubusercontent.com/41269164/70219309-9a3eca80-176a-11ea-8a4d-1bd701d07314.png)
 2. clone the repository.
	`https://github.com/ucalyptus/Spotify-Recommendation-Engine.git`
 3. create a different branch.
	`git checkout -b newbranch oldbranch`
 4. Do the needful changes to solve the issue.
 5. commit the changes and open a pull request.
	`git commit -m "description about changes"`
	`git push origin newbranch`
 6. Making a pull request
![image](https://user-images.githubusercontent.com/41269164/70219707-47194780-176b-11ea-96c2-d0c401ddb1e0.png)
	* click on `Compare and Pull Request`
![image](https://user-images.githubusercontent.com/41269164/70219836-8d6ea680-176b-11ea-81d5-549093bf0954.png)


## KWoC contributors
[@sibasmarak](http://github.com/sibasmarak) - [#15](https://github.com/ucalyptus/Spotify-Recommendation-Engine/pull/15)
