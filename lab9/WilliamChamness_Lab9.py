print("-----------exercise 5-----------")
words = {}
f = open(input("enter file path: "), "r")
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "").split(" ") # remove newline character for convinience and split each lines into a list of words
f.close()

for line in lines:
    for word in line:
        if word.lower() not in words.keys(): 
            words[word.lower()] = 1
        else:
            words[word.lower()] += 1

for word in words.keys():
    print('"' + word + '"', "appears", words[word], "times" if words[word] > 1 else "time") 

print("--------exercise 2---------")
import random as rd 

capitals = {}
f = open(input("enter location of capitals: "), "r") 
lines = f.readlines()
for line in lines:
    # split "capital, state" into [capital, state]
    pair = line.split(", ")
    pair[0] = pair[0].replace("\n", "") # remove new line character for convinience
    pair[1] = pair[1].replace("\n", "")
    capitals[pair[1]] = pair[0]

TOTAL_QUESTIONS = len(capitals)
correct = 0

while capitals: # while there are still questions
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
