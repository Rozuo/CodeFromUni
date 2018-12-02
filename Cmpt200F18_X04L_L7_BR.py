print("Cmpt200F18_X04L_L6_BR.py 1.00 3048109 Ross Beaudin")
'''*****************************************************************************
CMPT200- LAB 7 - Sorting and Arrays
Section: X04L
Cmpt200

This program creates a random list of numbers and sorts them by bubbleSort, 
mergeSort, quickSort, heapSort. The program then will take statistics of the 
program and stores them in a text file. These statistics are run time, number
of accesses, number of recursive calls and extra space.

REFS: 
Lecture slides on Linked lists by Alex Kreiger
https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
*****************************************************************************'''

from random import * 

#from random import sample

#N = 1000
#L = sample([i for i in range(N)], N)
#print("before:", L)
#bubbleSort(L)
#print("After:", L)

from random import sample
from time import time

class Sorting:
        
    def __init__(self, size):
        self._A = sample([i for i in range(size)], size)   
        print("Before:", self._A[:5], "...", self._A[-5:])      # Dev check 
        self._copy = None       # Will be a copy of the array above
        self._timeDif = 0       # Duration of sort for the selected sort 
        self._nAcc    = 0       # algorithm
        self._recCount = 0
        self._exSpace = 0
    
    # will try to open the text file that stores values. If this file doesn't 
    # exist create a new file and begin writing to that file.
    def save_stats(self, fName):
        fileExists = False
        try:
            f = open(fName, "r")
            fileContent = f.read()
            f.close()
            f = open(fName, "w")
            f.write(fileContent + "%-15s %5d %9d %10d %7d %15.12f\n" % \
                    (s + " Sort", len(self._A), self._nAcc, self._recCount,\
                     self._exSpace, self._timeDif))
            f.close() 
            return
        except:
            f = open(fName, "w")
            f.write(
                "FILE: " + fName + '\n'
                "SORT             Data     Array  Recursive   Extra  Elapsed\n"
                "                 Size       Ops      Calls   Space  Time\n\n")
        
            f.write("%-15s %5d %9d %10d %7d %15.12f\n" % \
                    (s + " Sort", len(self._A), self._nAcc, self._recCount,\
                     self._exSpace, self._timeDif))
            f.close()
            return
        
    def sort(self, typeSort):
        self._copy = self._A.copy()    # Keep original data
        timeStart = time()    
        if s == 'bubble':
            self._nAcc = 0
            self._exSpace = 0
            self._nAcc = self.bubbleSort(self._copy)
        elif s == 'quick':
            self._recCount = 0
            self._nAcc = 0
            self._exSpace = 0
            self.quickSort(self._copy, 0, len(self._copy)-1)
        elif s == 'merge':
            self._recCount = 0
            self._nAcc = 0
            self._exSpace = 0
            self._copy = self.merge_sort(self._copy)
        elif s == 'heap': 
            self._nAcc = 0
            self._exSpace = 0
            self.heapSort(self._copy)
        
        self._timeDif = time() - timeStart
        # This is to demonstrate that the functions do sort the values
        print("After:", self._copy[:5], "...", self._copy[-5:])
        
        # The code below that is commented are for dev checks 
        
        #print("\nDuration: %12.10f\nAccesses: %6d\nRecursive Calls: %6d" %\
              #(self._timeDif, self._nAcc, self._recCount))
        #print("Extra Space: %6d" % self._exSpace)
        
        self.save_stats("Cmpt200F18_L7_Results_BR.txt")
        print("\nFile has been created and has stored the data.")
        return self._timeDif, self._nAcc, self._recCount, self._exSpace
    
# bubble sort section ------------------------------------------------------
    def bubbleSort(self, A):
        nAcc = 0
        for end in range(len(A)-1, -1, -1):
            for i in range(0, end):
                nAcc += 2                       # 2 accesses of data
                if A[i] > A[i+1]:
                    nAcc += 4                   # 4 accesses of data
                    A[i], A[i+1] = A[i+1], A[i]
        return nAcc
    
    
