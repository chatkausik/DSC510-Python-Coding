# Author: Kausik Chattapadhyay
# DSC 500 Assignment 6.1
# Date 07/13/2022
# This program is designed to accept user inputs and create a list of
# temperatures, then show the total temperatures entered, smallest and largest

def max_number(numbers):
    """
    Function to return max number from a list.
    :param numbers:
    :return: Max number
    """
    max_value = None

    for num in numbers:
        if max_value is None or num > max_value:
            max_value = num
    return max_value


def min_number(numbers):
    """
    Function to return min number from a list.
    :param numbers:
    :return: min number
    """
    min_value = None

    for num in numbers:
        if min_value is None or num < min_value:
            min_value = num
    return min_value


def input_check():
    """
    Function to check the input valid values and exit out for invalid input.
    :return: temperature list
    """
    temperatures = []

    while True:
        input_temp = input('Enter temperatures or enter done to quit: ')
        if input_temp == 'done':
            break

        try:
            temps = float(input_temp)
        except ValueError:
            print('Invalid input. Please enter valid temperature or done to quit.')
            quit()

        temperatures.append(temps)

    return temperatures


def main():
    """
    Main function to get the input temperature list and print the Max, Min value from the recorded data.
    :return:
    """
    print("Welcome to Max/Min Temperature Calculator!")
    # Calling input_check function to record the temperatures from user input in a list.
    temperatures = input_check()

    if temperatures:
        print(temperatures)
        print('Maximum temperature is', max_number(temperatures), chr(176), sep='' or None)
        print('Lowest temperature is', min_number(temperatures), chr(176), sep='' or None)
        print('The total number of temperatures entered is', len(temperatures))
    else:
        print('The total number of temperatures entered is', len(temperatures))


if __name__ == '__main__':
    main()
