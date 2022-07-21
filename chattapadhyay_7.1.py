# Author: Kausik Chattapadhyay
# DSC 500 Assignment 7.1
# Date 07/21/2022
# Program to calculate the total words, and output the number of occurrences of each word in the file.

import string


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
    words = line.split()  # splitting the line into words

    for word in words:
        add_word(word, dictionary)  # calling the add_word function


def pretty_print(dictionary):
    """
    Function to print the length and the dictionary from high to low frequency.
    :param dictionary:
    :return:
    """
    print(f"Length of the dictionary: {len(dictionary)}")
    print("Word                Count")
    print("-------------------------")

    # Sort The dictionary by value
    # lst = list()
    # for key, value in list(dictionary.items()):
    #     lst.append((value, key))
    #
    # lst.sort(reverse=True)
    lst = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    # Make some space between word, and it's frequency to print nicely.
    length = 21
    for key, value in lst:
        key_length = len(key)
        filler = length - key_length
        print(key, ' ' * filler, value)


def main():
    """
    Main function to open the text file, read line by line, call other functions to process
    the lines and store the words in a dictionary with frequency from high to low. Also print the
    output.
    :return:
    """
    dictionary = dict()  # defining the dictionary

    gba_file = open('gettysburg.txt', 'r')  # Open the text file.

    for line in gba_file:
        process_line(line, dictionary)  # calling the process_line function

    pretty_print(dictionary)  # calling the pretty_print function


if __name__ == "__main__":
    main()  # calling the main function
