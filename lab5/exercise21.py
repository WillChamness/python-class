import random as rd 

def display_choices(user, cpu):
    print("you choose", user)
    if cpu == 1:
        print("i choose rock")
    elif cpu == 2:
        print("i choose paper")
    else:
        print("i choose scissors")

def rock(cpu):
    if cpu == 1: return "tie"
    elif cpu == 2: return "you lose"
    else: return "you win"

def paper(cpu):
    if cpu == 1: return "you win"
    elif cpu == 2: return "tie"
    else: return "you lose"

def scissors(cpu):
    if cpu == 1: return "you lose"
    if cpu == 2: return "you win"
    else: return "tie"


def main():
    result = "tie"
    while result == "tie":
        cpu_choice = rd.randint(1, 3)

        user_input = ""
        while not (user_input == "rock" or user_input == "paper" or user_input == "scissors"):
            user_input = input("enter rock, paper or scissors: ").lower()

        display_choices(user_input, cpu_choice)

        if user_input == "rock":
            result = rock(cpu_choice)
        elif user_input == "paper":
            result = paper(cpu_choice)
        else:
            result = scissors(cpu_choice)
        
        print(result)

if __name__ == "__main__":
    main()