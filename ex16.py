# Importing the argv feature from the sys module
from sys import argv

# Defining the arguments which need to be made to run the script
script, filename = argv

# Prints a string with a formatted variable (filename)
print "We're going to erase %r." % filename

# Prints a string
print "If you don't want that, hit CTRL-C (^C)."

# Prints a string
print "If you do want that, hit RETURN."

# Prompts an input from the user; any input will achieve the same result despite what is said in the above strings
raw_input("?")

# Prints a string
print "Opening the file..."

# Defines a variable to execute an open command.  The 'w' stands for write, which is an optional argument taken by open().  Having 'w' in here automatically truncates the file.
target = open(filename, 'w')

# Prints a string
print "Truncating the file. Goodbye!"

# Executes a truncate function on the target variable, but this is unnecessary since opening the filename in 'w' already does this automatically.
target.truncate()

# Prints a string
print "Now I'm going to ask you for three lines."

# Defines lines1-3 as user input and stores this input in each variable
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Prints a string
print "I'm going to write these to the file."

line_break = "\n"

# Executes a write function on the target, which targets the file object.  Six lines are given here; three for actual lines, three for line breaks.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# Prints a string
print "And finally, we close it."

# Executes a close function on the target (file object) and saves it
target.close()
