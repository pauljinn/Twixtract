from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
import os

import twitter_credentials

import sys

class TwitterClient:
	def __init__(self, twitter_user=None):
		self.auth = TwitterAuthenticator().twitter_authenticate()
		self.twitterClient = API(self.auth)
		self.twitter_user = twitter_user

	def get_user_timeline_tweets(self, num_tweets):
		tweets = []
		for tweet in Cursor(self.twitterClient.user_timeline, id=self.twitter_user).items(num_tweets):
			tweets.append(tweet)
		return tweets

class TwitterAuthenticator:
	def twitter_authenticate(self):
		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
		return auth

class TwitterListener(StreamListener):

	def __init__(self, fetched_tweets_filename, max_tweets):
		self.fetched_tweets_filename = fetched_tweets_filename
		self.counter = 0
		self.max_tweets = max_tweets
		try:
			os.remove(fetched_tweets_filename)
		except:
			pass

	def on_data(self, data):
		self.counter += 1
		if self.counter > self.max_tweets:
			return False
		try:
			print(data)
			with open(self.fetched_tweets_filename, "a") as fp:
				fp.write(data)
			return True
		except BaseException as e:
			print("Error: %s\n" % str(e))
			return False

	def on_error(self, status):
		if status == 420:
			return False
		print(status)

class TwitterStreamer:
	def __init__(self):
		self.twitterAuthenticator = TwitterAuthenticator()
		
	def stream_tweets(self, fetched_tweets_filename, hashtag_list, max_tweets):
		listener = TwitterListener(fetched_tweets_filename, max_tweets)
		auth = self.twitterAuthenticator.twitter_authenticate()

		myStream = Stream(auth, listener)
		myStream.filter(track = hashtag_list)

if __name__ == '__main__':
	
	tweets_filename = "new_tweets.json"
	hashtags = ['fifa', 'messi', 'ronaldo', 'fifawc', 'world cup']
	myTwitterStreamer = TwitterStreamer()
	myTwitterStreamer.stream_tweets(tweets_filename, hashtags, 5)
	
	#twitterClient = TwitterClient('evilhag')
	#print(twitterClient.get_user_timeline_tweets(1))
