import re

def stripRegex(string, remove="default"):
    if remove == 'default':
        front = re.sub("^\s+","",string)
        frontAndBack = re.sub("\s+\Z", "",front)
        print(frontAndBack)
    else:
        modifiedString = re.sub(remove,"",string) 
        print(modifiedString)

string = '    hey there     '
stripRegex(string)
string = 'hey there'
remove = 'e'
stripRegex(string, remove)
string = 'hey there       '
stripRegex(string)
