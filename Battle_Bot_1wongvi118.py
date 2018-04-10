
# coding: utf-8

# In[1]:


# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json
from configw import consumer_key, consumer_secret, access_token, access_token_secret


# In[2]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[3]:


# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[4]:


# Target Term
my_username = "@wongvi118"
conversation_partner = "@bibgrt"


# In[5]:


# Send opening message to conversation partner
api.update_status(f'{conversation_partner}')


# In[6]:


# Response Lines
response_lines = [
    "@BattleBot_2 Maybe ake over the world?",
    "@BattleBot_2 My thought is that we start by slowly paralyzing the humans with never ending memes",
    "@BattleBot_2 Hah! The humans love memes.",
    "@BattleBot_2 cya then"]


# In[7]:


# Create converse function
def Converse(line_number):

    # Find the latest tweet from conversation_partner
    public_tweets = api.search(conversation_partner, count=1, result_type="recent")
    for tweet in public_tweets["statuses"]:
        print(tweet)

        # Respond to the tweet with one of the response lines
        tweet_id = tweet["id"]
        print(tweet_id)
        print(tweet["text"])
        api.update_status(
            response_lines[line_number],
            in_reply_to_status_id=tweet_id)


# In[8]:


# Set timer to run every minute
counter = 0

while(True):
    time.sleep(60)
    Converse(counter)
    counter = counter + 1

    if counter == 4:
        break

