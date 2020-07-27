# importing the module 
import tweepy
from time import sleep
import random
from datetime import datetime
import emojis

# personal information 
api_key = "9Wsb5Hf9sKKARIdOeKLkpzDaa"
api_secret_key = "mtlQXzEX7ePdLPCmosKymXVMWhim4Z13DdbvM95QdZ3zKkspva"
access_token = "1283039072219533315-gum0LTkAdNzXyVrYa47VX9gVPYyWm5"
access_token_secret = "Ob04oPMk6eTtS6rwuDenTJChi9mhuhyktN48eUPI1sk8T"

# authentication 
auth = tweepy.OAuthHandler(api_key, api_secret_key) 
auth.set_access_token(access_token, access_token_secret) 


# authentication of access token and secret 
api = tweepy.API(auth) 

piclist=["t.co/DVIh9mPqtu",
"t.co/mkPzzaqXge",
"t.co/qlg9UxICTy",
"t.co/dDSkDiqj92",
"t.co/LeTY4rJRQP",
"t.co/zQsMxcPCeY",
"t.co/v1rQYUS5ci",
"t.co/QPzcpLeH7s",
"t.co/711aO1d44J",
"t.co/xxMZZiIaer",
"t.co/UPrtXKk459",
"t.co/7lDiJFRfnm",
"t.co/MoBnb3La5r",
"t.co/LafVFjnGcl",
"t.co/QAT9VkfaUN",
"t.co/0gWF0pbSXZ",
"t.co/tlJLpUaUR3",
"t.co/TXFAvnG7a1",
"t.co/Bix5vJkFh2",
"t.co/ceHoLkEUgR",
"t.co/ZFFWbu3hHu",
"t.co/muGNfyIg40",
"t.co/uWl2XAA6zF",
"t.co/pTXbJbljMA",
"t.co/y3YIUmLljV",
"t.co/TK1kGm1JeC",
"t.co/4sYLk7EWWD",
"t.co/jDPEbeeHvF",
"t.co/S1WphGKTTq",
"t.co/SkWoGKmm2c",
"t.co/zKbWPZ9Q3V",
"t.co/i7f1vSpG6E",
"t.co/hG5pgOjyPO",
"t.co/L8LfR8hx0j",
"t.co/DWsP0umNcJ",
"t.co/OHDrv49I2f",
"t.co/wedONDbuhc",
"t.co/zD30YuSaAy",
"t.co/zD30YuSaAy",
"t.co/r5fPr5aH37",
"t.co/k9VT6gNGTA",
"t.co/w9tGWUnb41",
"t.co/fTMUY5SRYf",
"t.co/s9LgbhgtYz",
"t.co/5DKddIRzDC",
"t.co/nPL4e1BOcO",
"t.co/9APCBbCcfp",
"t.co/EWpMIxv38E",
"t.co/fYceUdHCiK",
"t.co/G75INgGAlX",
"t.co/B0Dwh8uWMC",
"t.co/Ov5ogfevzg",
"t.co/CcYvjDcJeh",
"t.co/TxBwdWYAJA",
"t.co/Tl7SVbjf47",
"t.co/CgsrusE8qV",
"t.co/GEihsm9LqM",
"t.co/pPA0mJ4P4L",
"t.co/ikXBvpED9H"
]


# Change the hashtags by your choice

for tweet in tweepy.Cursor(api.search, q = ("#Valimai -filter:retweets"),lang="en").items(): 
	try: 
		print("\nTweet by: @" + tweet.user.screen_name) 

		tweet.retweet() 
		print("Retweeted the tweet") 

		# Favorite the tweet  
		tweet.favorite() 
		print("Favorited the tweet") 
		
		# Twitter bot sleep time settings in seconds. Use large delays so that you account will not banned
		sleep(90) # 90 seconds = 1.5 minutes


		# Posting of tweets 
		for i in range(len(piclist)):
			try:
				#insert more hashtags if you want to here
				v = emojis.encode(":smile:" ":heart_eyes:" ":heart:" ":boom:" ":collision:" ":fire:" ":yellow_heart:" ":blue_heart:" ":purple_heart:" ":cupid:" ":kissing_heart:" ":relieved:" ":sunglasses:" ":innocent:" ":pray:" ":muscle:" ":clap:" ":bow:" ":no_entry_sign:")
				emoji = random.choice(v)
				namelist = ["Thala da","Thala Ajith daaa","The name is Thala AjithKumar","Thala Ajith","Thala da vera evanda","ultimate star ajithkumar","Aasai nayagan Thala","தல","தல அஜித்","தல அஜித்குமார்","தல டா வேற எவன் டா","வலிமை","ஆசை நாயகன்"]
				name = random.choice(namelist)
				hash = ["#Thala","#Ajith","#ThalaAjith","#AjithKumar"]
				hashlist = random.choice(hash)
				api.update_status(status =name+" "+ emoji+ emoji+ emoji+" "+ hashlist+" "+" #Valimai"+" "+ piclist[i])
				sleep(60)
				print("successfully tweeted")

			except: 
				pass

	except KeyboardInterrupt:
		exit()
