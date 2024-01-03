print("Welcome to the tip calculator")
bill = float(input("What is the total Bill? $"))
tip = int(input("How much tip would you like to add? 10, 12 or 15 ?"))
people = int(input("How many people to split the bill ?"))

tip_as_percent = tip / 100
total_tip_amt = bill * tip_as_percent
total_bill = bill + total_tip_amt
bill_per_person = total_bill / people
final_amt = round(bill_per_person,2)
final_amt = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amt}:")