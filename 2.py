import re
import collections

temp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
#-----------------------------------------
def openFile(filename):
    input = open(filename, 'r')
    aString = input.read()
    return aString
#---------------------------------------
def parseFile(aString):
    pResult = re.findall(temp, aString)
    return pResult
#------------------------------------------
def countIP(pResult):
    count = collections.Counter(pResult)
    return(count)
#---------------------------------------
def tenIP(count):
    b = list(count.items())
    b.sort(key=lambda item: item[1], reverse=True)
    print(b)
    return b
#-----------------------------------------

if __name__ == '__main__':
    m = (tenIP(countIP(parseFile(openFile('access_log')))))
    h = 0
    for i in m:
        print(  i[0], '=>', str(i[1]))
        h += 1
        if h == 10:
            break
