# This program reads a "|" delimited text file and prints out
# the name, year, and runtime.

infile = open('movie.txt', 'r')
outfile =  open('movie_processed.txt','w')


count = 0
for line in infile:
    if count == 0:
        print ("name year runtime", file=outfile)
    components = line.split("|")
    print (components[1],components[2],components[4],file=outfile)        
    count += 1

if count == 0:
    print ("Infile does not contain anything.")

    
infile.close()
outfile.close()
print ("Done.")
