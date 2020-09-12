import tweepy

consumer_key = "xxxxx"
consumer_secret = "xxxxx"
access_token = "xxxxx"
access_token_secret = "xxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
my_tweet = [tweet.text for tweet in tweepy.Cursor(api.user_timeline, id="@kaz_m2ve9x").items(30) if (list(tweet.text)[:2]!=['R', 'T']) & (list(tweet.text)[0]!='@')]
print(my_tweet)