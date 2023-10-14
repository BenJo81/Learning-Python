#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? "))
people_split = float(input("How many people to split the bill? "))

each_pay = float((((percentage_tip / 100) * total_bill) + total_bill) / people_split)
each_pay = round(each_pay, 2)

print(f"Each person should pay: ${each_pay}")