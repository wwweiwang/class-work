#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# load movie reviews dataset
# imdb and rtid need to be loaded as string to void lstrip of 0
df = pd.read_csv(
    '../dataset7/reviews.csv', 
    dtype={
        'imdb': 'object',
        'rtid': 'object',
    },
)


# In[3]:


# question1:
# what are the top-10 movies with most reviews?

# select rows whose imdb column is not null, groupby imdb and count size
movie_review_counts = df.loc[df['imdb'].notnull()]     .groupby('imdb')     .size().to_frame('review_counts')     .sort_values('review_counts', ascending=False)
print('Q1: Top10 most reviewed movies:')
print(movie_review_counts.head(10))
print()


# In[4]:


# quesiton2:
# are there any imdb ids map to multiple rtids?

imdb_to_rtids_count = df.loc[df['imdb'].notnull()]     .groupby('imdb')     .rtid.nunique()     .to_frame('counts')
imdb_with_multiple_rtids = imdb_to_rtids_count.loc[imdb_to_rtids_count['counts'] > 1]
print('Q2: IMDB ids with multiple rtids:')
print(imdb_with_multiple_rtids)
print()


# In[5]:


# question3: 
# who are most active 10 crtics for those less popular movies (bottom 500 movies)
tail_movies = movie_review_counts.tail(500)
tail_critics = df.filter(items=['imdb','critic'])     .join(how='inner', other=tail_movies, on='imdb')     .groupby('critic')     .size().to_frame('review_counts')     .sort_values('review_counts', ascending=False)
print('Q3: Top10 most active tail movie crtics (bottom 500 movies)')
print(tail_critics.head(10))
print()


# In[ ]:




