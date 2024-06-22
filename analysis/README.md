# Analysis of IMDb Top 250 Movies 

This README.md contains a detailed explanation to the analysis of the top 250 movies listed on IMDb.

## Visualizations

### 1. Distribution of IMDb Ratings

![Distribution of IMDb Ratings](/visualizations/Distribution%20of%20IMDb%20Ratings.png)

This histogram displays the distribution of IMDb ratings for the top 250 movies. The x-axis represents the IMDb ratings, while the y-axis represents the frequency of movies with those ratings. Additionally, a kernel density estimate (KDE) curve is overlaid to show the probability density function of the IMDb ratings.

#### Key Observations:
- The majority of movies have ratings between 8.0 and 8.4.
- There is a noticeable drop in frequency as the ratings increase beyond 8.4.
- The KDE curve indicates a peak around the 8.0 to 8.2 rating range, highlighting it as the most common rating range.

### 2. Number of Movies by Release Year

![Number of Movies by Release Year](/visualizations/Number%20of%20Movies%20by%20Release%20Year.png)

This histogram shows the number of movies released over the years. The x-axis represents the release years, and the y-axis represents the number of movies released in each year range.

#### Key Observations:
- The number of movies released has generally increased over time, with a few fluctuations.
- There is a significant rise in the number of movies released from the 1990s to the early 2000s.
- The number of movies released peaks around the 2000s and then shows a slight decline in recent years.

### 3. Average Duration of Movies Over the Years

![Average Duration of Movies Over the Years](/visualizations/Average%20Duration%20of%20Movies%20Over%20the%20Years.png)

This line chart displays the duration of the movies over th years. The x-axis represents the release years, and the y-axis represents the duration in minutes. 

#### Key Observations: 
- Most movies have durations ranging from 120 to 160 minutes.
- Movie durations normalized to this range starting from the 1960s.
- Movies from the 1920s to 1930s had the shortest durations.

### 4. Top 10 Directors/Actors/Actresses
![Top Directors](/visualizations/Top%20Directors.png)
![Top Actors/Actresses](/visualizations/Top%20ActorsActresses.png)

These bar charts shows the directors, actors, and actresses whose work made it to the top 250 movies multiple times. The x-axis of the charts represents the number of the movies the individuals were involved in that made the list, while the y-axis represents the name of those individuals.

#### Key Observations: 
- Directors within this chart has directed at least 4 movies that made IMDb's top 250 list.
- Actors/Actresses within this chart has starred in at least 4 different movies that made IMDb's top 250 list.
- Diversity in nationality is evident, with names like Akira Kurosawa and Tatsuya Nakadai representing different ethnicities.

#### 5. Correlation Heatmap
![Correlation Heatmap](/visualizations/Correlation%20Heatmap.png)

This heatmap demonstrates the relationships between four variables: Released Year, Duration, Rating (Star out of 10), and User Vote. The values represent the correlation coefficients, indicating the strength and direction of the relationships.

#### Key Observations:
- **Released Year:**
  - Weak positive correlation with Duration (0.15): Newer movies tend to be slightly longer.
  - Weak positive correlation with Rating (0.06): The release year has minimal impact on ratings.
  - Moderate positive correlation with User Vote (0.39): Newer movies tend to receive more votes, possibly due to an increasing user base over time.
- **Duration:**
  - Weak positive correlation with Rating (0.26): Longer movies show a slight tendency to receive higher ratings.
  - Weak positive correlation with User Vote (0.16): Longer movies might attract slightly more votes.
- **Rating (Star out of 10):**
  - Moderate positive correlation with User Vote (0.59): Higher-rated movies tend to receive more votes, suggesting that popular and well-rated movies attract more viewers.
- The correlations indicate some trends, but they are generally weak, implying that other factors likely play significant roles in these relationships.

## Conclusion

In conclusion, the analysis of IMDb's top 250 movies reveals fascinating trends and insights. The distribution of IMDb ratings shows a concentration around 8.0 to 8.4, indicating the prevalence of highly acclaimed films within this range. The increase in movie entries since the 1990s, peaking in the early 2000s, reflects evolving trends in cinematic production and audience preferences over time. Average movie durations have stabilized between 120 to 160 minutes since the 1960s, highlighting a consistent trend in film length. The prominence of directors, actors, and actresses in multiple top 250 entries underscores their lasting impact on cinematic excellence. Lastly, correlations between factors like release year, duration, IMDb rating, and user votes provide nuanced insights into the dynamics influencing film success and audience reception. Together, these findings deepen our appreciation of the factors shaping IMDb's top-ranked movies and their enduring appeal.