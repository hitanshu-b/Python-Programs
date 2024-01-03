s1 = "real madrid is the greatest club of all time, this time is the time to win time"
##print("occurences: ", s1.count("time"))
##print("finding postions: ", s1.find("time"))
##print("finding postions: ", s1.find("time",9))
##print("finding postions: ", s1.find("time",17))
##print("finding postions: ", s1.find("time",42))
##

#write a program to find all occurances of cat

pos = s1.find("time")
count = 0
while pos!=-1:
    count = count+1
    print("count: ",count,"position: ",pos)
    pos = s1.find("time",pos+1)
if count == 0:
    print("not found")
