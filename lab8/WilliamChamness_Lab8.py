print("-------exercise 1---------")
name = input("Enter first, middle, and last name (e.g. John William Smith): ").split(" ")
finitial = name[0][0].upper()
minitial = name[1][0].upper()
linitial = name[2][0].upper()
print(finitial + ". " + minitial + ". " + linitial + ". ")

print("-------exercise 3----------")
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"   
]

date = input("Enter date (mm/dd/yyyy): ").split("/")
month = months[int(date[0]) - 1]
day = str(int(date[1])) # remove leading 0s
year = str(int(date[2]))

print(month, day + ",", year)