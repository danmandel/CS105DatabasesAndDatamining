import sqlite3
import time 
import datetime
import random

conn = sqlite3.connect('test.sqlite')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS StuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
    
def data_entry():
    c.execute("INSERT INTO StuffToPlot VALUES(145, '2016-01-01', 'Python',5)")
    conn.commit()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO StuffToPlot(unix,datestamp,keyword,value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value)) # %s in SQL
    conn.commit()

def read_from_db():
    c.execute('SELECT keyword, unix FROM StuffToPlot')
    #c.execute('SELECT * FROM StuffToPlot WHERE time_stamp BETWEEN 9:00 AND 9:10')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row[0]) #only prints unix stamp


##create_table()
##data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

read_from_db()
c.close()

