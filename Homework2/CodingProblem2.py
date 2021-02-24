#Name: Juan Gonzalez
#ID: 1808943

#Stage B

from datetime import date

today = date.today()
currDate = today.strftime("%m/%d/%y")

def sentenceWorks(sentence):
    if '-1' in sentence:
        return False
    elif ',' in sentence:
        if (sentence.count(' ') == 2):
            return True
        else:
            return False

def getMonth(sentence):
    if 'January' in sentence:
        return '1'
    elif 'February' in sentence:
        return '2'
    elif 'March' in sentence:
        return '3'
    elif 'April' in sentence:
        return '4'
    elif 'May' in sentence:
        return '5'
    elif 'June' in sentence:
        return '6'
    elif 'July' in sentence:
        return '7'
    elif 'August' in sentence:
        return '8'
    elif 'September' in sentence:
        return '9'
    elif 'October' in sentence:
        return '10'
    elif 'November' in sentence:
        return '11'
    elif 'December' in sentence:
        return '12'

def getDay(sentence):
    comLoca = sentence.find(',')
    numList = [sentence[comLoca - 2], sentence[comLoca - 1]]
    if ' ' in numList:
        numList.remove(' ')
        dayNum = ''.join(numList)
        finDay = str(dayNum)
        return finDay
    else:
        dayNum = ''.join(numList)
        finDay = str(dayNum)
        return finDay

def getYear(sentence):
    yearList = [sentence[-5], sentence[-4], sentence[-3], sentence[-2]]
    yearJoin = ''.join(yearList)
    year = str(yearJoin)
    return year

def pastorpres(sentence):
    intMonth = int(getMonth(sentence))
    intDay = int(getDay(sentence))
    intYear = int(getYear(sentence))
    if intYear < today.year:
        return True
    elif intYear == today.year:
        if intMonth < today.month:
            return True
        elif intMonth == today.month:
            if intDay <= today.day:
                return True
            else:
                return False

file = open('inputDates.txt')

for line in file:
    if sentenceWorks(line):
        tempDate = [getMonth(line), getDay(line), getYear(line)]
        dateJoin = '/'.join(tempDate)
        work = pastorpres(line)
        if work:
            print(dateJoin)
    else:
        break

file.close()
