import tweepy
import credentials
# Authenticate to Twitter
access_token, access_token_secret, API_key, API_secret_key = credentials.credentials()


auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")
