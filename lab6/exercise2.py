f = open(input("enter file location: "), "r")

lines = f.readlines()
if len(lines) >= 5:
    result = lines[0:5]
else:
    result = lines[0:]

for i in range(len(result)): print(result[i].strip())
f.close()