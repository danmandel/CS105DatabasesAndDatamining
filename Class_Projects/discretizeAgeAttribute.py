infile = open("dataset1.csv",'r')
outfile = open("dataset_processed.csv",'w')

current_order = "ID Name Age Party x1 x2 x3 x4 x5"
target_order = "ID Name Bin Party x1 x2 x3 x4 x5"

count = 0
for line in infile:
    if count == 0:
        print (target_order,file=outfile)

    components = line.split('\n')
    components = line.split(",")
    
    age = int(components[6])
    
    if age < 9:
        components[6] = "C"
    elif age < 15:
        components[6] = "W"
    elif age < 24:
        components[6] = "Y"
    elif age < 30:
        components[6] = "P"
    elif age < 40:
        components[6] = "T"
    elif age < 65:
        components[6] = "M"
    else:
        components[6] = "S"

    transformed = ",".join(components)
    print (transformed)
    count +=1

    
infile.close()
outfile.close()
