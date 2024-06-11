import pandas as pd
import re
import numpy as np

title = pd.read_csv('scrapedData/title.csv')
yrr = pd.read_csv('scrapedData\yearRatingRrestrictedRating.csv')
director = pd.read_csv('scrapedData\directors.csv')
cast = pd.read_csv('scrapedData\cast.csv')
synopsis = pd.read_csv('scrapedData\synopsis.csv')
rating = pd.read_csv('scrapedData\rating.csv')

#title = pd.DataFrame(title)
title['title'] = title['title'].astype(str)
titleWithNumber = title[title['title'].apply(lambda x: str(x)[0].isdigit())]
titleClean = titleWithNumber['title'].apply(lambda x: re.sub(r'^[\d\.]+', '', x))

# Reset the index of both DataFrames to ensure they have a common index
titleClean.reset_index(drop=True, inplace=True)
yrr.reset_index(drop=True, inplace=True)

yrr.loc[197]

# Concatenate the two DataFrames
tyrr = pd.concat([titleClean, yrr], axis=1)

tyrr.loc[196]

rating[['Rating (Star out of 10)', 'User Vote']] = rating['rating (Start out of 10)'].str.split('\n', n=1, expand=True)
ratingSplit = rating
ratingSplit['User Vote'] = ratingSplit['User Vote'].str.translate(str.maketrans("", "", "()"))
ratingClean = ratingSplit[['Rating (Star out of 10)', 'User Vote']]

tyrr.reset_index(drop=True, inplace=True)
ratingClean.reset_index(drop=True, inplace=True)

tyrrr = pd.concat([tyrr, ratingClean], axis=1)

tyrrr.reset_index(drop=True, inplace=True)
director.reset_index(drop=True, inplace=True)

tyrrrd = pd.concat([tyrrr, director], axis=1)

tyrrrd['Co-Director'] = ''
tyrrrd['Co-Director '] = ''

for i in range(len(tyrrrd)):
    if i == 15:
        tyrrrd.loc[i, 'Co-Director'] = 'Lilly Wachowski'
    elif i == 24:
        tyrrrd.loc[i, 'Co-Director'] = 'Kátia Lund'
    elif i == 36:
        tyrrrd.loc[i, 'Co-Director'] = 'Kemp Powers'
        tyrrrd.loc[i, 'Co-Director '] = 'Justin K. Thompson'
    elif i == 37:
        tyrrrd.loc[i, 'Co-Director'] = 'Rob Minkoff'
    elif i == 47:
        tyrrrd.loc[i, 'Co-Director'] = 'Éric Toledano'
    elif i == 62:
        tyrrrd.loc[i, 'Co-Director'] = 'Joe Russo'
    elif i == 64:
        tyrrrd.loc[i, 'Co-Director'] = 'Peter Ramsey'
        tyrrrd.loc[i, 'Co-Director '] = 'Rodney Rothman'
    elif i == 72:
        tyrrrd.loc[i, 'Co-Director'] = 'Adrian Molina'
    elif i == 77:
        tyrrrd.loc[i, 'Co-Director'] = 'Joe Russo'
    elif i == 87:
        tyrrrd.loc[i, 'Co-Director'] = 'Gene Kelly'
    elif i == 111:
        tyrrrd.loc[i, 'Co-Director'] = 'Bob Peterson'
    elif i == 118:
        tyrrrd.loc[i, 'Co-Director'] = 'Amole Gupte'
    elif i == 147:
        tyrrrd.loc[i, 'Co-Director'] = 'Joel Coen'
    elif i == 153:
        tyrrrd.loc[i, 'Co-Director'] = 'Terry Jones'
    elif i == 155:
        tyrrrd.loc[i, 'Co-Director'] = 'Lee Unkrich'
    elif i == 162:
        tyrrrd.loc[i, 'Co-Director'] = 'George Cukor'
        tyrrrd.loc[i, 'Co-Director '] = 'Sam Wood'
    elif i == 166:
        tyrrrd.loc[i, 'Co-Director'] = 'Ronnie Del Carmen'
    elif i == 171:
        tyrrrd.loc[i, 'Co-Director'] = 'Carlos Martínez López'
    elif i == 172:
        tyrrrd.loc[i, 'Co-Director'] = 'Ethan Coen'
    elif i == 196:
        tyrrrd.loc[i, 'Co-Director'] = 'David Silverman'
        tyrrrd.loc[i, 'Co-Director '] = 'Lee Unkrich'
    elif i == 197:
        tyrrrd.loc[i, 'Co-Director'] = 'Buster Keaton'
    elif i == 200:
        tyrrrd.loc[i, 'Co-Director'] = 'Chris Sanders'
    elif i == 206:
        tyrrrd.loc[i, 'Co-Director'] = 'Jan Pinkava'
    elif i == 210:
        tyrrrd.loc[i, 'Co-Director'] = 'Ethan Coen'
    elif i == 228:
        tyrrrd.loc[i, 'Co-Director'] = 'King Vidor'
    elif i == 248:
        tyrrrd.loc[i, 'Co-Director'] = 'John Musker'

tyrrrd.loc[87]
tyrrrd.loc[196]

castClean = pd.DataFrame(cast.values.reshape(-1, 3), columns=["Starring", "Co-Starring", "Co-Starring "])

tyrrrd.reset_index(drop=True, inplace=True)
castClean.reset_index(drop=True, inplace=True)

tyrrrdc = pd.concat([tyrrrd, castClean], axis=1)

tyrrrdc.reset_index(drop=True, inplace=True)
synopsis.reset_index(drop=True, inplace=True)

finalv1 = pd.concat([tyrrrdc, synopsis], axis=1)

finalClean = finalv1.rename(columns={
    'title' : 'Movie Title',
    'rating' : 'Restrticted Rating',
    'year' : 'Released Year',
    'duration' : 'Duration',
    'director' : 'Director (1)',
    'Co-Director' : 'Director (2)',
    'Co-Director ' : 'Director (3)',
    'Starring' : 'Starring (1)',
    'Co-Starring' : 'Starring (2)',
    'Co-Starring ' : 'Starring (3)',
    'synopsis' : 'Synopsis'
})

#final.sample()
finalClean.info()
finalClean.loc[182]
finalClean.loc[183]
finalClean.loc[220]
finalClean.loc[182]
finalClean.loc[196]
#finalClean.to_csv('scrapedData/cleaned_v3.0.csv', index=False)