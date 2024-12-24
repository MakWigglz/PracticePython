number = 24
steps = 0

for i in range(200):
    if number == 1:
        break
    elif number % 2 == 0:
        number = number / 2
        steps = steps + 1
    else:
        number = 3*number + 1
        steps = steps + 1
    
if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")