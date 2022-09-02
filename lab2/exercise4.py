SALES_TAX = 0.07
sales = 0

sales += float(input("enter the cost of item: "))
sales += float(input("enter the cost of item: "))
sales += float(input("enter the cost of item: "))
sales += float(input("enter the cost of item: "))
sales += float(input("enter the cost of item: "))

tax = sales * SALES_TAX
total = sales + tax

print("\nsubtotal:", "${:.2f}".format(sales))
print("tax:", "${:.2f}".format(tax))
print("total:", "${:.2f}".format(total))