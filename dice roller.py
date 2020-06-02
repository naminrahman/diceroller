import random
#the main function
def main():
    
    #to start the code, roll dice
    roll_dice = input("Do you want to roll the dice, yes or no?").lower()
    
    print(roll_dice)
    if roll_dice == "no" or roll_dice == "n":
        print("Dice won't be rolled")
    
    elif roll_dice == "yes" or roll_dice == "y":
        yessir = True
        while yessir == True:
            result = random.randint(1,6)
            print(f"The result is {result}")

            re_roll = input("Do you want to roll the dice again?").lower()

            if re_roll == "no" or re_roll == "n":
                print("Thanks for using the dice, see you next time!")
                yessir = False
            elif re_roll == "yes" or re_roll == "y":
                yessir = True
            else:
                print("Please enter yes, no, y, or n!")
                yessir = False
    
    else:
        print("Please enter yes or no")






if __name__ == '__main__': main()
