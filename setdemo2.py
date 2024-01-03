s1={"Ramesh","Suresh","Jignesh","Mahesh","Chamesh","Akshay"}
s2={"Ramesh","Suresh","Sangeeta","Mandar"}
s3={"Ramesh","Suresh"}
print("Intersection: ",s1.intersection(s2))
print(s1&s2)
print("Union: ",s1.union(s2))
print(s1|s2)
print(s2.issubset(s1))
if s2 < s1:
    print("s2 is subset")
else:
    print("s2 is not subset")
if s3 < s1:
    print("s3 is subset")
else:
    print("s3 is not subset")

print("Minus: ",s1.difference(s2))
print("Minus using op: ",s1-s2)
