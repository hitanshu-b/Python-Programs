fh=open("empdata.dat","r")
fhcopy=open("empcopy.dat","w")
cnt=1
for line in fh:
    print(line)
    lst=s.split(":")
    print(lst[1])
    fhcopy.write(str(cnt)+":"+line)
    cnt+=1
fh.close()
fhcopy.close()
