tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

def printTable(listTable):
    colWidths = [0] * len(listTable)
    for i in range(len(listTable[0])):
        for j in range(len(listTable)):
            colWidths[j] = len((max(listTable[j], key=len)))
            a = listTable[j][i]
            print(a.rjust(colWidths[j]), end=' ')
        print("\n")
#    for s in colWidths:
#        s = listTable[n]
#        n += 1
#        for i in s:
#            maxlen = len(max((s), key=len))
#            element = i.rjust(maxlen)
#            print(element)

printTable(tableData)
