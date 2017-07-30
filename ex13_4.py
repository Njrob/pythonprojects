from sys import argv

script, age, height, weight = argv

print "So, you are %s years old. What is your exact birthday?" % age
birthday = raw_input()
print "You are %s tall. Are you satisfied with your height?" % height
sat_height = raw_input()
print "You are %s heavy. Are you satisfied with your weight?" % weight
sat_weight = raw_input()

print "So your birthday is on %s.  You answered %s for satisfaction about your height and %s for satisfaction about your weight." % (
    birthday, sat_height, sat_weight)
