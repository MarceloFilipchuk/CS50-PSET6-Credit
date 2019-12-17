## A function designed to return the type of credit card according to the number inputed

def main():
    # Prompts the user for a credit card number
    try:
        number = int(input("Number: "))
        while number <= 0:
            number = int(input("Number: "))
    except ValueError as err1:
        print(err1)
        print("Enter only numbers")
        return main()

    # Checks whether that number corresponds to a certain type of credit card or if its invalid

    # Checks if the number corresponds to a VISA
    if (number / 1000000000000000) >= 4 and (number / 1000000000000000) < 5:
        print("VISA")

    # Checks if the number corresponds to an AMERICAN EXPRESS
    elif (number / 100000000000000) >= 3 and (number / 100000000000000) < 4:
        print("AMEX")

    # Checks if the number corresponds to a MASTERCARD
    elif (number / 1000000000000000) >= 5 and (number / 1000000000000000) < 6:
        print("MASTERCARD")

    else:
        print("INVALID")
    return


# Calls the main() function
if __name__ == "__main__":
    main()