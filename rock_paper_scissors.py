import random
R_choices = ["rock", "paper","scissor"]

# loop starts here
while True :
    a = input("Enter rock, paper, scissor (or 'quit' to exit):").lower()



    if a == "quit" :
        print("good bye !")
        break #to exit the loop
    # game logic starts here
    computer_choice = random.choice(R_choices)
    if(a == computer_choice):
        print("It's a tie!")
    elif(a== "rock" and computer_choice == "scissor") :
        print("you won !")
    elif(a== "scissor" and computer_choice == "rock") :
        print("computer won !")
    elif(a== "paper" and computer_choice == "rock"):
        print("you won !")
    elif(a == "rock" and computer_choice == "paper"):
        print("computer won !")
    elif(a== "scissor" and computer_choice == "paper"):
        print("you won !")
    elif(a== "paper" and computer_choice== "scissor"):
        print("computer won !")
    print("Computer chose:", computer_choice)


    


