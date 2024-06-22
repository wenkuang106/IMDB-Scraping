import pandas as pd

df = pd.read_csv('scrapedData\cleaned_v3.0.csv')

# Average duration of movies over the years using a line chart
def convert_duration(duration_str):
    if 'h' in duration_str and 'm' in duration_str:
        hours, minutes = duration_str.split('h')
        hours = int(hours.strip())
        minutes = int(minutes.strip().strip('m'))
        return hours * 60 + minutes
    elif 'h' in duration_str:
        hours = int(duration_str.strip().strip('h'))
        return hours * 60
    elif 'm' in duration_str:
        minutes = int(duration_str.strip().strip('m'))
        return minutes
    else:
        return None

# Apply the conversion function to the 'Duration' column
df['Duration'] = df['Duration'].apply(convert_duration)

df.loc[15]

df.info()

n = df.nunique(axis=0)
 
print("No.of.unique values in each column :\n",n)

#df.to_csv('scrapedData/cleanedTableau.csv', index=False)