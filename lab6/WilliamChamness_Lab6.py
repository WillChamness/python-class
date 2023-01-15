print("--------exercise 2---------")
f = open(input("enter file location: "), "r")

lines = f.readlines()
if len(lines) >= 5:
    result = lines[0:5]
else:
    result = lines[0:]
print(lines)

for i in range(len(result)): print(result[i].strip())
f.close()

print("---------exercise 3---------")
f = open(input("enter file location: "), "r")
lines = f.readlines()
for i in range(0, len(lines)): 
    print(f"{i+1}:\t{lines[i].strip()}")
f.close()