print("Rock-paper-scissors Game!")
print("Score is (you)-(computer)")
import random
import sys
wins = 0
lose = 0
choice = " "
def game():
    global choice
    choice = " "
    pick = 0
    pick = random.randint(1,3)
    if pick == 1:
        choice = "paper"
    if pick == 2:
        choice = "scissors"
    if pick == 3:
        choice = "rock"
def win(x):
    global wins
    global lose
    global choose
    if x == "1":
        if choice == "scissors":
            print(f"The computer picked {choice}")
            print("******You Won******!")
            wins = wins + 1
        elif choice == "paper":
            print(f"The computer picked {choice}")
            print("************You Lost************!")
            lose = lose + 1
        elif choice == "rock":
            print(f"The computer picked {choice}")
            print("************Tie************!")
            lose = lose + 1
            wins = wins + 1
    elif x == "2":
        if choice == "scissors":
            print(f"The computer picked {choice}")
            print("******You Lost******!")
            lose = lose + 1
        elif choice == "rock":
            print(f"The computer picked {choice}")
            print("******You Won******!")
            wins = wins + 1
        elif choice == "paper":
            print(f"The computer picked {choice}")
            print("************Tie************!")
            lose = lose + 1
            wins = wins + 1
    elif x == "3":
        if choice == "rock":
            print(f"The computer picked {choice}")
            print("******You Lost******!")
            lose = lose + 1
        elif choice == "paper":
            print(f"The computer picked {choice}")
            print("******You Won******!")
            wins = wins + 1
        elif choice == "scissors":
            print(f"The computer picked {choice}")
            print("************Tie************!")
            lose = lose + 1
            wins = wins + 1
def round():
    global choose
    print("Enter 1 for rock!\nEnter 2 for paper\nEnter 3 for scissors")
    while True:
        choose = input("Enter your choice here: ")
        if choose in ["1","2","3"]:
            game()
            win(choose)
            break
        elif choose not in ["1","2","3"]:
            print("Invalid choice!")
while True:
    try:
        rounds = int(input("How many rounds?: "))
        break
    except ValueError:
        print("Enter a number!")
while True:
    for _ in range(rounds):
        round()
        print(f"The score is {wins}-{lose}")
    if wins > lose:
        score = "You Won!"
    if lose > wins:
        score = "You Lost!"
    if lose == wins:
        score = "It was a tie"
    print(score)
    while True:
        again = input(f"Play again {rounds} rounds? (y/n): ")
        if again == "y":
            break
        elif again not in ["y","n"]:
            print("Enter either y or n!")
        elif again == "n":
            print("ggz")
            sys.exit()