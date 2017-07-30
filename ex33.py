def buildList(num, increment):
    numList = []
    i = 0
    while i < num:
        numList.append(i)
        i += increment
        print "i: %d, " % i,
        print "list: ", numList
    #note: you don't need to return a value

#you can hard code any number here, of course
buildList(6, 2)

def secondlist(num):
    numList = []
    i = 0
    for i in range(num):
        numList.append(i)
        print "i: %d" % i,
        print "list: ", numList

secondlist(10)
