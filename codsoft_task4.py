import random
list=["rock","paper","scissor"]
human_score=0
computer_score=0
while(True):
        computer_choice=list[random.randint(0,2)]
        print(" 1.Rock\n 2.Paper\n 3.Scissor\n 4.Exit")
        choice=int(input("Enter your choice(1,2,3,4)"))
        if(choice==1):
                human_choice="rock"
        elif(choice==2):
                human_choice="paper"
        elif(choice==3):
                human_choice="scissor"
        elif(choice==4):
                break
        else:
            print("Invalid Choice")
        print(f"User's choice:{human_choice},Computer Choice:{computer_choice}")
        if(computer_choice=="rock" and human_choice=="paper"):
               print("YOU WON!!!")
               human_score=human_score+1
        elif(computer_choice=="rock" and human_choice=="scissor"):
               print("COMPUTER WON!!!")
               computer_score=computer_score+1
        elif(computer_choice=="paper" and human_choice=="scissor"):
               print("YOU WON!!!")
               human_score=human_score+1
        elif(computer_choice=="paper" and human_choice=="rock"):
               print("COMPUTER WON!!!")
               computer_score=computer_score+1
        elif(computer_choice=="scissor" and human_choice=="rock"):
               print("YOU WON!!!")
               human_score=human_score+1
        elif(computer_choice=="scissor" and human_choice=="paper"):
               print("COMPUTER WON!!!")
               computer_score=computer_score+1
        else:
               print("It is a draw")
print(f"Your score is {human_score}")
print(f"Computer score is {computer_score}")
