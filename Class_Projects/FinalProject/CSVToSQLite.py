# CS105 Final Group Project
# Molly Herman, Tien Ho, Dan Mandel
# April 20, 2016
# reference: https://docs.python.org/2/library/sqlite3.html
#

import csv
import sqlite3

infile = open("train_processed.csv",'r')
conn = sqlite3.connect('twitterData_train.sqlite')

c = conn.cursor()
c.execute('''CREATE TABLE twitterMeasures
              (A_followers integer, A_following integer, A_listed integer,
               A_mentions_received real, A_retweets_received real, A_mentions_sent real,
               A_retweets_sent real, A_posts real,
               B_followers integer, B_following integer, B_listed integer,
               B_mentions_received real, B_retweets_received real, B_mentions_sent real,
               B_retweets_sent real, B_posts real, choice char(1))''')

dataset = csv.reader(infile, delimiter=',')



count = 0
for line in dataset:
    if count != 0:
        values = [int(line[0]),int(line[1]),int(line[2]),
                   float(line[3]),float(line[4]),float(line[5]),
                   float(line[6]),float(line[7]),
                   int(line[8]),int(line[9]),int(line[10]),
                   float(line[11]),float(line[12]),float(line[13]),
                   float(line[14]),float(line[15]),line[16]]
        c.execute('INSERT INTO twitterMeasures VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',values)

    count += 1


conn.commit()
conn.close()
infile.close()
