# Author: Kausik Chattapadhyay
# DSC 510 Assignment 10.2
# Date 08/10/2022
# This program is designed to simulate a cash register where
# users can enter the price of each item purchased and the result
# will show the total purchase price and total items purchased

class CashRegister:
    """
    Simple CashRegister class to print the items and amounts added to the cart.
    Methods are like add items to the cart, get count and get total.
    """
    def __init__(self):  # Constructor
        self.item_count = 0
        self.total_price = 0.0

    def addItem(self, price):   # Add item count and price to the Cash register
        self.item_count += 1
        self.total_price += price

    def getTotal(self):         # Get the total price in the cart
        return self.total_price

    def getCount(self):         # Get the item count
        return self.item_count


def main():
    """
    Will show the total purchase price and total items purchased.
    :return:
    """
    print("Welcome to the simple cash register!!")
    print("*************************************")
    import locale
    my_register = CashRegister()  # Instantiate the cash register.
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    while True:
        choice = input("Enter a to add item in the cart, and q to quit: ")
        if choice == 'q' or choice == 'Q':
            break
        elif choice == 'a' or choice == 'A':
            try:
                price = float(input("Enter the price of the item: "))
            except ValueError as ex:
                print(ex)
            my_register.addItem(price)
        else:
            print("Invalid choice, please try again.")
    print(" " * 40)
    print(f"The total items in your cart is {my_register.getCount()}")
    print(f"The total price of your items in the cart is {locale.currency(my_register.getTotal())}")
    print("Thanks for using Cash Register! Have a great day!")


if __name__ == '__main__':
    main()
