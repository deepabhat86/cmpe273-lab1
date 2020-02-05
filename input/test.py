import asyncio
import aiofiles
import os

directory = "/tmp"
listOfLists = list()

async def sortingFiles(numbersInList):
    numbersInList.sort()

async def awaitProcessFiles(filename,numbersInList):
    await readFromFile(filename,numbersInList)
    await sortingFiles(numbersInList)
    await appendToList(numbersInList)


async def readFromFile(filename,numbersInList):
    async with aiofiles.open(directory+"/"+filename, 'r') as fin:
        async for line in fin:
            return numbersInList.append(int(line.strip("\n"),10))            
    fin.close()    

async def appendToList(numbersInList):
    listOfLists.append(numbersInList)

async def main():
    tasks=[]
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  
            numbersInList =list()
            task=asyncio.ensure_future(awaitProcessFiles(filename,numbersInList))
            tasks.append(task)
    await asyncio.gather(*tasks)   

if __name__== "__main__":
    asyncio.run(main())
