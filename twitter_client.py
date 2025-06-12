import tweepy
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def get_tweets(query, count=100):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=query, count=count, lang='en')
    return [tweet.text for tweet in tweets]