# IMDb Top 250 Movies Analysis

## Project Overview
This project analyzes IMDb's Top 250 movies, examining key metrics like release year, duration, star ratings, and vote counts to uncover trends and insights, showcasing essential data analysis skills.

## Objective
The objective of this project is to analyze IMDb's Top 250 movies to uncover trends and characteristics of highly-rated films, providing insights into the movie industry and showcasing data analysis skills.

## IMDb Criteria for Top 250 Movies
- The Top Rated Movie list only includes feature films.
- Shorts, TV movies, and documentaries are not included.
- The list is ranked by a formula which includes the number of ratings each movie received from users, and the value of ratings received from regular users.
- To be included on the list, a movie must receive ratings from at least 25,000 users.

## Data Collection
The dataset includes the following columns:
- **Movie Title**
- **Released Year**
- **Duration**
- **Restricted Rating**
- **Rating (Star out of 10)**
- **User Vote**
- **Director (1)**
- **Director (2)**
- **Director (3)**
- **Starring (1)**
- **Starring (2)**
- **Starring (3)**
- **Synopsis**

## Tools and Technologies
- **Python**: for web scraping and data analysis
- **Selenium**: for web scraping
- **Pandas** and **NumPy**: for data manipulation
- **Matplotlib** and **Seaborn**: for data analysis visualization
- **Tableau**: for dashboard visualization

## Exploratory Data Analysis (EDA)
The exploratory analysis includes:

### Number of Movies by Release Year
![Release Year Distribution](/visualizations/Number%20of%20Movies%20by%20Release%20Year.png)

### Average Duration of Movies Over the Years
![Average Duration](/visualizations/Average%20Duration%20of%20Movies%20Over%20the%20Years.png)

### Distribution of Ratings
![Rating Distribution](/visualizations/Distribution%20of%20IMDb%20Ratings.png)

### Director and Cast Analysis
![Top Directors](/visualizations/Top%20Directors.png)
![Top Actors/Actresses](/visualizations/Top%20ActorsActresses.png)

### Example Code Snippets

#### Count of Movies by Release Year
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('scrapedData\cleaned_v3.0.csv')

# Count of movies by release year
plt.figure(figsize=(14,7))
sns.histplot(data=df, x='Released Year', bins=20, kde=False)
plt.xticks(rotation=90)
plt.title('Number of Movies by Release Year')
plt.xlabel('Released Year')
plt.ylabel('Number of Movies')
plt.show()
