import requests
import os
import json
import tweepy
import time

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# Credentials (INSERT YOUR KEYS AND TOKENS IN THE STRINGS BELOW)
api_key = "3XXFKSwNdFRYmmINitPptFPV6"
api_secret = "mdBXEHci91aQwwbiLHQUTjKP3SiuYXGiKMIez21mSQINsU39gM"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAMbHngEAAAAAeuuZyha2eI5w9RgD2s2TPOTInKw%3DLLqNTu0W5esgSSXYOxvY25m8IEVshPoSHbKufWM9QWxIHc8BEM"
access_token = "1083753347423731712-W1Mh62AJO7Xfv1ugZQKwIWeYSVnaCR"
access_token_secret = "UfZFBhNMF0qWPXTzDFQx4Uy3BQFyt1mWFzGmSVHKRYJ2W"

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"
tweets = []
limit = 10

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])

df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])
print(df)
