print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# This will pass the variable 'start-point' and its corresponding value of 10000
# into the 'started' argument of 'secret_formula'
start_point = 10000

# This creates new variables to store the output of jelly_beans, jars, and crates;
# despite the fact that 2 out of 3 of them are not changed, these are different
# variables from the ones above as shown by the word 'beans'; each argument here
# corresponds with the relevant variables above.
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point /= 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
