import praw
import prawcore
import sys
def setup():
	try:
		subredditName = sys.argv[1].lower()
	except IndexError:
		print('Incorrect argument count, proper usage is: python3 main.py "subreddit"')
		exit(0)



	reddit = praw.Reddit(client_id='YgFnfjpWFbv66g', \
	                     client_secret='jzxvfyzNhrle4G-G2QtttDqzsWM', \
	                     user_agent='Subreddit Scraper', \
	                     username='redeyesbigsmile', \
	                     password='skrillex')

	subreddit = reddit.subreddit(subredditName)

	return reddit, subreddit
