magicNumber = 21

while True:
    user_choice = input("Do you want to play the game to guess the number? (Y/n)")
    if(user_choice == 'n'):
        break

    user_number = int(input("Enter the number you want to guess "))
    if(magicNumber == user_number):
        print("You guessed it right and magic number is {}".format(user_number))
    elif(abs(magicNumber-user_number) == 1):
        print("Your guessed number {} is off by just 1".format(user_number))
    else:
        print("Sorry, it's wrong")