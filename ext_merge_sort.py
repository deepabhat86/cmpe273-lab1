import os
import time
from heapq import merge

inputDirectory = os.getcwd()+os.path.sep+'input'
outputDirectory = os.getcwd()+os.path.sep+'output'
listOfLists = list()
afterKwayMerge = list()

def sortList(numbersInList):
    numbersInList.sort()

#read and sort individual files add it to list of list
def processFiles(fileName, numbersInList):
    #To simulate large files, sleep(0.1) has been introduced to the sync program to prove that async is faster.
    time.sleep(0.1)
    readFromFile(fileName,numbersInList)
    sortList(numbersInList)
    listOfLists.append(numbersInList)

#reading from the file
def readFromFile(filename,numbersInList):
    with open(inputDirectory+os.path.sep+filename, 'r') as fin:
        for line in fin:
            numbersInList.append(int(line.strip("\n"),10))   
    fin.close()    
 
# k-way merge sort
def kWayMerge(*listOfList):
    return list(merge(*listOfList))

#Writing to the final sorted file
def writeToFile(afterKwayMerge):
    filename = outputDirectory+os.path.sep+"sorted.txt"
    with open(filename,'w') as fout:
        for line in afterKwayMerge:
            fout.write(str(line) + '\n')
    fout.close      
        
def main():
    for filename in os.listdir(inputDirectory):
        if filename.endswith(".txt"):
            numbersInList =list()
            processFiles(filename,numbersInList)

    afterKwayMerge = kWayMerge(*listOfLists)
    writeToFile(afterKwayMerge)

if __name__== "__main__":
    main()
