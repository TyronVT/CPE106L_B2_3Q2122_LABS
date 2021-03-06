"""
Program: stats.py
Author: Jason Moslares
Creation of mean function combined with mode.py, and median.py
This program expects a list, compute and output mean, median and mode.
Returns 0 if the list is empty.
"""

def mean(fileName):
    f = open(fileName, 'r')
    theSum = 0
    counts = 0
    for line in f:
        wordlist = line.split()
        counts += 1
        for word in wordlist:
            number = int(word)
            theSum += number
    if(counts == 0):
        return 0
    else:
        mean = round(theSum / counts, 2)
        print("The mean is", mean)
    f.close()

def median(fileName):
    f = open(fileName, 'r')
    counts = 0
    numbers = []
    for line in f:
        words = line.split()
        counts += 1
        for word in words:
            numbers.append(float(word))
    if(counts == 0):
        return 0
    else:
        numbers.sort()
        midpoint = len(numbers) // 2
        print("The median is", end=" ")
        if len(numbers) % 2 == 1:
            print(numbers[midpoint])
        else:
            print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
    f.close()
    
def mode(fileName):
    f = open(fileName, 'r')
    counts = 0
    words = []
    for line in f:
        wordsInLine = line.split()
        counts += 1
        for word in wordsInLine:
            words.append(word.upper())
    if(counts == 0):
        return 0
    else:
        theDictionary = {}
        for word in words:
            number = theDictionary.get(word, None)
            if number == None:
                theDictionary[word] = 1
            else:
                theDictionary[word] = number + 1
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                print("The mode is", key)
                break
    f.close()

def main():
    fileName = input("Enter the file name: ")
    mean(fileName)
    median(fileName)
    mode(fileName)

main()
