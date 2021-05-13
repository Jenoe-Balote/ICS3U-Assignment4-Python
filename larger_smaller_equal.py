#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program determines which of two numbers are
#       larger, smaller or equal to each other.

import string


def main():
    # this function runs the "Larger, Smaller or Equal?" program"

    # input
    print("Which number is the greatest?")
    number_one = str(input("Enter your first number: "))
    number_two = str(input("Enter your second number: "))
    print("")

    # process and output
    try:
        number_one = int(number_one)
        number_two = int(number_two)
        if number_one > number_two:
            print("{} is larger.".format(number_one))
            print("{} is smaller.".format(number_two))
        elif number_one < number_two:
            print("{} is larger.".format(number_two))
            print("{} is smaller.".format(number_one))
        elif number_one == number_two:
            print("The two numbers are equal!")
    except Exception:
        print("{} is invalid data.".format(number_one and number_two))
    finally:
        print("")
        print("Thanks for participating!")


if __name__ == "__main__":
    main()
