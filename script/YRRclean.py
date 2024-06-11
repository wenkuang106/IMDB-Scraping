import pandas as pd
import itertools


# Load your CSV file
df = pd.read_csv('scrapedData\test.csv', header=0)

# Initialize empty lists to store data for each column
years = []
durations = []
ratings = []

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Check if the 'year' column contains a numeric value
    if str(row['year']).isdigit():
        # If it's a year, append it to the 'years' list
        years.append(row['year'])
        # Check if the next row contains the duration
        if index + 1 < len(df) and not str(df.loc[index + 1, 'year']).isdigit():
            # If it does, append it to the 'durations' list
            durations.append(df.loc[index + 1, 'year'])
            # Check if the next row contains the rating
            if index + 2 < len(df) and not str(df.loc[index + 2, 'year']).isdigit():
                # If it does, append it to the 'ratings' list
                ratings.append(df.loc[index + 2, 'year'])
            else:
                # If there's no rating, append an empty string
                ratings.append('')
        else:
            # If there's no duration, append an empty string
            durations.append('')
            # If there's no rating, append an empty string
            ratings.append('')
        
# Create a new DataFrame from the lists
result_df = pd.DataFrame({'year': years, 'duration': durations, 'rating': ratings})

# Print the result
print(result_df)
result_df.loc[220]
result_df.info()
result_df.to_csv('yearRatingRrestrictedRating.csv',index=False)