import random

print("Hellow welcome to the world rock paper scissors championship!!")
print("let's start!!!")
User=input("Choose your weapon:\n1.Rock.\n2.Paper.\n3.Scissors. :").lower()
opt={"rock","paper","scissors"}
computer = random.choice(list(opt))
if User == computer :
    print("It's a draw!!\ntry again")

#User wins    
elif User=="rock" and computer=="scissors" :

    # Scissors
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    \nyou've win""")
    
elif User=="paper" and computer=="rock" :
    #rock
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    \nYou've win""")
    
elif User=="Scissors" and computer=="paper" :
  # Paper
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    \nYOu've win""")
    
#computer wins
elif User=="scissors" and computer=="rock" :
    
    print("""
      _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    \nyou've lost""") 
    
elif User=="rock" and computer=="paper" : 
    # Paper
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    \nYOu've lost""")
    
elif User=="paper" and computer=="scissors" :
  # Paper
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    \nYOu've lost""")

else :
    print("try again!")