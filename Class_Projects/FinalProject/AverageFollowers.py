import sqlite3

conn = sqlite3.connect('twitterData_train.sqlite')

c = conn.cursor()
c.execute('''SELECT AVG(A_followers) FROM twitterMeasures WHERE choice = "A"''')

for tuple in c:
    print(tuple[0])
