import random as rd 

capitals = {}
f = open("python-class\lab9\capitals.txt", "r") 
lines = f.readlines()
for line in lines:
    pair = line.split(", ")
    pair[0] = pair[0].replace("\n", "")
    pair[1] = pair[1].replace("\n", "")
    capitals[pair[1]] = pair[0]

TOTAL_QUESTIONS = len(capitals)
correct = 0

while capitals:
    question = list(capitals.keys())[rd.randint(0, len(capitals) - 1)] # randomly quiz user
    ans = capitals[question]
    print(question)
    guess = input(">> ").lower()
    if guess == ans.lower():
        print("correct\n")
        correct += 1
    else:
        print("incorrect. answer is", ans, "\n")
    del capitals[question]

print("total correct:", correct)
print("total incorrect:", TOTAL_QUESTIONS - correct)
