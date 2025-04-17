# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: April 14, 2025
# Is a for loop program
# It calculates the power of two for each number starting from 0 to the user number


def main():
    # Get user num as a string
    user_number = input("Enter a whole number: ")
    try:

        # Validate the user number as an integer
        number = int(user_number)

        # Checks if the entered number is negative
        if number < 0:

            # If the number is negative, print a error message
            print("Please enter a positive number.")
            return

        # set counter to 0
        counter = 0

        # for loop, it starts at 0, incrementing by one each time and then stops until it reaches the number from the user
        # It adds one to counter so it doesn't stops a num before it gets to the user num
        for counter in range(number + 1):

            # Prints the counter to the power of 2 and calculates what would that be and displays it
            print(f"{counter}^2 = {counter**2}")

    except Exception:
        # Print an error message if the user does not enter a valid whole number
        print("Invalid input. Please enter a whole number.")

    # Final message independently of the user input
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
