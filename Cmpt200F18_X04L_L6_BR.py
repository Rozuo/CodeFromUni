print("Cmpt200F18_X04L_L6_BR.py 1.00 3048109 Ross Beaudin")
'''*****************************************************************************
CMPT200- LAB 6 - World Tree
Section: X04L
Cmpt200

This program will process a text file. It will output a binary search tree of 
the words in the file as well as their frequencies. We will be able to search 
for specific words in the file and determine if they exist or not.

REFS: 
Lecture slides on Linked lists by Alex Kreiger
WordCounter.py program from blackboard
BinarySearchTree.py program from blackboard

EXAMPLE OUTPUT:

Cmpt200F18_X04L_L6_BR.py 1.00 3048109 Ross Beaudin
Word Tree Function

Totale of words: 27 
Number of unique words processed: 15
and: 3
close: 2
de: 4
deal: 1
down: 1
drove: 1
hill: 2
jack: 2
jill: 2
moon: 1
ran: 1
see: 2
ski: 1
to: 2
up: 2

Is up in the tree: True
up: 2 
Percentage out of total words: 7.4074074074074066%

Press enter for Text_short.txt example...

File example: Text_short.txt
Word Tree Function

Totale of words: 64 
Number of unique words processed: 15
1967: 8
american: 4
analysis: 4
and: 4
classic: 4
computational: 4
english: 4
francis: 4
in: 4
kucera: 4
of: 4
present-day: 4
published: 4
their: 4
work: 4

Is their in the tree: True
their: 4 
Percentage out of total words: 6.25%

Press enter for Text.txt example...

File example: Text.txt
Word Tree Function

Totale of words: 724 
Number of unique words processed: 364
0-395-32250-2: 1
1/n: 1
100: 1
1014312: 1
15: 2
1961: 3
1967: 2
1969: 1
1983: 1
2000: 2
3%: 1
500: 1
50000: 1
7%: 1
80: 1
a: 17
about: 4
above: 1
acoustics: 1
across: 1
additionally: 1
after: 2
all: 1
also: 1
although: 1
american: 5
among: 1
amount: 1
an: 1
analyses: 1
analysis: 5
anatomy: 1
and: 21
andrew: 1
another: 1
anthropology: 1
appeared: 1
appears: 1
applied: 1
approach: 1
approached: 2
are: 2
article: 1
artistic: 1
as: 11
asterisk: 1
at: 1
base: 1
basic: 1
basis: 1
be: 4
been: 1
began: 1
being: 1
biology: 1
bits: 1
boston: 1
both: 1
boundary: 1
british: 1
brown: 6
but: 2
by: 6
can: 1
capitals: 1
carefully: 1
carried: 1
cases: 1
categories: 1
chosen: 1
citation: 1
classic: 1
codes: 1
combining: 1
commonly: 1
compiled: 3
compound: 1
computational: 3
computer: 1
concerned: 1
considerably: 1
consists: 1
constitutes: 1
contained: 1
continued: 1
contractions: 1
corpora: 2
corpus: 16
could: 1
current: 1
data: 1
decreasing: 1
defined: 1
describe: 1
determined: 1
dictionary: 3
directions: 1
disciplines: 1
distributed: 1
diverse: 1
done: 1
drawn: 1
draws: 1
each: 4
either: 1
elements: 1
enabled: 1
english: 6
entry: 1
error: 1
even: 1
example: 2
extensive: 1
extraordinary: 1
far: 2
few: 2
field: 6
fields: 1
first: 5
following: 1
for: 10
foreign: 1
formed: 1
forms: 1
formulae: 1
francis: 3
frequency: 4
frequent: 1
from: 6
general: 1
genres: 2
george: 1
grabbed: 1
graduate: 1
grammar: 1
graphing: 1
great: 1
greene: 1
ground-breaking: 1
groups: 1
had: 2
half: 1
hapax: 1
has: 1
have: 1
helped: 1
henry: 1
heritage: 1
high: 1
his: 1
houghton: 1
houghton-mifflin: 1
human: 1
hyperbola: 1
identifier: 1
in: 16
indicated: 1
indicators: 1
influence: 1
informatics: 1
information: 1
initial: 1
intellectual: 1
interesting: 1
international: 1
is: 8
isbn: 1
it: 5
items: 1
its: 2
january: 1
just: 1
keypunch: 1
kingsley: 1
known: 2
kucera: 4
lancaster-oslo/bergen: 1
language: 5
languages: 3
large: 1
larger: 1
later: 1
law: 1
led: 1
legomena: 1
lexicon: 1
lexicostatistical: 1
linguist: 1
linguistic: 1
linguistics: 6
literary: 1
literature: 1
location: 1
machines: 1
mackie: 1
manual: 1
many: 3
meant: 1
methodologies: 1
mifflin: 1
million: 3
miscounts: 1
more: 2
most: 1
most-cited: 1
much: 2
n-th: 1
narrowly: 1
national: 1
native: 1
nearly: 1
nelson: 1
neuroscience: 1
new: 2
noted: 1
now: 1
number: 1
occur: 1
occurrence: 1
of: 35
on: 4
once: 1
one: 1
only: 3
opus: 1
or: 5
order: 2
original: 1
originally: 1
other: 4
out: 1
outside: 2
over: 1
part: 1
part-of-speech: 1
particular: 1
parts: 1
pathology: 1
people: 1
phenomena: 2
philosophy: 1
pioneered: 1
plus: 1
preceding: 1
present-day: 1
program: 1
proofreading: 1
proportion: 1
proportional: 1
provided: 1
psychobiology: 1
psychology: 2
publication: 1
published: 4
publisher: 1
quite: 1
random: 1
rank-vs-frequency: 1
rate: 1
refer: 1
related: 1
relationship: 1
relevant: 1
required: 1
resources: 1
result: 1
rich: 1
rough: 1
roughly: 1
rubin: 1
sample: 1
sampled: 2
samples: 3
science: 1
scientific: 1
see: 2
selection: 2
semiotics: 1
sentence: 1
sentence-boundary: 1
several: 1
shortly: 1
shows: 1
signs: 1
simple: 1
simply: 1
sociology: 2
some: 1
someone: 1
sophisticated: 1
sources: 1
speak: 1
speakers: 1
special: 3
speech: 2
speech-language: 1
statistical: 1
statistics: 2
strange: 1
student: 1
studies: 1
study: 5
subjected: 1
such: 4
supply: 1
symbols: 1
tagged: 2
tagging: 2
tags: 1
tend: 1
term: 1
text: 2
than: 1
that: 3
the: 42
their: 1
themselves: 1
then: 1
theorists: 1
they: 2
this: 4
those: 1
three-line: 1
thus: 1
to: 15
today: 1
total: 1
totaling: 1
typical: 1
under: 2
unit: 1
up: 1
upper-case: 1
usage: 1
use: 1
used: 4
uses: 1
using: 1
variegated: 1
variety: 4
various: 1
very: 2
vocabulary: 2
was: 6
well: 1
were: 6
what: 1
which: 3
while: 1
who: 2
wide: 1
widely: 1
wikipedia: 1
winthrop: 1
with: 1
within: 1
word: 3
words: 10
work: 2
works: 1
written: 1
years: 2
zipf: 1
zipf's: 1

Is forms in the tree: True
forms: 1 
Percentage out of total words: 0.13812154696132595%
*****************************************************************************'''

