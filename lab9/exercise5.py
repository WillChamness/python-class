words = {}
f = open(input("enter file path: "), "r")
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "").split(" ")
f.close()

for line in lines:
    for word in line:
        if word.lower() not in words.keys():
            words[word.lower()] = 1
        else:
            words[word.lower()] += 1

for word in words.keys():
    print('"' + word + '"', "appears", words[word], "times" if words[word] > 1 else "time")
