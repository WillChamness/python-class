print("---------exercise 1-----------")
name = input("enter your name: ")
street_addr = input("enter your street address: ")
city = input("enter the city: ")
state = input("enter the state: ")
zip = input("enter the ZIP code: ")
phone = input("enter your telephone number: ")
major = input("enter your college major: ")

print(name, street_addr + ",", city + ",", state, zip, phone, major)


print("---------exercise 3-----------")
ft = float(input("enter square feet: "))
acres = ft / 43560
print(ft, "ft^2 =", acres, "acres")


print("---------exercise 4-----------")
SALES_TAX = 0.07
sales = 0

sales += float(input("enter the cost of item: "))
sales += float(input("enter the cost of item: "))
sales += float(input("enter the cost of item: "))
sales += float(input("enter the cost of item: "))
sales += float(input("enter the cost of item: "))

tax = sales * SALES_TAX
total = sales + tax

print("\nsubtotal: ${:.2f}".format(sales))
print("tax: ${:.2f}".format(tax))
print("total: ${:.2f}".format(total))