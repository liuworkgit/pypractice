####################################################
# Text Reader
# Given a file path to a text file, the program will read the text file
# and print out the text to the terminal.
#######################################################
path_to_file = input("Please enter a file path to the file you want read: ")
try:
    with open(path_to_file) as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print("File does not exist.")