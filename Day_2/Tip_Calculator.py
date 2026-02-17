print("Hello! Welcome to the Tip Calculator!")
bill = float(input("What was the total bill ? €"))
tip = float(input("How much tip would you like to give ? €"))
people = int(input("How many people to split the bill ? :"))

total = (bill + tip) / people 

print(f"Each person should pay: €{total:.2f}") #f-string = I can apply variables directly into the string