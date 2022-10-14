print("--------exercise 1---------")
day = input("enter a number from 1 to 7: ")

if day == "1":
    print("Monday")
elif day == "2":
    print("Tuesday")
elif day == "3":
    print("Wednesday")
elif day == "4":
    print("Thursday")
elif day == "5":
    print("Friday")
elif day == "6":
    print("Saturday")
elif day == "7":
    print("Sunday")
else:
    print("input not an integer or outside range from 1 to 7")


print("--------exercise 3---------")
age = int(input("enter person's age: "))

if age <= 1:
    print("person is an infant")
elif age < 13:
    print("person is a child")
elif age < 20:
    print("person is a teenager")
else:
    print("person is an adult")