infile = open('train.csv', 'r')
outfile = open('train_processed.csv','w')


count = 0
for line in infile:
    if count == 0:
        count += 1
        
    elif count < 5:
        components = line.split(",")
        num = components[0]
        target = components[1]
        print ("Target is: {}, num: {}".format(target, count))
        print ("")
        count +=1
