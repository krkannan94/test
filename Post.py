import tweepy 
from time import sleep
 
# personal information 
api_key = "Znxbo7JW3ts58vFitj6na8HV"
api_secret_key = "mD8mQxlhvrcsSo5Ql0wNPnFz74y47cYhHc4xJlY1Z8yUFi4is"
access_token = "128303907221933315-UEjF4tZWQSYgFdAeGeNEfihPSissQT"
access_token_secret = "gfMFlN5dXSUD40C3ZFmdhoUHtB6qkKz69VNRO2VPvHLJ"

# authentication 
auth = tweepy.OAuthHandler(api_key, api_secret_key) 
auth.set_access_token(access_token, access_token_secret) 


# authentication of access token and secret 
api = tweepy.API(auth) 

for i in range(10):

	for tweet in tweepy.Cursor(api.search, q='its  -filter:retweets -filter:replies', result_type='recent', lang='en').items(1): 
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
			sleep(60)
