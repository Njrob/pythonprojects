people = 39
cars = 40
trucks = 15
trains = 10
highways = 50

if cars > people and trucks < cars:
    print "We should take the cars."
    print "...and not take the trucks."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
# elif trucks < cars:
    # print "Maybe we can take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

if cars < people or highways >= trains:
    print "There are too many people and the highway lobby has killed public transportation."
