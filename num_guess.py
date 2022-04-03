#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: March 30. 2022

# the program asks the user for a number
# between 0-9. then tell them if they are correct

import constants
from colorama import Fore


def main():
    # get user input
    num_guess = int(input("Guess a number between 0-9: "))
    print("")

    # check if number is correct or incorrect
    if num_guess == constants.MY_NUMBER:
        print(Fore.GREEN + "You guessed right")

    else:
        print(Fore.RED + "You guessed wrong my number is: {}"
              .format(constants.MY_NUMBER))


if __name__ == "__main__":
    main()
