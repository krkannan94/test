import tweepy 
from time import sleep
 
# personal information 
api_key = "Znxbo7JW3tts58vFitj6na8HV"
api_secret_key = "mD8mQxlhyvrcsSo5Ql0wNPnFz74y47cYhHc4xJlY1Z8yUFi4is"
access_token = "1283039072219533315-UEjF4tZWQSYgFdAeGeNEfihPSissQT"
access_token_secret = "gfMFlN5dlXSUD40C3ZFmdhoUHtB6qkKz69VNRO2VPvHLJ"

# authentication 
auth = tweepy.OAuthHandler(api_key, api_secret_key) 
auth.set_access_token(access_token, access_token_secret) 


# authentication of access token and secret 
api = tweepy.API(auth) 

for i in iter(int, 1):

	for tweet in tweepy.Cursor(api.user_timeline, screen_name='its_samyu', include_rts=False, include_replies=False).items(1): 
		try:
			print('\nTweet by: @' + tweet.user.screen_name) 

			if not tweet.retweeted:
						tweet.retweet() 
						print('Retweeted the tweet')
			if not tweet.favorited:
						tweet.favorite() 
						print('Favorited the tweet')
			sleep(60)

		except:
			print('Already retweeted and favorited please be patient till next tweet')
			sleep(300)
