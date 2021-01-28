import praw
import prawcore
import sys


def setup():

	reddit = praw.Reddit(client_id='YgFnfjpWFbv66g', \
	                     client_secret='jzxvfyzNhrle4G-G2QtttDqzsWM', \
	                     user_agent='Subreddit Scraper', \
	                     username='redeyesbigsmile', \
	                     password='skrillex')

	wsb = reddit.subreddit('wallstreetbets')

	return reddit, wsb