from random import randint

testString = '''Jack and Jill drove up de hill to see de moon up close and Jack 
see Jill ski down de hill and ran de deal to close.'''

class WordCounter :
    def __init__(self, word, count = 1) :
        self._word = word
        self._count = count
       
    def __repr__(self):
        return self._word + ': ' + str(self._count)
    
    def __str__(self) :
        return self._word + ": " + str(self._count)
    def __eq__(self,y) :
        return self._word == y._word
    def __ne__(self,y) :
        return not self == y
    def __gt__(self,y) :
        return self._word > y._word
    def __ge__(self,y) :
        return self == y or self > y
    def __lt__(self,y) :
        return not (self >= y)
    def __le__(self,y) :
        return not (self > y)
    
    def increment(self) :
        self._count += 1

class WordTree:
    class _Node :
        def __init__(self, value, left = None, right = None) :
            self._value = value
            self._left = left
            self._right = right
    
    def __init__(self, file = None) :
        self._root = None
        self._size = 0        # The unique words in the tree
        self._totalWords = 0  # Total words in the tree
        if file != None:
            if file.endswith('.txt') != True: # Check to see if it's a text file
                raise(Exception("Error! The file is not a .txt"))
            else:
                self.fileInputed(file)  # Run and test the files contents.
    
    # This function doubles as a demo function and opens the file
    def fileInputed(self, file):
        self._file = open(file, "r")
        self._fileContents = self._file.read()
        self._file.close()
        
        print("Word Tree Function")
        listString = self._fileContents.split()
        wordTree = WordTree()
        tempVar = None
        newListString = []              # new list for all words with  
        for word in listString:         # punctutaions removed or not present
            for punc in [',', '.', '?', '!', ':', ';', '(', ')', '"']:
                tempVar = list(word)
                for var in tempVar:
                    if var == punc:
                        tempVar.remove(punc) # Remove punctuations
                        word = "".join(tempVar)
            newListString.append(word)   # append the word without punctutation.
            wordCounter = WordCounter(word.lower())
            wordTree.insert(wordCounter)
            
        print("\nTotale of words:", wordTree._totalWords, \
              "\nNumber of unique words processed:", wordTree._size)
        wordTree.inOrder()   # Prints out the list of words.
        randomNum = randint(0, len(newListString)-1) # Pick a random number to 
        wordCount = WordCounter(newListString[randomNum].lower()) # select from 
        print("\nIs", wordCount._word, "in the tree: ", end = "")#newListString.
        
        # If the word is present in the binary tree print out true and it's 
        if wordTree.search(wordCount) != None: # specification with the  
            print(True)                  # percentage of it's presence within 
                                         # the string/file. Else false.
            print(wordTree.search(wordCount)._value, \
                  "\nPercentage out of total words:", \
                  str((wordTree.search(wordCount)._value._count / \
                   wordTree._totalWords) * 100)+"%")
        else:
            print(False)
        
    # This repr is what I call a dummy magic function. This repr will output 
    # nothing and it's only purpose is to prevent unnecessary address outputs.
    def __repr__(self):
        return ""
    
    def __len__(self):
        return self._size
    
    def isEmpty(self) :
        return self._root == None
    
    def search(self, value) :
        probe = self._root
        while (probe != None) :
            if value == probe._value :
                return probe
            if value <= probe._value :
                probe = probe._left
            else :
                probe = probe._right
        return None     
    
    
    def insert(self, value) :
        if self.isEmpty() :
            self._root = self._Node(value)
            self._size += 1
            self._totalWords += 1
            return
        parent = None # to keep track of parent
        # we need above information to adjust 
        # link of parent of new ndoe later
        
        probe = self._root
        while (probe != None) :
            if value._word == probe._value._word: # If the word is already 
                probe._value.increment() # present in the binary tree increase 
                self._totalWords += 1  # that words counter and return nothing.
                return
            if value <= probe._value :#go to left tree
                parent = probe#before we go to child, save parent
                probe = probe._left
            else :#go to right tree
                parent = probe#before we go to child, save parent
                probe = probe._right
        if (value <= parent._value) :#new value will be new left child
            parent._left = self._Node(value)
            self._size += 1
            self._totalWords += 1
        else :#new value will be new right child
            parent._right = self._Node(value)
            self._size += 1
            self._totalWords += 1
    
    
    def delete(self, value) :
        parent = None
        probe = self._root
        while(probe != None) :
            if value == probe._value :
                break
            if value < probe._value :
                parent = probe
                probe = probe._left
            else :
                parent = probe
                probe = probe._right
        if probe == None :
            raise NotPresent("Attempt to delete nonexistent value.")
        # At this point, probe points at the node to be deleted and 
        # parent to the parent of this node.
        if (probe._left != None and probe._right != None):
            # Two children present; find the successor
            parentSu = probe
            su = probe._right#WE'LL LOOK FOR LEFTMOST IN RIGHT SUBTREE
            while (su._left != None) :
                parentSu = su
                su = su._left
            # At this point, su points to the successor of probe
            # Copy su value to probe value and delete node su
            probe._value = su._value
            if parentSu == probe :#if su is child of probe then su has no left child (loop was not executed)
                parentSu._right = su._right#bypass su
            else :#su has right child and loop was executed
                parentSu._left = su._right#
            return
        # We are in the case 0 or 1 child
        newChild = probe._left
        if newChild == None : newChild = probe._right
        if parent == None :
            # We are deleting the root
            self._root = newChild
        else:
            if probe == parent._left:
                parent._left = newChild
            else:
                parent._right = newChild
                
    def inOrder(self) :
        self.recInOrder(self._root)
        
    def recInOrder(self,node) :
        if node == None : return
        self.recInOrder(node._left)
        print(node._value)
        self.recInOrder(node._right)            
        
