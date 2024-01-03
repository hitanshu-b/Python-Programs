lst=[]
s=""
while s!="end":
    s=input("Enter word to add: ")
    flag = False
    for i,w in enumerate(lst):
        if w[1]==s[1]:
            while i<(len(lst)):
                if lst[i][1]==s[1]:
                    i=i+1
                else:
                    break
            lst.insert(i,s)
            print(lst)
            flag = True
            break
        if flag==False:
            lst.append(s)
        print(lst)