# Quick sort section -------------------------------------------------------
    # helper function for the quick sort
    def partition(self, array, first, last):
        #print("first:",first,"last:",last)        # Dev check
        big = first + 1
        small = last
        pivot = array[first]
        self._exSpace += 3       # accessed data and created three new variables
        self._nAcc += 1
        while (big <= small) :
            while (big <= last and array[big] <= pivot) :
                self._nAcc += 1
                big += 1
            while array[small] > pivot :
                self._nAcc += 1
                small -= 1
            if big < small :
                self._nAcc += 4
                array[small], array[big] = array[big], array[small]
                
        self._nAcc += 4
        array[first], array[small] = array[small], array[first]
        return small
    
    # Main quick sort function
    def quickSort(self, array, first, last) :
        self._recCount += 1
        if first >= last :
            return
        pivLoc = self.partition(array, first, last)      # more space is created
        self._exSpace += pivLoc
        
        self.quickSort(array, first, pivLoc-1)
        self.quickSort(array, pivLoc+1, last)
        return
    

                
# Merge sort section -------------------------------------------------------
    def merge_sort(self, lst):                    # From Cmpt103 noted
        self._recCount += 1
        if len(lst) < 2: return lst
        
        mid = len(lst)//2
        self._exSpace += 1              # add to extra space due to new variable
        #print(lst, "mid:", mid, "==>", lst[:mid], lst[mid:])
        
        L, R = self.merge_sort(lst[:mid]),  self.merge_sort(lst[mid:])
        self._exSpace += len(lst)                          # excess data
        self._nAcc += 2
        
        
        #print(L, 'and:', R, end=' ==> ')       	   # Just to see
        merged = []
        self._exSpace += 1
        while len(L) * len(R) > 0:                      # If both lengths > 0
            self._nAcc += 2
            if L[0] < R[0]:  
                self._nAcc += 1
                merged.append(L.pop(0))      # List constantly expands therefore
                self._exSpace += 1           # extra space is created               
            else:
                self._nAcc += 1
                merged.append(R.pop(0))
                self._exSpace += 1
                
        merged += L + R
        self._exSpace += len(lst)
        #print(merged)
        return merged
        
# Heap Sort section --------------------------------------------------------
    def swapDown(self, myArray, last) :
        insPt = 0
        done = False
        self._exSpace += 2
        while (not done and ((2*insPt+1) <= last)):
            bigChild = 2*insPt + 1
            self._exSpace += 1
            self._nAcc += 2
            if ((bigChild+1) <= last and
                myArray[bigChild+1] > myArray[bigChild]) :
                bigChild += 1
            self._nAcc += 2
            if myArray[insPt] < myArray[bigChild] :
                self._nAcc+= 4
                myArray[insPt], myArray[bigChild] = \
                    myArray[bigChild], myArray[insPt]
                insPt = bigChild
            else:
                done = True
        return
                
    def mergeHeaps(self, myArray, rt) :
        insPt = rt
        done = False
        self._exSpace += 2
        while (not done and ((2*insPt+1) < len(myArray))):
            bigChild = 2*insPt + 1
            self._exSpace += 1
            self._nAcc += 2
            if ((bigChild+1) < len(myArray) and
                myArray[bigChild+1] > myArray[bigChild]) :
                bigChild += 1
            self._nAcc += 2
            if myArray[insPt] < myArray[bigChild] :
                self._nAcc += 4
                myArray[insPt], myArray[bigChild] = \
                    myArray[bigChild], myArray[insPt]
                insPt = bigChild
            else:
                done = True
        return 
    
    def buildHeap(self, myArray) :
        lastChild = len(myArray) - 1
        self._exSpace += 1
        
        for i in range((lastChild-1)//2,-1,-1): #(lastChild-1)//2 parent of
            self.mergeHeaps(myArray,i) # lastChild
        return 
    
    # Main heap Sort function
    def heapSort(self, myArray) :
        self.buildHeap(myArray)
        for i in range(len(myArray)-1,0,-1) :
            self._nAcc += 4
            myArray[0], myArray[i] = myArray[i], myArray[0]
            self.swapDown(myArray,i-1)
        return 
    

if __name__ == "__main__":
    for s in ['bubble', 'quick', 'merge', 'heap']:
        for N in [10, 100, 1000]:
            print("\nSort:", s.title(), 'Data size:', N)
            data = Sorting(N)
            performance = data.sort(s)
            