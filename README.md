# Rock Through The Ages

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
- Cameron Brody, crbrody@ucsd.edu
- Richard Duong, r3duong@ucsd.edu
- Thomas Evans-Barton, tevansba@ucsd.edu
- Brian Cheng, brc042@ucsd.edu

## Abstract

(10 points) 

For our project we decided to take a look at how music changes over time. In order to do that, we wanted to choose a musical genre and utilize a classifier to see if it would be able to correctly classify songs as what decade they’re from. We decided to choose Rock and Roll as our genre due to its popularity, distinguishing characteristics, and persistence through the ages.

To collect data, we utilized Spotify’s large library of music, which provided us not only with clips of each song for analysis, but also features that describe the song. These features include things which are descriptors of the song, e.g. tempo and key, but also features that Spotify engineered from the songs, such as “energy” and “danceability”. These features were excellent for our classifier, and allowed for straightforward features.

We utilized these features to create a classifier with sklearn, which was able to successfully classify ~37% of the testing data. This is significantly more successful than a naive approach, which would be 1/7, ~14%. Rock and Roll may be its own distinguishable genre, but within it are clearly many different styles that have changed over the years.

## Data

(10 points) 

Our data is obtained through the Spotify API. Our project is building a classifier of Rock music by decade, and the data we used to achieve this task were 1. Basic track data which includes album info etc. and 2. Spotify audio features. Spotify audio features contain some basic raw data such as loudness, tempo, etc but also their own engineered features such as “danceability” and “speechiness”. The info for each specific Spotify audio feature can be found at: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/ The data should be the most recent till the date we obtained the data.
 
To access the data, we made a playlist of the songs we wanted then called the Spotify API to get the data from the playlist.

Since we were looking at Rock through the ages, we decided to separate our data by decade, starting in the 1950’s and going until the 2010’s. Each decade of our training data contained 5 of the most popular Rock songs from that decade. The training data is the same, but with different songs of course. Each decade has a variety of artists, though some artists are repeated within a decade.

## Code

(20 points)

Notebook:
https://github.com/ucsd-dsc-arts/dsc160-midterm-group17/blob/master/code/DSC%20106%20Midterm.ipynb

Our code accesses the Spotify API through the package Spotipy in order to retrieve features for the Logistic Regression model that we use to predict which decade our songs are from. To access the data, we used Spotipy to access playlists that we created containing the training and test songs. 
	The cleaning/re-organizing we have to do include extracting the release date (we found it under the album info) and then categorize each release date into their decades. We then merge the basic track data and audio features together and pair each audio feature into their supposed decade that came out.
For the model, we extracted 7 key features from the API, valence, energy, danceability, loudness, speechiness, tempo, and instrumentalness. We trained the logistic regression classifier from sklearn on our training song set using these 7 features. We then used this model to predict the labels of our test song set.
Additionally, all graphs included in our project were created in our notebook.

## Results

(30 points) 

Our classifier was made using a Logistic Regression classifier, and was able to successfully predict ~37% of the songs we tested. Since we have 7 decades as labels, a naive classifier randomly guessing the decade would get ~14% correct. This means that our classifier was significantly more accurate than a random guess, but wasn’t entirely accurate with its prediction. So it seems that Rock and Roll has changed a fair bit over the decades, but not enough so that our classifier would be able to predict with too much accuracy.
When looking deeper into how the classifier performed on the test set, we can see that it performed very well on certain decades, while not performing nearly as well on others:


From this visualization, it is evident that the classifier does very well on songs from the 1980s, fairly well with songs from the 1950s, 70s, and 00s, and very poorly on songs from the 1960s and 1990s. This is a curious revelation, however, some of these issues can be explained when examining the (normalized) variables that we were feeding into our classifier:
What we can see here is the normalized attributes of each decade in the training set. What this shows us is that it makes sense as to why the 1970s had reasonably good classification, due to its very distinct sound profile. It makes a little less sense as to why 1980s classification was so consistent, however, it does have a fairly unique danceability number as well as a unique ‘instrumentalness’ and tempo. For the 1960s and 1990s on the other hand, it is understandable as to why these decades were difficult to classify, as the majority of their sound profile variables hovered just around the average, causing it to lack a certain level of distinctness.

Overall, our classifier performed very well for certain decades, and less well for others, however, when compared to a naive classifier, it is reasonable to be optimistic and satisfied with its level of success.

## Discussion

(30 points, three to five paragraphs)

The classifier we made was able to correctly classify ~37% of the testing songs we selected. This is quite a bit stronger than a naive guessing method, which would be 1/7, ~14%, since we have 7 decades (or labels) in our classifier. 

One of Billy Joel’s classic hits “Still Rock and Roll To Me” helps show why this examination is culturally significant. Many critics over the years have arbitrarily decided what is and isn’t rock and roll. Does our classifier back up Billy Joel? Or does it show that rock and roll really has changed? Since our classifier was successful significantly more often than a naive classifier, that means it’s more able to distinguish successfully between the decades. So perhaps Billy Joel was wrong, and rock and roll has in fact changed significantly over the years.

As far as artistic interpretation, this classifier is very different from typical musical analysis. A musician would look at the instrumentation, complexity, themes, and overall mood of a song in order to distinguish its decade of origin. We, on the other hand, used engineered features that describe the songs in a general way, e.g energy and instrumentality. I believe that most artistic analysts would frown upon our analysis, since it doesn’t factor in a lot of what makes music so distinguishable.

If we were to continue this experiment, I would like to use more songs in general, since it would help paint a broader picture of the decades. We could also engineer more features that help describe the data in different ways. Finally, it would also be interesting to expand this to include other genres as well. That would help us see what genres change more or less than others.

## Team Roles

Cameron: Planning, Spotify API setup, writing

Richard: Classifier creation, writing

Thomas: Classifier creation, writing

Brian: Spotify API setup, data obtaining/cleaning, writing

## Technical Notes and Dependencies

This project heavily utilizes the Spotipy package, which interfaces with the Spotify API through Python. Anyone wanting to run this code would need to setup a Spotify API account in order to obtain API keys for usage, as well as a Spotify account. Additionally, our project utilized numpy, pandas, and sklearn to process our data and implement our classifier. The urllib package was used to download song samples which were not utilized in our classifier.

## Reference

Spotify API: https://developer.spotify.com/documentation/web-api/
Spotipy documentation: https://spotipy.readthedocs.io/en/2.12.0/
