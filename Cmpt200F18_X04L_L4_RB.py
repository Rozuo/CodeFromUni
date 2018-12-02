print("Cmpt200F18_X04L_L4_RB.py 3048109 Ross Beaudin")
'''*****************************************************************************
CMPT200- LAB 4 - Queues
Section: X04L
Cmpt200

Program purpose: This program's purpose is to simulate how two printers would 
print out pages if they were just plugged in with orders waiting. Through, queue
and dequeue functions

REFS: Lab 4 lecture monday october 15,
https://www.cs.usfca.edu/~galles/visualization/QueueLL.html
Linked Queue program from blackboard
*****************************************************************************'''
from random import randint
# Program 1
#-------------------------------------------------------------------------------
# Node will be the queues content
class Node:
    
    def __init__(self, var, nex = None): # The variable is stored while next one
        self._var = var                  # will be prepared
        self._nex = nex
        
    def __repr__(self):
        return s + str(self._var) + ' -> ' + \
               (str(self._nex) if self._nex != None else 'END')
    
    def demo():
        print("n1 = Node(5, Node(4, Node(7)))")
        n1 = Node(5, Node(4, Node(7)))
        print("n1 ->", n1)

class Queue:
    '''
    Usage: Q = Queue()
    - len()
    - repr()
    - isEmpty()
    - first()
    - enqueue(var)
    - dequeue()
    '''
    class _Node:
        #__slot__ = '_var', '_nex'
        def __init__(self, var, nex = None):
            self._var = var
            self._nex = nex
            
    # head will be the first value to be queued while tail will be the last.
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    # Display the head of the queue all the way to the tail.
    def __repr__(self):
        s = ''
        p = self._head                      # Get ref to the first Node
        while p != None:
            s += str(p._var) + ' -> '
            p = p._nex
        s += 'END'
        return s
    
    def __len__(self):
        return self._size
    # if the queue is empty return true else return false.
    def isEmpty(self):
        return True if len(self) == 0 else False
    
    # assign the first variable in the queue to be the head
    def first(self):
        if self.isEmpty:
            raise(Exception('Error the queue is empty!'))
        return self._head._var
    
    # remove an item from the queue as long as it still has a variable. 
    # While reassigning the head
    def dequeue(self) :
        if self.isEmpty():
            raise Empty('Queue is empty')
        ans = self._head._var
        self._head = self._head._nex        # reassign the head to the next 
        self._size -= 1                     # value.
        if self.isEmpty() :
            self._tail = None
        return ans
    
    # add an item to the queue and assign it as the tail.
    def enqueue(self, e) :
        new = self._Node(e, None)           # assign the new value within node
        if self.isEmpty() :
            self._head = new
        else :
            self._tail._nex = new           # it will become the tail if a the
        self._tail = new                    # list is not empty. While 
        self._size += 1                     # establishing that the next 
                                            # variable is within node shall be 
                                            # the tail
    
    # demonstrate the class queue's functionallity.
    def demo(self):
        Q = Queue()
        for v in [ 'Jack', 'Bob', 6, ('Fil', 4), ('Jill', 7) ]:
            print("Enqueueing:", v, end=' ==> Q -> ')
            Q.enqueue(v)
            print(Q)
            
        print("\nThere are", len(Q), "elements in the queue.")
        input("Press ENTER ...")
        
        while not Q.isEmpty():
            print("Dequeueing:", Q.dequeue(), end=' ==> Q -> ')
            print(Q)    
#-------------------------------------------------------------------------------

class Printer():
    
    def __init__(self, name):           # Give the printer a name and assign 
        self._name = name               # class.
        self._pages = 0 
        
    def __repr__(self):                 # display to the user if the printer is 
        if self._pages > 0: return str(self._pages) # ready for another print 
        if self._pages <= 0: return 'Ready'   # else display the remaining page.
        
    def ready(self):                # If no pages remain the printer is ready.
        return self._pages == 0
    
    # Will print out one page if you use print()
    # If a n pages is in print(n) then it will print out n amount of pages.
    def printing(self, pages = 0):
        if pages > 0:
            self._pages = pages
        else:
            if self._pages >0:
                self._pages -= 1
    def demo(self):                     # Demonstrate the printer class.
        page = Printer("Jack")
        print("Printer", page._name, "is", page)
        page.printing(4)
        while not page.ready():
            print("Printing:", page, "pages:")
            input("Press ENTER ...")
            page.printing()
        print("Printer:", page)
        input("All done! Press ENTER ...")
            
def main():
    printQueue = Queue()        # assign Queue class
    
    print("\nPrint Queue Simulation")
    print("Time\tPrint Queue                               Prn R     Prn G")
    printList = [4, 6, 3, 5, 2, 7]
    maxNum = len(printList)              # determine the max length
    canPrint = False                     # determine when to print
    printQueue.enqueue(printList.pop(0)) # pop the first item in the list to the
    red = Printer('Red')                 # queue to create the head
    green = Printer('Green')    # assign printer classes (activate printers)
    i = 0                       # a counter to stop the loop in case of an 
                                # infinite loop situation
    while not printQueue.isEmpty() and i < 100: # if the queue has items and the 
                                   # limiter has not been surpase run the loop.
        if maxNum == len(printQueue): # Determine if all items are in the queue.
            canPrint = True        
        i += 1
        count = 1
        print(' %2d  '% i , '   ', printQueue) # display the increasing queue
        if printList:
            printQueue.enqueue(printList.pop(0)) # aquire another item to the 
        while canPrint and not printQueue.isEmpty() and i < 500: # queue.
            i += 1
            if (red.ready() or green.ready()): # increase the count if the 
                if len(printQueue) != 3:       # length does not equal to 3
                    count += 1                 # the tabs are increase by 1.
                                           
            if red.ready():                          # If the printer is ready
                red.printing(printQueue.dequeue())   # Aquire printing request
            if green.ready():                   
                green.printing(printQueue.dequeue())
            
            while not red.ready() or not green.ready() and i <1000:
                i += 1
                print(' %2d  '% i , '   ', printQueue, " \t  "*count, red,\
                      "        ", green) # print out the remaining print queue 
                red.printing()           # and requests being processed.
                green.printing()         # print out one page from the request.
                if (red.ready() or green.ready()):
                    if not printQueue.isEmpty():
                        i += 1
                        if red.ready():   # This is used to tidy the display 
                            spaces = "    " # when one of the printers are ready
                        else:               # or the other.
                            spaces = "        "
                        print(' %2d  '% i , '   ', printQueue, " \t  "*count, \
                              red, spaces, green)                        
                        break
                    elif printQueue.isEmpty and red.ready() and\
                         green.ready():                 # Print for the final 
                        i += 1                          # statement.
                        print(' %2d  '% i , '   ', printQueue, " \t  "*count,\
                              red, "    ", green)                        
                        break
                        

if __name__ == '__main__':
    main()
    