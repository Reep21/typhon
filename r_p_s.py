#Basic rock, paper scissors game
import random
import time

def user_option():
    global user_input
    user_input = input("Choose number:\n1. Rock\n2. Paper\n3. Scissors\n:")

    if user_input == "1":
        user_input = "Rock"
        print("You chose",user_input,"\n")
        user_input = "Rock"
    elif user_input == "2":
        user_input = "Paper"
        print("You chose",user_input,"\n")
    elif user_input == "3":
        user_input = "Scissors"
        print("You chose",user_input,"\n")
    elif  user_input != "1" or user_inpput != "2" or user_inpput != "3":
        print("Invalid option! Please select either 1,2 or 3.")
        all_functions()
    else:
        print("Unexpected error!")

    return user_input

def bot_option():
    global bot_choice_final
    bot_choice = ["Rock", "Paper", "Scissors"]
    bot_selection = random.choices(bot_choice)
    bot_choice_final = ", ".join(bot_selection)

    print ("The bot selected",bot_choice_final,"\n")

    return bot_choice_final
 
def result():
    if user_input == bot_choice_final:
        print("It's a tie! You both selected",user_input)
    elif  user_input == "Rock" and bot_choice_final == "Scissors":
        print("You win! The bot chose",bot_choice_final,"and",user_input,"beats",bot_choice_final)
    elif  user_input == "Rock" and bot_choice_final == "Paper":
        print("You lose! The bot chose",bot_choice_final)
    elif  user_input == "Paper" and bot_choice_final == "Rock":
        print("You win! The bot chose",bot_choice_final,"and",user_input,"beats",bot_choice_final)
    elif  user_input == "Paper" and bot_choice_final == "Scissors":
        print("You lose! The bot chose",bot_choice_final,"and",bot_choice_final,"beats",user_input)
    elif  user_input == "Scissors" and bot_choice_final == "Paper":
       print("You win! The bot chose",bot_choice_final,"and",user_input,"beats",bot_choice_final)
    elif  user_input == "Scissors" and bot_choice_final == "Rock":
       print("You lose! The bot chose",bot_choice_final,"and",bot_choice_final,"beats",user_input)

def try_again():
    option = input("\nTry again? (y/n)\n:")

    if option == "y":
        all_functions()
    elif option == "n":
        print("Exiting game, thanks for playing!")
        exit(0)
    elif option != "y" or option != "n":
        print("Invalid option! Please select either y or n")
        try_again()
    else:
        print("Unexpected error!")

      
#call functions
def all_functions():
    user_option()
    bot_option()
    result()
    time.sleep(2)
    try_again()

all_functions()