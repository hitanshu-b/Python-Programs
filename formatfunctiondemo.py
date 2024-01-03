i = int(input("Enter Age: "))
name = input("Enter Name: ")
print("Your Name: ",name, "Your Age: ",i)

#using format function
s1 = "Your Name: {0} Your Age: {1}".format(name,i)
print(s1)

#in operator
s2 = "There is a cat, where is your cat ?"
s3 = "cat"
if s3 in s2:
    print("found")
else:
    print("not found")
