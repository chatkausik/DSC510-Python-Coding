# Change#: 1
# Change(s) Made: Generate a text file from the output rather than printing to the screen
# Author: Kausik Chattapadhyay
# DSC 500 Assignment 8.1
# Date 07/28/2022
# Program to calculate the total words, and output the number of occurrences of each word in the file.
# Generate a text file from the output rather than printing to the screen.

import string
import os


def add_word(word, dictionary):
    """
    Function to add the words to dictionary.
    :param word:
    :param dictionary:
    :return:
    """
    if word in dictionary:  # check whether a word exists or not
        dictionary[word] = dictionary[word] + 1  # increase count if word exists
    else:
        dictionary[word] = 1  # append dictionary if word doesn't exist


def process_line(line, dictionary):
    """
    Function to process lines by removing the unnecessary punctuations, lowering the words
    and lastly split the lines into words.
    :param line:
    :param dictionary:
    :return:
    """
    line = line.translate(str.maketrans('', '', string.punctuation))  # Removed all the punctuations
    line = line.lower()  # Lower all the words.
    line = line.strip()  # Strip leading and trailing spaces
    words = line.split()  # splitting the line into words

    for word in words:
        add_word(word, dictionary)  # calling the add_word function


def process_file(dictionary, oname):
    """
    Write the details to output .txt file.
    :param dictionary:
    :return:
    """
    lst = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    with open(oname, 'w') as ofile:
        ofile.write("Welcome to the text to word frequency converter!! \n")
        ofile.write("                                                  \n")
        ofile.write(f"Length of the dictionary: {len(dictionary)} \n")
        ofile.write("                                                 \n")
        ofile.write(f"{'----' : <15}{'-----' : ^30} \n")
        ofile.write(f"{'Word' : <15}{'Count' : ^30} \n")
        ofile.write(f"{'----' : <15}{'-----' : ^30} \n")
        # ofile.write("Word                Count \n")
        # ofile.write("------------------------- \n")
        # length = 21
        # for key, value in lst:
        #     key_length = len(key)
        #     filler = length - key_length
        #     out = key + ' ' * filler + str(value) + '\n'
        #     ofile.write(out)
        for key, value in lst:
            ofile.write(f"{key : <15}{value : ^30} \n")


def main():
    """
    Main function to open the text file, read line by line, call other functions to process
    the lines and store the words in a dictionary with frequency from high to low. Also print the
    output.
    :return:
    """
    dictionary = dict()  # defining the dictionary
    print("Welcome to the text to word frequency converter!!")

    while True:
        iname = input("What's the input file name in 'name.txt' format? ").strip()

        try:
            gba_file = open(iname, 'r')  # Open the text file.
        except FileNotFoundError as ex:
            print(ex)
        else:
            oname = input("What's the output file name in 'name.txt' format? ").strip()
            while os.path.exists(oname):
                oname=input(f"Output file name '{oname}' is already present. Please try another name: ").strip()
            break

    for line in gba_file:
        process_line(line, dictionary)  # calling the process_line function

    # print(f"Length of the dictionary: {len(dictionary)}")
    process_file(dictionary, oname)  # calling the process_file function

    print(f"Output file '{oname}' has been created successfully. Have a nice day!!")
    gba_file.close()  # Close the input text file.


if __name__ == "__main__":
    main()  # calling the main function
