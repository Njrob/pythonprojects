name = 'Nicholas J. Roberts'
age = 26 # not a lie
height = 74 # inches
height_cm = 74 * 0.393701 # height in centimeters
weight = 180 # pounds
weight_kg = 180 * 0.453592 # weight in kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'

print "Let's talk about %r." % name
print "He's %r feet tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, weight, height, age + weight + height)

print "If we use the metric system, he is %r centimeters tall and %r kilograms heavy." % (height_cm, weight_kg)
