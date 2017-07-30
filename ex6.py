# A variable storing a string, which is also storing a formatted variable (10)
x = "There are %d types of people." % 10

# A variable storing a string
binary = "binary"

# Another variable storing a string
do_not = "don't"

# A variable storing a string, which is in turn storing multiple formatted variables.
y = "Those who know %s and those who %s." % (binary, do_not) # First two instances of a string inside a larger string.

# Printing the first variable, which will be output as a string.
print x

# Now the second variable, also output as a string.
print y

# Printing the first variable holding a string (x) again.
print "I said: %r." % x # Third instance of a string within a string.

# Now printing the second variable holding a string (y) again.
print "I also said: '%s'." % y # Fourth instance.

# Defining the word 'hilarious' as a boolean which will output 'False'
hilarious = False

# Defining the variable 'joke_evaluation' with a question, followed by a formatted variable; without the formatted variable, 'hilarious' will not print.
joke_evaluation = "Isn't that joke funny?! %r"

# Printing the variable with the formatted variable, which is the boolean 'hilarious'.
print joke_evaluation % hilarious

# Basic string variable
w = "This is the left side of..."

# And again
e = "a string with a right side."

# Now let's print those two strings together.  When the addition sign is used on strings, it adds the text together to form one string.
print w + e
