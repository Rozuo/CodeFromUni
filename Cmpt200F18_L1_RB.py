print("Cmpt200F18_L1_RB.py 3048109 Ross Beaudin")
'''*****************************************************************************
CMPT200- LAB 1 - REVIEW
Section: X04L
Cmpt200

REFS: skeleton from blackboard, 
https://www.guru99.com/reading-and-writing-files-in-python.html#1
*****************************************************************************'''

# Program 1
#-------------------------------------------------------------------------------
def q1(num = "276951438"):
    # print out statment.
    print("\nQ1. Magic Square Checker\n")
    print(num[:3] + '\n' + num[3:6] + '\n' + num[6:])
    
    # Convert the string into a list of integers.
    numList = []
    for i in num:
        numList.append(int(i))
    
    # Check if the sum of the rows are the same for each. 
    # If true then the rest should equal to the exact same sum.
    if (sum(numList[:3]) == sum(numList[3:6]) or sum(numList[3:6]) ==\
       sum(numList[6:]) or sum(numList[:3]) == sum(numList[6:])):
        print("\nThis is a magic square.")
    else:
        print("\nThis is not a magic square.")
    
    input("Q1 Done. Press ENTER  ...")
#-------------------------------------------------------------------------------
    
# Program 2
#-------------------------------------------------------------------------------
# can only take string in parameter symbol.
def q2(symbol = '*', line = 4):
    print("Q2. Triangle Creator\n")
    # Check if there is multiple symbols
    if len(symbol) > 1:
        symbol = symbol[0]
    # print out the triangle
    for i in range(line):
        print((" "*(line-i)), end = "")
        for j in range(0, i+1):
            print((symbol + " "), end = "")
        print()

    input("Q2 Done. PRess ENTER ...")
#-------------------------------------------------------------------------------

# Program 3
#-------------------------------------------------------------------------------

def q3(string):
    listPunctuation = ['.', ',', '/', '"', ';', ':', '!', '?']
    
    # Remove punctuation
    for i in listPunctuation:
        string = string.split(i)
        string = "".join(string)
    string = string.split()
    
    input("Q3 Done. Press Enter ...")
    
    return string
#-------------------------------------------------------------------------------

# Program 4
#-------------------------------------------------------------------------------

def q4(fileName = "Q4.txt"):
    print("\nQ4. Split String from Text File")
    file = open("Q4.txt","r")
    string = file.read()
    string = q3(string)
    string = " ".join(string)
    newFile = open("newQ4.txt", "w+")
    newFile.write(string)
    file.close()
    newFile.close()

    input("Q4. Done, press enter ...")
#-------------------------------------------------------------------------------

# main function runs all the previously made question function
def main():
    q1()
    q1('123456789')
    q2()
    q2('X', 8)
    q3("A tall-ish wall, with trim. I don't want to paint it;")
    q4()