class NotPresent(Exception) :
    pass

def main():
    print("Word Tree Function")
    listString = testString.split() # Split the test string from the top of the
    wordTree = WordTree()           # program
    tempVar = None
    newListString = []              # new list for all words with punctutaions 
    for word in listString:         # removed or not present
        for punc in [',', '.', '?', '!', ':', ';', '(', ')', '"']:
            tempVar = list(word)
            for var in tempVar:
                if var == punc:
                    tempVar.remove(punc) # Remove punctuations
                    word = "".join(tempVar)
        newListString.append(word)   # append the word without punctutation.
        wordCounter = WordCounter(word.lower())
        wordTree.insert(wordCounter)
        
    print("\nTotale of words:", wordTree._totalWords, \
          "\nNumber of unique words processed:", wordTree._size)
    wordTree.inOrder()   # Prints out the list of words.
    randomNum = randint(0, len(newListString)-1) # Pick a random number to 
    wordCount = WordCounter(newListString[randomNum].lower()) # select from 
    print("\nIs", wordCount._word, "in the tree: ", end = "") # newListString.
    
    # If the word is present in the binary tree print out true and it's 
    if wordTree.search(wordCount) != None: # specification with the percentage 
        print(True)                  # of it's presence within the string/file.
        print(wordTree.search(wordCount)._value, \
              "\nPercentage out of total words:", \
              str((wordTree.search(wordCount)._value._count / \
               wordTree._totalWords) * 100)+"%")
    else:
        print(False)
    
    # Run the other examples.
    input("\nPress enter for Text_short.txt example...")
    print('\nFile example: Text_short.txt')
    WordTree("Text_short.txt")
    
    input("\nPress enter for Text.txt example...")
    print('\nFile example: Text.txt')
    WordTree("Text.txt")    
    
if __name__ == '__main__':
    main()