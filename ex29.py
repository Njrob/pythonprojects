people = 35
cats = 30
dogs = 30

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled in!"

if people > dogs:
    print "The world is dry!"

if people > dogs and cats:
    print "The world has more people than cats or dogs."

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# the if statement creates a set of conditions; if one condition is met, something will
# be printed/be returned; if another condition is met, something else will be printed/returned
