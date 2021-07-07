import json #Google play uses json library or list of json based functions
import pandas as pd 
from tqdm import tqdm

import seaborn as sns
import matplotlib.pyplot as plt #porting performed in this code
 
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from google_play_scraper import Sort, reviews #Reviews to be taken in a sorted order
from google_play_scraper import app

%matplotlib inline
%config InlineBackend.figure_format='retina'

sns.set(style='whitegrid', palette='muted', font_scale=1.2) # for scaling the font

app_package= ['org.edx.mobile']

len(app_package)

app_info = []

for ap in tqdm(app_package):  #Iteration of the app done with specifications as stated and information added at the end or appended
    info = app(ap, lang='en' , country='us')
    del info['comments']
    app_info.append(info)
    

app_info_df = pd.DataFrame(app_info) # App Information converted into Pandas Dataframe
app_info_df.head()
app_info_df.head(n=0)

app_info_df.to_csv('EDX Reviews.csv', index=None, header=True) # App Information stored as a csv file

app_reviews = []

print_json(app_info[0])

for ap in tqdm(app_package): # Code to download the reviews with specifications as mentioned
  for score in list(range(1, 6)):
    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
      rvs, _ = reviews(
        ap,
        lang='en',
        country='us',
        sort=sort_order,
        count= 200 if score == 3 else 100,
        filter_score_with=score
      )
      for r in rvs:
        r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
        r['appId'] = ap
      app_reviews.extend(rvs)
      
print_json(app_reviews) # Displays App Reviews with details such as Score given, Username, Date of reply, User Image, etc. 
                        # To run this line, first execute the previous codes mainly including the code to download the reviews, then run this code and display the app reviews.






  


