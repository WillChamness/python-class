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