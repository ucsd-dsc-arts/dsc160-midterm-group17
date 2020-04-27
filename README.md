# Project Title

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
- Cameron Brody, crbrody@ucsd.edu
- Richard Duong, r3duong@ucsd.edu
- Thomas Evans-Barton, tevansba@ucsd.edu
- Brian Cheng, brc042@ucsd.edu

## Abstract

(10 points) 

	For our project, we’re taking a look at how genres of music can change over time. With a classifier trained on music of a certain genre from a number of certain time periods, e.g 70’s Rock and Roll, we can try to look at music from the same genre but a different time period. With this, we can try to analyze certain songs, albums, and artists within the context of musical trends of the time. If a song is classified incorrectly, what features cause that? Additionally, we can observe how different genres change at different rates by looking at the features over time. Do the features in Hip-Hop change faster or slower over time when compared with Pop?
	As for data, we can use any number of songs from different genres. Ideally, we can download however many songs we need per genre and time period so that we can populate as many genres as possible. Spotify’s API would allow us to access a huge number of songs to analyze, and provides built-in methods for extracting key features for each song. This includes acousticness, danceability, energy, etc. and will be the most important aspects that we measure for each song. These will be the values we use in our model.
	This project is a sort of expansion of Exercise 2 with similar techniques, but we plan on increasing the scope by applying it with two variables - genre and time period. I predict that some genres definitely will have more change over time than others. We hypothesize that something like classical probably won’t change too much due to the grand scope of the genre, but hip-hop has aged tremendously since its inception until now. I also predict that some standout artists might be classified as being from a different time period. Many artists use an old-fashioned style intentionally, which might throw off the prediction.


## Data

(10 points) 

This section will describe your data and its origins. Each item should contain a name of the data source, a link to the source, and any necessary background information such as:
- What is your cultural data source? 
- When was it made? 
- Who created the works? 
- Is it digital native, or is it some kind of scan, recording, photo, etc., of an analog form? 

## Code

(20 points)

This section will link to the various code for your project (stored within this repository). Your code should be executable on datahub, should we choose to replicate your result. This includes code for: 

- data acquisition/scraping
- cleaning
- analysis
- generating results. 

Link each of your notebooks or .py files within this section, and provide a brief explanation of what the code does. Reading this section we should have a sense of how to run your code.

## Results

(30 points) 

This section will contain links to documentation of your results. This can include figures, sound files, videos, bitmaps, as appropriate to your domain of analysis. Each result should include a brief textual description, and all should be listed below: 

- image files (`.jpg`, `.png` or whatever else is appropriate)
- audio files (`.wav`, `.mp3`)
- written text as `.pdf`

## Discussion

(30 points, three to five paragraphs)

The first paragraph should be a short summary describing your results.

The subsequent paragraphs could address questions including:
- Why is this culturally relevant?
- How does your computational approach differ from the traditional art historical, musicological, manuel/subjective approach to analyzing your cultural subject? 
- How do you think the original artists/musicians would respond to this type of analysis? Would it change/inform their practice in some way?
- How do your results relate to broader social, cultural, economic political, etc., issues? 
- In what future directions could you expand this work?

## Team Roles

Provide an account of individual members and their efforts/contributions to the specific tasks you accomplished.

## Technical Notes and Dependencies

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
- Does this code require other pip packages, software, etc?
- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts
