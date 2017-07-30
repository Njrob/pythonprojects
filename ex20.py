# Importing the argv feature from the sys module
from sys import argv

# argv will accept exactly two arguments: the name of the script, and the name of the file to be read by the script
script, input_file = argv

# Creates a function 'print_all' which will read and print the input file
def print_all(n):
    print n.read()

# Creates a function 'rewind' which uses the .seek command/function to move to the beginning of the document in terms of bytes
def rewind(n):
    n.seek(0)

# Defines a function called 'print_a_line' which takes two arguments: the line_count (an integer), and n (a filename).
# the function will print out the integer input for line_count; readline is a function which reads up to the end of each line and
# adds a new line space between each line
def print_a_line(line_count, n):
    print line_count, n.readline()

# Sets current_file equal to the input_file, and opens it in the terminal to be read or written over.
current_file = open(input_file)

# Print's a string, followed by a \n which will add a line of whitespace between this statement and the output of the file
print "First let's print the whole file:\n"

# Prints the contents of the input file
print_all(current_file)

# Simple string/print statement
print "Now let's rewing, kind of like a tape."

# Uses the rewind function to go back to the first byte of the input file
rewind(current_file)

# Simple print statement for a string
print "Let's print three lines:"

# Tells us where to begin; each line contains a += to denote that for each line, we are adding 1 to the current_line
current_line = 1 # starts at 1
print_a_line(current_line, current_file)

current_line += 1 # 2
print_a_line(current_line, current_file)

current_line += 1 # 3
print_a_line(current_line, current_file)
