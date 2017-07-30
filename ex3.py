# The first line will print a statement about the output

print "I will now count my chickens:"

# Order of operations: 30 / 6 is calculated first, then added to 25
print "Hens", 25 + 30 / 6

# Everything else in this equation is done prior to subtracting anything from 100.  The first operation is 25 * 3 (75), and the remainder of 75 / 4 is 3 (the % operator).  100 - 3 = 97.
print "Roosters", 100 - 25 * 3 % 4

# Another output statement.
print "Now I will count the eggs:"

# 4 % 2 and 1 / 4 are treated as expressions within this larger equation.  3 + 2 + 1 = 6, 6 - 5 = 1.  There is no remainder when 4 / 2 so nothing is added from that expression, and 1/4 is an integer of zero in Python 2. 1 + 6 = 7.
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# Output statement.
print "Is it true that 3 + 2 < 5 - 7?"

# A boolean statement; same result is achieved without using the print function.
print 3 + 2 < 5 - 7

# Two strings followed by operations.
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

# Output statement/string.
print "Oh, that's why it's false."

# Another output statement/string.
print "How about some more."

# Three strings followed by booleans.
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
