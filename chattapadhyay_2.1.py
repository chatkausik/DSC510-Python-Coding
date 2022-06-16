# DSC 510 T301 SUMMER 2022
# Week 2
# Programming Assignment 2.1
# Author: Kausik Chattapadhyay
# 06/13/2022


# Take user inputs Name, Company Name, feet of fiber optic cable
user = input("Enter user name: ")  # Enter username
print(f"Hello {user}! Welcome..")
company_name = input("Please Enter the company name: ")  # Enter Company Name

# raise value error for non-numeric fiber length
# while loop will continue until valid value is given
while True:
    try:
        cable_length = float(input("Please enter the length (in Feet) of fiber optic cable to be installed: "))
    except ValueError as ex:
        print(ex)
        continue
    else:
        break

# Printing the receipt if user inputs are valid
if user.replace(" ", "").replace(".", "").isalpha() and len(str(user).strip()) > 0:
    if company_name.replace(" ", "").replace(".", "").isalpha() and len(str(company_name).strip()) > 0:
        if isinstance(cable_length, (float, int)):
            # Calculate total install cost
            install_cost = round((cable_length * 0.87), 2)
            install_cost_format = "{:,.2f}".format(install_cost)
            # Printing Receipt
            print("****** RECiEPT ************************")
            print("                                       ")
            print(f"Name                     : {user}")
            print(f"Company                  : {company_name}")
            print(f"Fiber optic cable length : {'{:,.2f}'.format(cable_length)} feet")
            print(f"Calculated cost          :${str(install_cost_format)}")
            print(f"Total cost               :${str(install_cost_format)}")
            print("                                       ")
            print("****** Thank you **********************")
        else:
            raise ValueError("Invalid cable length..")
    else:
        raise ValueError("Invalid company name...")
else:
    raise ValueError("Invalid user name..")
