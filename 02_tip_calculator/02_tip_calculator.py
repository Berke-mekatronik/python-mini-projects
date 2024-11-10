#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator. ")

total = input("What was the total bill? ")
perc = input("What percentage tip would you like to give? 10, 12, or 15? ")
n_perc = 1 + (int(perc) / 100)

split = input("How many people to split the bill? ")
pay = (float(total)/int(split)) * float(n_perc)
round_pay = "{:.2f}".format(pay)

print(f"Each person should pay: {round_pay}")
