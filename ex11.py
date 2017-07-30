print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "What school do you go to?",
school = raw_input()
print "What is your GPA?",
gpa = raw_input()
print "What is your zip code?",
zip_code = raw_input()

print "So, you go to %s, you have a GPA of %s, you have a zip code of %s, and you %s enjoy going to school there." % (
    school, gpa, zip_code)
