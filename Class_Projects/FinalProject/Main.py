#infile = open('train.csv', 'r')
infile = "train.csv"
outfile = open('train_processed.csv','w')

import csv

with open(infile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',') # Better because \n was messing things up I think.
    row_counter = 0
    for row in readCSV:
        nonblank_fields = 0
        if row_counter < 10: #eventually can remove this and indent everything under it 1 tab to the left.
            
            ID = row[0]
            Target = row[1]
            Missing_Fields = []
            
            for field in row:
                print (row.index(field))
                if (field != ''):
                    nonblank_fields += 1

            print ("There are {} filled in fields for ID {} \n".format(nonblank_fields,ID))    
            row_counter +=1
        else:
            break
