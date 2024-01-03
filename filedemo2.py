#write a program to display all employees with given designation
#from file

with open("empdata.dat") as fh:
    for line in fh:
        lst=line.split(":")
        if lst[-1].rstrip("\n")=="Manager":
            print(line)
        
