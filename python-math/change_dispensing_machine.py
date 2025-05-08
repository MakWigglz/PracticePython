total_amount_str = input("What is the total amount of your bill?")
cash_payment_str = input("Cash payment amount?")

total_amount = float(total_amount_str)
cash_payment = int(cash_payment_str)

change_due = cash_payment - total_amount
change_due_cents = round(change_due * 100)

dollars = change_due_cents // 100
remaining_cents = change_due_cents % 100

quarters = remaining_cents // 25
remaining_cents %= 25

dimes = remaining_cents // 10
remaining_cents %= 10

nickels = remaining_cents // 5
remaining_cents %= 5

pennies = remaining_cents

print(f"change due ${change_due:.2f}")
print()
print(f"   Dollars: {dollars}    Quarters: {quarters}    Dimes: {dimes}     Nickels: {nickels}     Pennies: {pennies}")
