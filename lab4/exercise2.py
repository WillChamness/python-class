budget = float(input("enter budget for the month: "))

total = 0
while True:
    user_input = input('enter expense (or "done" to stop): ')
    if user_input == "done":
        break
    else:
        total += float(user_input)

if budget - total >= 0:
    print("under budget by ${:.2f}".format(budget - total))
else:
    print("over budget by ${:.2f}".format(total - budget))

