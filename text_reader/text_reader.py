####################################################
# Text Reader
# Given a file path to a text file, the program will read the text file
# and print out the text to the terminal.
#######################################################
option = input("Do you want to read or write to a file? [r/w]")
if option == "r":
    path_to_file = input("Please enter the path to the file to be read: ")
    try:
        with open(path_to_file, "r") as file:
            text = file.read()
            print(text)
    except FileNotFoundError:
        print("File does not exist.")
elif option == "w":
    path_to_file = input("Please enter the path to the file you want to write to: ")
    text_to_write = input("Enter the text you want to write to the file: ")
    with open(path_to_file, "w") as file:
        file.write(text_to_write)
        print("Successfully wrote to file.")