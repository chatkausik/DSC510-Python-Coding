# Author: Kausik Chattapadhyay
# DSC 510 Assignment 5.1
# Date 07/08/2022
# The purpose of this program is to run calculations for
# addition, subtraction, multiplication, division and average


def calculateAverage():
    """
    Calculate the average of values entered
    :return:
    """
    total = 0
    avg_val = int(input("How many values would you like to average? "))
    for i in range(avg_val):
        val = int(input("Enter number {0}: ".format(i + 1)))
        total += val
    print("Total:", total)
    print("Average:", total / avg_val)


def performCalculation(operator):
    """
    # calculate total of values by operator +,-,*,/
    :param operator:
    :return:
    """

    result = 0  # accept values for calculation from user
    try:
        first_val = int(input('Enter 1st number: '))
        second_val = int(input('Enter 2nd number: '))

        if operator == "+":
            result = first_val + second_val
        elif operator == "-":
            result = first_val - second_val
        elif operator == "*":
            result = first_val * second_val
        elif operator == "/":
            result = first_val / second_val
        print('Your result is:', result)

    except ValueError:  # Prompt user to enter only numbers for calculations
        print('This is not a number. Please try again.')


def main():
    # Ask user to choose calculator operation or to exit program.
    print('Welcome to the Calculator!')
    while True:
        print('1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Average and Total\n0. Exit')
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                performCalculation("+")
            elif choice == 2:
                performCalculation("-")
            elif choice == 3:
                performCalculation("*")
            elif choice == 4:
                try:
                    performCalculation("/")
                except ZeroDivisionError:
                    print('Error: Invalid Argument. Please enter non-zero value.')

            elif choice == 5:
                calculateAverage()
            elif choice == 0:
                print("Exit.Thank you for using!!")
                break
            else:
                print('This is not a valid choice. Please choose again.')

        except ValueError:  # Prompt user to enter only numbers for calculations
            print('This is not a valid choice. Please choose again.')


if __name__ == '__main__':
    main()
