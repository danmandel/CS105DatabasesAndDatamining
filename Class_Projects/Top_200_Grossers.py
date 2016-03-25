# Author: Dan Mandel
# This program finds movies from a given year that are among
# the top 200-grossing movies.

import sqlite3

filename = input("Enter the name of the database file: ")
db = sqlite3.connect(filename)
cursor = db.cursor()

targetyear = input("Enter the year: ")
command = '''
SELECT M.earnings_rank, M.name
FROM Movie M
WHERE M.earnings_rank <= 200
    AND M.year = ?
ORDER BY M.earnings_rank;
'''
cursor.execute(command, [targetyear])

resultsfile = input("Enter name of the results file: ")

count = 0
for i in cursor:
    if count == 0:
        outfile = open(resultsfile,'w') 
    
    print (i[0],',',i[1],file=outfile)
    count += 1

if count == 0:
    print ("There are no top-grossing movies from that year.")
else:
    outfile.close()

print ("Wrote {} lines of results to the file.".format(count))

db.commit()
db.close()
