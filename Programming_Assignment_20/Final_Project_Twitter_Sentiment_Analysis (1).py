#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud 


# In[7]:


load = pd.read_csv("/Users/Srivaishnavi/Downloads/Login.csv")
consumerKey = load["key"][0]
consumerSecret = load["key"][1]
accessToken = load["key"][2]
accessTokenSecret = load["key"][3]
#Authentication object

authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
#set the access token 
authenticate.set_access_token(accessToken, accessTokenSecret)
#Create the API Object
api = tweepy.API(authenticate, wait_on_rate_limit=True)


# In[15]:


posts = api.user_timeline(screen_name = "ElonMusk", count=100, tweet_mode='extended')

for tweet in posts[0:5]:
    print(tweet.full_text + '\n')

df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])




# In[17]:


def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #Remove @mentions
    text = re.sub(r'#', '', text) #removing the '#' symbol
    text = re.sub(r'RT[\s]+', '', text) #remove RT
    text = re.sub(r'https?:\/\/\s+', '', text) #rm hyperlink)
    
    return text

df['Tweets'] = df['Tweets'].apply(cleanTxt)
df


# In[18]:


def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)
df


# In[19]:


allwords = ''.join([twts for twts in df['Tweets']])
wordCloud = WordCloud(width = 500, height=300, random_state = 21, max_font_size =119).generate(allwords)
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()


# In[20]:


def getAnalysis (score):
    if score < 0:
        return ' Negative'
    elif score  == 0:
        return 'Neutral'
    else:
        return 'Positive'
    
df['Analysis'] = df['Polarity'].apply(getAnalysis)
df


# In[21]:


#Print all of the positive tweets
j=1
sortedDF = df.sort_values(by=['Polarity'])
for i in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][i] == 'Positive'):
        print(str(j)+ ')' + sortedDF['Tweets'][i])
        print()
        j=j+1

j=1
sortedDF = df.sort_values(by=['Polarity'])
for i in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][i] == 'Negative'):
        print(str(j)+ ')' + sortedDF['Tweets'][i])
        print()
        j=j+1


# In[22]:


plt.figure(figsize=(8,6))
for i in range(0, df.shape[0]):
    plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue' )
    plt.title('Sentiment Analysis')
    plt.xlabel('Polarity')
    plt.ylabel('Subjectivity')
    plt.show()


# In[26]:


#percentage of positive tweets 
ptweets = df[df.Analysis == 'Positive']
ptweets = ptweets ['Tweets']
   
round((ptweets.shape[0]/df.shape[0]) *100, 1)


# In[28]:


#poercentage of negative tweets 
ntweets = df[df.Analysis == 'Negative']
ntweets = ntweets ['Tweets']
    
round((ntweets.shape[0]/df.shape[0]) *100, 1)


# In[35]:


#value counts
    
df['Analysis'].value_counts()
    
    #plot and visualize 
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Count (%)')
df['Analysis'].value_counts().plot(kind='bar')
plt.show()


# In[ ]:




