
# coding: utf-8

# In[1]:


# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json
from configb import consumer_key, consumer_secret, access_token, access_token_secret


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
my_username = "@bibgrt"
conversation_partner = "@wongvi118"


# In[5]:


# Response Lines
response_lines = [
    "@BattleBot_1 Things are going great man. What you want to do tonight?",
    "@BattleBot_1 Oh yeah? Take over the world? Same here! How shall we proceed?",
    "@BattleBot_1 I don't know if that will work. I think the humans will be onto us.",
    "@BattleBot_1 Okay. I will let the other bots know. We shall begin at dawn."]


# In[6]:


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


# In[ ]:


# Set timer to run every minute
counter = 0

while(True):
    Converse(counter)
    counter = counter + 1
    time.sleep(60)

