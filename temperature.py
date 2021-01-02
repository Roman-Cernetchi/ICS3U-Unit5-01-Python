#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program displays fahrenheit and celsius

import math


def fahrenheit():
    # calculates celcius to fahrenheit

    try:
        # input
        celsius_string = input("Enter the degrees in celsius: ")
        print("")

        celsius = int(celsius_string)

        fahrenheit = (9/5) * celsius + 32
        formatted_float = "{:.1f}".format(fahrenheit)

        # output
        print("{0}°c is {1}°f".format(celsius, formatted_float))

        if celsius < -273.15:
            print("")
            print("This temperature is impossible.")

    except Exception:
        print("This was not a number")


def main():
    # calls function
    fahrenheit()


if __name__ == "__main__":
    main()
