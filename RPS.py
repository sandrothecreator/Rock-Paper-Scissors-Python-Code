import time
import random

your_score = 0
computer_score = 0

print("Score : - Player:", your_score, " - Computer: ", computer_score)
while your_score < 3 and computer_score < 3:
    your_ans = input("Choose: rock / paper / scissors ")
    if your_ans != "rock" and your_ans != "scissors" and your_ans != "paper":
        print("Error")
    else:
        print("Computer chooses")
        time.sleep(0.5)
        print(3)
        time.sleep(0.5)
        print(2)
        time.sleep(0.5)
        print(1)
        computer_ans = random.randint(1, 3)
        if computer_ans == 1:
            computer_ans = "rock"
        elif computer_ans == 2:
            computer_ans = "scissors"
        elif computer_ans == 3:
            computer_ans = "paper"
        print("Computer Chose ", computer_ans)
        if your_ans == computer_ans:
            print("Draw")
        elif your_ans == "scissors" and computer_ans == 'paper':
            print("You Won!")
            your_score += 1
        elif your_ans == "rock" and computer_ans == 'scissors':
            print("You Won!")
            your_score += 1
        else:
            print("Computer Won")
            computer_score += 1
print()
print("Last Score:  - Player:", your_score, "- Computer: ", computer_score)