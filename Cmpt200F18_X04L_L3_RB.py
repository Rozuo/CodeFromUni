print("Cmpt200F18_X04L_L3_RB.py 3048109 Ross Beaudin")
'''*****************************************************************************
CMPT200- LAB 3 - Recursion
Section: X04L
Cmpt200

REFS: Lab 3 lecture monday october 1, 
Lecture slides on recursion and recursive backtracking by Alex Kreiger
Maze Solver by A. Salo
https://www.cs.bu.edu/teaching/alg/maze/
*****************************************************************************'''
# Program #1
#-------------------------------------------------------------------------------
def findSum(num = 498):
    
    if type(num) != list:           # seperate the number into it's respective 
        numList = list(str(num))    # singular digits if and only if this is the
    else:                           # first time the function is called. Else,
        numList = num.copy()        # create a copy of the current list of 
                                    # numbers.
    
    if len(numList) == 1:           # Ending parameter. If the list of integers 
        return int(numList[0])      #length equals to one return the last number
                                    # in the list.
    
    n = len(numList)-1              # Aquire the lenght of the list. and 
                                    # decrease it by one to process.
    # return the last number from the list and add it with the second last 
    # number from the list and so on until there is no more but one number 
    # remaining in the list.
    return int(numList.pop(n))+findSum("".join(numList)) 
#-------------------------------------------------------------------------------

# Program #2
#-------------------------------------------------------------------------------
def find_max(aList):
    '''
    return maximum integer in aList
    parameters: aList: list where to find maximum,
    pre: aList non-empty, elements of aList are comparable
    post: aList unmodified
    '''
    if aList == []:
        return
    return rec_find_max(aList, 0, len(aList)-1)

def rec_find_max(aList,start,end):
    '''
    return maximum integer in the sub-list of aList that starts at index
    start up to index end
    parameters: aList: list where to find maximum,
    start: start index in sub-list,
    end: last index in sub-list
    pre: start <=end
    '''
    # If the start is less then or equal to the end. Check to see if the 
    # aList[start] is greater then the number that follows it within the list. 
    # If aList[start] is greater then the second value return it. If not return 
    # the following number. If the start is greater then the end return the 
    # aList[end]. 
    if start <= end:
        if aList[start] > rec_find_max(aList, start + 1, end):
            return aList[start]
        else:
            return rec_find_max(aList, start + 1, end)
    else:
        return aList[end]
    
#-------------------------------------------------------------------------------

