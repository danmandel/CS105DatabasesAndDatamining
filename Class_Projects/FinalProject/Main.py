# This program moves the target to the furthest column using a,b = b,a
# It sets the last column to either A or B depending on whether it's 0 or 1
# It also removes certain unneeded columns.

import csv

infile = open("train.csv",'r')
outfile = open("train_processed.csv",'w')

column_names = "A_follower_count,A_following_count,A_listed_count,A_mentions_received,A_retweets_received,A_mentions_sent,A_retweets_sent,A_posts,B_follower_count,B_following_count,B_listed_count,B_mentions_received,B_retweets_received,B_mentions_sent,B_retweets_sent,B_posts,Choice"

count = 0
dataset = csv.reader(infile,delimiter=',')
for line in dataset:
    if count == 0:
        print (column_names,file=outfile)
    if count > 0:
        classification = int(line[-1])
        if classification == 1:
            line[-1] = "A"
        if classification == 0:
            line[-1] = "B"
        result = ",".join(line[0:8]+line[11:19]+line[22:])
        print (result, file=outfile)
    
    count += 1
    
infile.close()
outfile.close()
