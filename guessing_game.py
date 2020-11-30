#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program checks to see if the number guessed is the magic number


import constants


def main():
    # this program checks to see if the number guessed is the magic number

    # input
    guessed_number = int(input("Enter a number(between 0-9): "))
    print("")

    # process
    if guessed_number == constants.MAGIC_NUMBER:
        # output
        print("Congratulations! You guessed the right number!")


if __name__ == "__main__":
    main()
