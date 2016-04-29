# CS105 Final Group Project
# Molly Herman, Tien Ho, Dan Mandel
# April 27, 2016
# Get_Averages.py

import sqlite3

conn = sqlite3.connect('twitterData_train.sqlite')
outfile = open("averages.txt","w")

command_list = [
 	 # Select averages of A when A wins.
	'''SELECT AVG(A_followers) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(A_following) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(A_listed) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(A_mentions_received) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(A_retweets_received) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(A_mentions_sent) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(A_retweets_sent) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(A_posts) FROM twitterMeasures WHERE choice = "A"''',

	# Select averages of B when A wins.
	'''SELECT AVG(B_followers) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(B_following) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(B_listed) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(B_mentions_received) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(B_retweets_received) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(B_mentions_sent) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(B_retweets_sent) FROM twitterMeasures WHERE choice = "A"''',
	'''SELECT AVG(B_posts) FROM twitterMeasures WHERE choice = "A"''',
   
	# Select averages of A when B wins.
	'''SELECT AVG(A_followers) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(A_following) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(A_listed) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(A_mentions_received) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(A_retweets_received) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(A_mentions_sent) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(A_retweets_sent) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(A_posts) FROM twitterMeasures WHERE choice = "B"''',  

	# Select averages of B when B wins.
	'''SELECT AVG(B_followers) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(B_following) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(B_listed) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(B_mentions_received) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(B_retweets_received) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(B_mentions_sent) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(B_retweets_sent) FROM twitterMeasures WHERE choice = "B"''',
	'''SELECT AVG(B_posts) FROM twitterMeasures WHERE choice = "B"''' 
	]

c = conn.cursor()

for command in command_list:
   c.execute(command)
   for tuple in c:
       print(tuple[0],file=outfile)

outfile.close()
