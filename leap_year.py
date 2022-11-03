#!/usr/bin/env python3

# Created by: :Lucas LeBlanc
# Created on: Nov 2022
# This program tells a user if their chosen year is/was a leap year


def main():
    # This function determines if the user's year is a leap year

    # Input
    year_a_s = input("Enter a year(AD): ")
    print("")

    # Process and Output
    try:
        year_a_i = int(year_a_s)
        if year_a_i % 4 == 0:
            if year_a_i % 100 == 0:
                if year_a_i % 400 == 0:
                    print("{0} is a leap year.".format(year_a_i))
                else:
                    print("{0} is a common year.".format(year_a_i))
            else:
                print("{0} is a leap year.".format(year_a_i))
        else:
            print("{0} is a common year.".format(year_a_i))

    except Exception:
        print("Invalid input.")

    print("\nDone")


if __name__ == "__main__":
    main()
