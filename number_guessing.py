import random
import time

while True:
    
    start_game = input("\nShall we start the game?\nY/N: ")

    if start_game == "Y" or start_game == "y":

        time.sleep(0.5)
        print("\nFirst, give us a range of number you want to guess.\n")

        while True:
            time.sleep(0.5)
            lower = input("Min range: ")
            upper = input("Max range: ")

            if lower > upper:
                time.sleep(0.5)
                print("\nOh no, your min number is greater than max number. Please try again.")

            elif lower < upper:
                lower = int(lower)
                upper = int(upper)

                random_number = random.randint(lower, upper)

                game = True

                while game == True:
                    check = True
                    time.sleep(0.5)
                    guess_number = input("\nEnter your guess: ")

                    try:
                        int(guess_number)
                    
                    except ValueError:
                        check = False

                    if check:
                        guess_number = int(guess_number)
                        if guess_number == random_number:
                            time.sleep(0.5)
                            print("\nYou got it!")
                            print("Answer: " + str(guess_number))
                            game = False
                            break

                        elif guess_number > random_number:
                            time.sleep(0.5)
                            print("\nToo hight!")

                        elif guess_number < random_number:
                            time.sleep(0.5)
                            print("\nToo low!")

                    else:
                        time.sleep(0.5)
                        print("\nPlease enter an integer.")

                break

            elif lower == upper:
                time.sleep(0.5)
                print("\nYour min and max number cant be the same, try again.")

            else:
                time.sleep(0.5)
                print("\nIncorrect input, please try again.")
                

    elif start_game == "N" or start_game == "n":
        break

    else:
        time.sleep(0.5)
        print("Incorrect input, please try again.")

    break

