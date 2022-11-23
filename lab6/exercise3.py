f = open(input("enter file location: "), "r")
lines = f.readlines()
for i in range(0, len(lines)): print(f"{i+1}:\t{lines[i].strip()}")
f.close()