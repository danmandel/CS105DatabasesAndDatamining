import csv

infile = open("train.csv",'r')
outfile = open("train_processed.csv",'w')

column_names = "A_follower_count,A_following_count,A_listed_count,A_mentions_received,A_retweets_received,A_mentions_sent,A_retweets_sent,A_posts,A_network_feature_1,A_network_feature_2,A_network_feature_3,B_follower_count,B_following_count,B_listed_count,B_mentions_received,B_retweets_received,B_mentions_sent,B_retweets_sent,B_posts,B_network_feature_1,B_network_feature_2,B_network_feature_3,Choice"

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
        result = ",".join(line)
        print (result, file=outfile)
    
    count += 1
    
infile.close()
outfile.close()
