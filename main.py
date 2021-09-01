import random
import time
import sys
import tweepy
from os import environ

consumer_key = environ['API_KEY']
consumer_secret_key = environ['API_SECRET_KEY']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

def get_quotes():
    with open('anders.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote

def tweet_quote():
    interval = 30 * 60 #30 minutes x 60 seconds
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    while True:
        print('Getting quote...')
        tweet = get_random_quote()
        api.update_status(tweet)
        print('And now we wait!!')
        time.sleep(interval)
    
if __name__ == "__main__":
    tweet_quote()
    
    


        
