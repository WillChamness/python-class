print("---------exercise 1----------")
total = 0
for i in range(5):
    total += int(input(f"enter number of bugs collected on day {i+1}: "))

print("number of bugs collected:", total)

print("---------exercise 2----------")
budget = float(input("enter budget for the month: "))

expenses = 0
while True:
    user_input = input('enter expense (or "done" to stop): ')
    if user_input == "done":
        break
    else:
        expenses += float(user_input)

if budget >= expenses:
    print("under budget by ${:.2f}".format(budget - expenses))
else:
    print("over budget by ${:.2f}".format(expenses - budget))