# put text file in a list to modify the maze
class Maze():
    
    def __init__(self, fileName = None):
        if fileName == None:
            self._text = self.fileRead('maze510.txt')
        else:
            self._text = self.fileRead(fileName)
        # From lab lecture slightly modified.
        self._lines = self._text.split('\n')
        self._height  , self._width  = [ int(i) for i in self._lines[0].split()]
        self._stRow   , self._stCol  = [ int(i) for i in self._lines[1].split()]
        self._endRow  , self._endCol = [ int(i) for i in self._lines[2].split()]
        self._maze = []
        for line in self._lines[3:]:
            self._maze.append(list(line))
        if len(self._maze) >= 12:           # This if statement was implemented 
            self._maze.remove([])           # due to the inconsistency of an 
                                            # empty list appearing in the 
                                            # ._maze
    def __repr__(self):
        return "\nDimensions: \n" + \
               str(self._height)   + ' ' + str(self._width)    + '\n'  +\
               str(self._stRow)    + ' ' + str(self._stCol)    + '\n'  +\
               str(self._endRow)   + ' ' + str(self._endCol)   + '\n' +\
               '\n'.join( [ ''.join(line) for line in self._maze])
    
    def fileRead(self, file):
        openedFile = open(file, 'r')         # Open file
        self.text = openedFile.read()        # Read contents
        openedFile.close()                   # Close file
        return self.text                     # return read contents.
        
    def findPath(self, h, w):
        if (h>=len(self._maze)-1 or w>=len(self._maze[0])-1):
            return False                            # Out of bounds cannot 
                                                    # proceed.
        if (h == self._stRow and w == self._endCol*2-1):
            pathFound = True
            self._maze[h][w] = '*'
            return True
                                                    # The finish point.
                                                    # Completed the maze
        if (self._maze[h][w] == '-' or self._maze[h][w] == '+' or \
            self._maze[h][w] == '|'):
            return False
                                                    # A wall, or corner cannot
                                                    # Cannot proceed
        if self._maze[h][w] == '*':
                                                    # An already explored path
                                                    # Try a different path
            return False
        if self._maze[h+1][w]=="+" or self._maze[h-1][w]=='+' or\
           (self._maze[h][w+1]== '+' or\
            self._maze[h][w-1] == '+'):       # By utilizing an if statment we 
            None                              # can ommit some marked positions 
        else:                                 # if a '+' is in one of the four 
            self._maze[h][w] = '*'            # positions near the current 
                                              # marked position and if a '+' is 
                                              # not present mark the current 
                                              # position (Unexplored path). 
        
        # If the next path is accessible and not blocked return True to continue
        # the recursion.
        if self.findPath(h - 1, w) == True:                                   
            return True                    # Go up
        if self.findPath(h, w + 1) == True:
            return True                    # Go right
        if self.findPath(h + 1, w) == True:
            return True                    # Go down
        if self.findPath(h, w - 1) == True:
            return True                    # Go left 
        self._maze[h][w] = ' '             
        return False                       # If we cannot advance from either up
                                           # , right, down or left clear 
                                           # previous marking and return False 
                                           # to move on to next point.
    def solve(self):      
        # Determine the actual dimension of the maze.
        completable = self.findPath(len(self._maze)-2, self._stCol) 
        if completable == True: # If the maze is completable display the maze.
            return self
        else:                   # else the maze is incompletable display error 
                                # message with maze.
            return print("Error! Maze cannot be completed!\n")
            
def demo_maze():
    print('\n Maze510.txt')
    maze = Maze()
    print(maze)
    print(maze.solve())
    input("Press enter for next maze maze1020.txt... ")
    print()
    maze = Maze("maze1020.txt")
    print(maze)
    print(maze.solve())
    input("Press enter for next maze maze50100.txt... ")
    print()    
    maze = Maze("maze50100.txt")
    print(maze)
    print(maze.solve())
    input("Press enter for next maze maze510island.txt... ")
    print()    
    maze = Maze("maze510island.txt")
    print(maze)
    print(maze.solve())
    input("Press enter for next maze maze510islandnosoln.txt... ")
    print()    
    maze = Maze("maze510islandnosoln.txt")
    print(maze)
    maze.solve()
    input("Press enter for next maze maze510cycles.txt...")
    print()    
    maze = Maze("maze510cycles.txt")
    print(maze)
    maze.solve()
    input("Press enter for next maze maze510nosoln.txt... ")
    print()        
    maze = Maze("maze510nosoln.txt")
    print(maze)
    maze.solve()
    input("End of demo press enter... ")      
    
if __name__ == '__main__':
    print("\nHere is the sum function with no inputs. (498)")
    print(findSum())
    input("Press enter to proceed... ")
    print("\nHere is the sum of all numbers in 4986.")
    print(findSum(4986))
    input("\nPress enter to proceed...")
    print('\nHere is the sum of 8')
    print(findSum(8))
    input("\nPress enter for next for find_max function...")
    print("\nHere is the highest number in [3, 4, -5, 10]")
    print(find_max([3, 4, -5, 10]))
    input("\nPress enter to proceed... ")
    print("\nHere is the highest number in [30, 4, -5, 10]")
    print(find_max([30, 4, -5, 10]))    
    input("\npress enter to proceed to maze demo.")
    demo_maze()