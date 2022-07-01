# Author: Kausik Chattapadhyay
# DSC 510 Assignment 4.1
# 06/29/2022
# The purpose of this program is to calculate the total cost
# to purchase fiber optic cable and provide a discounted price

def calculate_cost(cable_length, cost_per_foot):
    """
    Function to calculate total cost with below parameters.
    :param cable_length:
    :param cost_per_foot:
    :return: total_cost
    """
    total_cost = cable_length * cost_per_foot
    return total_cost


def determine_cost_per_foot(cable_length):
    """
    Function to determine cost per cable foot with below parameter.
    :param cable_length:
    :return: cost_per_foot
    """
    if 100.00 < cable_length <= 250.00:
        cost_per_foot = 0.80
    elif 250.00 < cable_length <= 500.00:
        cost_per_foot = 0.70
    elif cable_length > 500.00:
        cost_per_foot = 0.50
    else:
        cost_per_foot = 0.87
    return cost_per_foot


def main():
    """
    User will key company name and cable length. Main function will call other functions to calculate total cost
    and print the total.
    :return:
    """
    print('Welcome to FB Optics Fiber Optic Cable Calculator!')
    # Requesting user to input their company name
    company_name = input('Please enter the name of your company: ')
    # Requesting user to input amount of optic cable measured in feet
    # while loop will continue until valid value is given
    while True:
        try:
            cable_length = float(input('Please enter amount of cable in feet: '))
        except ValueError as ex:
            print(ex)
            continue
        else:
            break

    # Cost per foot depending on the amount of feet ordered
    cost_per_ft = determine_cost_per_foot(cable_length)

    # Calculate total cost
    total_cost = calculate_cost(cable_length, cost_per_ft)

    print('Thank you ' + str(company_name) + ' for your order.')
    print(f"The quantity of fiber optic cable ordered is {'{:,.2f}'.format(cable_length)}")
    print(f"The total rate per foot is ${'{:,.2f}'.format(cost_per_ft)}")
    print(f"The total cost of your order comes to ${'{:,.2f}'.format(total_cost)}")


if __name__ == "__main__":
    # execute only if run as a script
    main()



