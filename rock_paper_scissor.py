import random
import time

def choice_generator (choice):
  
    choice = str(choice)

    if choice == "1":
        return "Rock"
    elif choice == "2":
        return "Paper"
    elif choice == "3":
        return "Scissor"

def compete (user, bot):

    if user == bot:
        return "Draw!"
    
    elif user == "Rock" and bot == "Paper":
        return "Bot wins!"

    elif user == "Rock" and bot == "Scissor":
        return "User wins!"
    
    elif user == "Scissor" and bot == "Paper":
        return "User wins!"

    elif user == "Scissor" and bot == "Rock":
        return "Bot wins!"
    
    elif user == "Paper" and bot == "Rock":
        return "User wins!"

    elif user == "Paper" and bot == "Scissor":
        return "Bot wins!"

while True:

    play = input("\nPlay or nay?\nY/N: ")

    if play == "Y" or "y":

        gamemode = True

        while gamemode:

            time.sleep(0.5)
            print("\nPick your choice - (1) Rock / (2) Paper / (3) Scissor")
        
            time.sleep(0.5)
            user_input = input("\nEnter the number: ")
            user = choice_generator(user_input)
        
            bot_input = random.randint(1, 3)
            bot = choice_generator(bot_input)

            result = compete(user, bot)

            time.sleep(0.5)
            print("\nUser: " + str(user))
            print("Bot: " + str(bot))
            print("Result: " + str(result))

            time.sleep(0.5)
            print("\nTo stop playing, type 'quit'.")

            if user_input == "Quit" or user_input == "quit":
                time.sleep(0.5)
                print("\nThanks for playing!")
                break

    else:
        time.sleep(0.5)
        print("\nSee ya!")
        break

    break


