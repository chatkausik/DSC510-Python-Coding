# Author: Kausik Chattapadhyay
# DSC 510 Assignment 9.1
# Date 08/03/2022
# This program is to access Chuck Norris jokes from the web and
# display them for the user of the program.

import requests
from pprint import pprint

if __name__ == '__main__':

    print("""Welcome. Please choose your Chuck Norris joke of the day!  
    (0) End Program      (1) Animal      (2) Career 
    (3) Celebrity        (4) Dev         (5) Explicit  
    (6) Fashion          (7) Food        (8) History 
    (9) Money            (10) Movie      (11) Music
    (12) Political       (13) Religion   (14) Science 
    (15) Sport           (16) Travel\n""")

    cat_dict = {1: "animal", 2: "career", 3: "celebrity", 4: "dev",
                5: "explicit", 6: "fashion", 7: "food", 8: "history",
                9: "money", 10: "movie", 11: "music", 12: "political",
                13: "religion", 14: "science", 15: "sport", 16: "travel"}

    while True:
        choose = None
        try:
            choose = int(input("What category would you like? "))
        except ValueError as e:
            pass

        if choose in cat_dict.keys():
            try:
                choose = int(choose)
            except ValueError as ex:
                print(f'Category must be integer: {ex}')

            category = cat_dict[choose]

            try:
                req_joke = requests.get(f"https://api.chucknorris.io/jokes/random?={category}")
                req_joke.raise_for_status()
                data = req_joke.json()
                print("\n" + data["value"])
            except requests.exceptions.HTTPError as error:
                print(f'HTTP error occurred: {error}')
            except requests.ConnectionError as error:
                print(f'Connection error occurred: {error}')
            except Exception as err:
                print(f'Other error occurred: {err}')

        elif choose == 0:
            print("See you later!")
            break
        else:
            print("Invalid input. Please try again.")