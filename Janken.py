import random

print("Hello! Welcome to the Rock, Paper, Scissors Championship!!")
print("Let's start!!!")
user = input("Choose your weapon:\n1. Rock\n2. Paper\n3. Scissors: ").lower()
opt = {"rock", "paper", "scissors"}
computer = random.choice(list(opt))

if user == computer:
    print("It's a draw!!\nTry again")

# User wins
elif user == "rock" and computer == "scissors":
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    \nYou've won""")

elif user == "paper" and computer == "rock":
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    \nYou've won""")

elif user == "scissors" and computer == "paper":
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    \nYou've won""")

# Computer wins
elif user == "scissors" and computer == "rock":
    print("""
      _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    \nYou've lost""")

elif user == "rock" and computer == "paper":
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    \nYou've lost""")

elif user == "paper" and computer == "scissors":
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    \nYou've lost""")

else:
    print("Invalid input! Please try again.")
