#24/6/2018 - Samuel McHale - Sorting functions comparison tools

import time
import random
from matplotlib import pyplot as plt

from sortingFunctions import *

sortIds = ['Bubble Sort','Quick Sort']

def randomArray(valueRange, arrayLength):
    array = []
    for i in range(arrayLength):
        array.append(random.randint(1,valueRange))
    return array

def meanSortTime(valueRange, arrayLength, repeats, sortId):
    total = 0
    for i in range(repeats):
        items = randomArray(valueRange, arrayLength)
        t1 = time.time()

        #Add functions to be tested here with unique control circumstance
        if sortId == 1:
            bubbleSort(items)
        elif sortId == 2:
            quickSort(items)
        else:
            print('Sorting function not found, invalid sort Id')
            
        t2 = time.time()
        dif = t2 - t1
        total += dif
        
    return total/repeats

def compareSortFunctions(testLengths, testValueRange, repeats):
    completeData = []
    markerSet = ['b','r','g','c','m','y','k']
    for i in range(len(sortIds)):
        i += 1
        lengthdata = []
        timedata = []
        for length in testLengths:
            lengthdata.append(length)
            timedata.append(meanSortTime(testValueRange,length,repeats,i))
        completeData.append([lengthdata,timedata])
        
    for i in range(len(completeData)):
        name = sortIds[i]
        plt.plot(completeData[i][0],completeData[i][1],'-x',c=markerSet[i],label=name)
    plt.legend()
    plt.xlabel('Number of items sorted')
    plt.ylabel('Time (s)')
    plt.show()
