import asyncio
import os
from heapq import merge

inputDirectory = os.getcwd()+os.path.sep+'input'
outputDirectory = os.getcwd()+os.path.sep+'output'
listOfLists = list()
afterKwayMerge = list()

def sortingFiles(numbersInList):
    numbersInList.sort()


#read and sort individual files add it to list of list    
async def awaitProcessFiles(filename,numbersInList):
    
    #force asyncio to process files in parallel
    await asyncio.sleep(.1)
    
    #reading from the file
    with open(inputDirectory+os.path.sep+filename, 'r') as fin:
        for line in fin:
            numbersInList.append(int(line.strip("\n"),10))            
    fin.close() 
    sortingFiles(numbersInList)
    appendToList(numbersInList)

# k-way merge sort
def kWayMerge(*listOfLists):
    return list(merge(*listOfLists))

def appendToList(numbersInList):
    listOfLists.append(numbersInList)

#Writing to the final sorted file
def writeToFile(AfterKwayMerge):
    filename = outputDirectory+os.path.sep+"sorted_async.txt"
    with open(filename,'w') as fout:
        for line in AfterKwayMerge:
            fout.write(str(line) + '\n')
        fout.close      
        
async def main():
    tasks=[]
    for filename in os.listdir(inputDirectory):
        if filename.endswith(".txt"):  
            numbersInList =list()
            task=asyncio.ensure_future(awaitProcessFiles(filename,numbersInList))
            tasks.append(task)   
    await asyncio.gather(*tasks)   
    afterKwayMerge = kWayMerge(*listOfLists)
    writeToFile(afterKwayMerge)

if __name__== "__main__":
    asyncio.run(main())
