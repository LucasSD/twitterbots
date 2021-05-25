import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("insert", 
    "insert")
auth.set_access_token("1insert", 
    "insert")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")