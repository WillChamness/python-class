import random as rd

f = open(input("enter file to write to: "), "w")
total_lines = int(input("enter total random numbers: "))

for i in range(total_lines):
    f.write(str(rd.uniform(1, 500)) + "\n")
f.close()
print("done")
