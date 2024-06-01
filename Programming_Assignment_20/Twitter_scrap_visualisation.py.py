################Tweet Analysis Visualization################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tweepy import API
from tweepy import Cursor 
from tweepy import OAuthHandler
from tweepy import Stream
import twt_credentials

##########Twitter Client##########

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twt_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
    
    def get_twitter_client_api(self):
        return self.twitter_client
    
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets   
    
    def get_friend_list(self, num_friends):
        friend_list= []
        for friend in Cursor (self.twitter_client.friends).items(num_friends):
            friend_list.append(friend)
            
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor (self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
            

############Twitter Autheticator#############
class TwitterAuthenticator():
    
    def authenticate_twt_app(self):
        auth = OAuthHandler(twt_credentials.CONSUMER_KEY, twt_credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(twt_credentials.ACCESS_TOKEN, twt_credentials.ACCESS_TOKEN_SECRET)
        return auth 

#################Twitter Streamer####################
class TwtStreamer():
    #### Class that streams and processes the live tweets 
    
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    
    def streamtweets(self, fetched_tweets_filename, hash_tag_list):
        ##The function handles the twt authentication and connection to the streaming API 
        listener = TwtListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twt_app()
        stream = Stream(auth, listener)
        
        ##Filters the twitter streams to capture data by keywords
        stream.filter(track=hash_tag_list)
        
        
###########Twitter Stream Listener##################
        
class TwtListener(Stream):
    # a listener class that prints the recieved tweets to stdout 
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
     
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a', encoding="utf8") as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
    
    def on_error(self, status):
        if status == 420:
            #Returning False on_data method incase rate limit occurs
            return False
        print(status) 
        

##################Tweet Analysis#####################
class TweetAnalyzer():
    #Functionality for analyzing and categorizing content from tweets.
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        return df
    pass               

if __name__ == "__main__":
    
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()
    
    tweets = api.user_timeline(screen_name="clcoding", count=200)
    
    #print(dir(tweets[0]))
    #print(tweets[2].retweet_count)
    
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    #print(df.head(50))
    print(np.mean(df['len']))
    print(np.max(df['Likes']))
    
###############Time Series Visualisation##################
    time_likes = pd.Series(data=df['Likes'].values, index=df['date'])
    time_likes.plot(figsize=(16, 4), color='r', marker = 'o', mec = '#4CAF50')
    plt.title("clcoding engagement data")
    plt.xlabel("Date")
    plt.ylabel("Likes")
    plt.show()    
    
    
     