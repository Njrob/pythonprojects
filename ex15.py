# Importing the argument variable from the sys module
from sys import argv

# Defining the arguments which need to be made in order for the script to run
script, filename = argv

# A variable, txt, is defined by its execution of the open command on the filename argument variable. If printed/called, the variable will executed the command.
txt = open(filename)

# Prints a string with a formatted variable which holds the filename inputted by the user in the original argument
print "Here's your file %r:" % filename

# Prints the txt variable, which opens ex15_sample.txt, and then executes the read function so that ex15_sample.txt is opened and readable right in the terminal
print txt.read()
txt.close()

# A printed string
print "Type the filename:"

# This variable will take raw_input from the user, and it must be a file contained within the same directory as ex15.py
file_again = raw_input("> ")

# Like the original txt variable, this one executes an open command on the variable defined above by the input of a txt file within the same directory as this exercise
txt_again = open(file_again)

# Like line 14, this prints the txt_again variable and executes the read function; txt_again is itself a transformation of the input given for file_again
print txt_again.read()
txt_again.close()

# Since we are getting input from the user, it makes more sense to only use raw_input rather than argv
