print("-------exercise 1----------")
sales = [float(input(f"Enter sales on day {i+1}: ")) for i in range(7)]    

total = 0
for sale in sales:
    total += sale

print("total sales: ${:.2f}".format(total))