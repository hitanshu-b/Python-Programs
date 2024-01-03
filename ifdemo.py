age = int(input("Enter Age: "))
if age < 5:
    print("You are very small")
    print("You are in kindergarten")
elif age>=5 and age<10:
    print("You are still small")
    print("You are in primary school")
elif age<16:
    print("You are still young")
    print("You are in highschool")
elif age<18:
    print("You are going to be an adult")
    print("You are in college")
else:
    print("You are a grown up kid")
    print("Drive a vehicle")
