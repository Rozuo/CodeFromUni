print("Cmpt200F18_L2_RB.py 3048109 Ross Beaudin")
'''*****************************************************************************
CMPT200- LAB 2 - CLASSES
Section: X04L
Cmpt200

Program 1 purpose:
The purpose of this class is to create a function that can be added, subtracted,
multiplied, divided and compared (==, !=, <=, >=, <, >) with other fractions of 
the same class.

REFS: skeleton for lab 2 question 1 from blackboard by Dr. Alex Krieger, 
blackboard slides by Dr. Alex Krieger on OOP and Jon Coulson on lists.

Program 1 test output:

Cmpt200F18_L2_RB.py 3048109 Ross Beaudin
main()

Addition of 1/2 + 3/4 = 7/2 

Subtraction of 1/2 - 3/4 = 1/2 

Multiplication of 1/2 * 3/4 = 3/8 

Division of (1/2) / (3/4) = 1/2 

Is 1/2 == 3/4:  False 

Is 1/2 != 3/4:  True 

Is 1/2 < 3/4:  True 

Is 1/2 <= 3/4:  True 

Is 1/2 > 3/4:  False 

Is 1/2 >= 3/4:  False 


Program 2 purpose:
The purpose of this class is to create a deck of cards (52) with the classes 
Card() and Deck() (each card being from the class Card()). Once the deck has 
been created deck will be shuffled and compare two cards to see if they are the 
same. After that the deck will deal out n amount of cards to a hand (deck.hand).
The remaining will have less cards by the amount specified.

Program 2 test output:
Cmpt200F18_L2_RB.py 3048109 Ross Beaudin

main2()
[AS, 2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, 10S, JS, QS, KS]
[AC, 2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC]
[AH, 2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, JH, QH, KH]
[AD, 2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, JD, QD, KD]

Shuffling...

[AS, 2S, 8S, QS, 2C, 3C, 6C, 7C, 9C, 10C, 2H, 5H, 6H]
[7H, JH, 5D, 6D, 7D, 8D, 9D, QD, 8H, AH, 6S, 10D, 4C]
[7S, AC, KH, QH, 5S, 4D, JD, 3D, JS, 9H, 8C, 10S, KS]
[KD, QC, 5C, JC, 4S, 3S, 9S, AD, 3H, 2D, 4H, KC, 10H]

Is the first card the same as the second: False
Is the first card not the same as the second: True

Dealing...

This is your hand: [QD, 4C] 

Remaining deck:

[AS, 2S, 8S, QS, 2C, 3C, 6C, 7C, 9C, 10C, 2H, 5H, 6H]
[7H, JH, 5D, 6D, 7D, 8D, 9D, 8H, AH, 6S, 10D, 7S, AC]
[KH, QH, 5S, 4D, JD, 3D, JS, 9H, 8C, 10S, KS, KD, QC]
[5C, JC, 4S, 3S, 9S, AD, 3H, 2D, 4H, KC, 10H]



*****************************************************************************'''
# Code received by skeleton for lab 2 in blackboard
def gcd(x=32, y=12):
    while y:
        x, y = y, (x % y)
    return x

# Program 1
#-------------------------------------------------------------------------------

class Fraction:
    
    # initialize the function
    def __init__(self, numer, denom):
        if type(numer) == float or type(denom) == float: # Error check if there 
                                                         # is a float in one of 
                                                         # the parameters
            raise(Exception("Can only have int type for numer and denom"))
        common = gcd(numer, denom)
        self.numer, self.denom = int(numer/common), int(denom/common) # Gives a 
                                                                      # rational
    # string representation of the Fraction
    def __repr__(self):
        return(str(self.numer) + "/" + str(self.denom))
    
    # add a fraction with another fraction.
    def __add__(self, fract):             
        if isinstance(fract, Fraction) != True: # Checks if fract is from a 
                                                # fraction class
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        self.denom = fract.denom * self.denom
        self.numer = ((self.numer * fract.denom) + (fract.numer * self.denom))
        
        return(Fraction(self.numer, self.denom))
            
    # subtracts a fraction with another fraction (almost identical to __add__).
    def __sub__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        self.denom = fract.denom * self.denom
        self.numer = ((self.numer * fract.denom) - (fract.numer * self.denom))
        
        return(Fraction(self.numer, self.denom))      
    
    # multiply a fraction with another fraction.
    def __mul__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        self.numer, self.denom = (fract.numer * self.numer), (fract.denom * 
                                                              self.denom)
        return(Fraction(self.numer, self.denom))    
    
    # divide a fraction with another fraction.
    def __div__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        self.numer, self.denom = (fract.denom * self.numer), (fract.numer * 
                                                                 self.denom)
        return(Fraction(self.numer, self.denom))    
    
    # checks if a fraction is equal to another fraction and returns a bool.
    def __eq__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        return((self.numer/self.denom)==(fract.numer/fract.denom))
    
    # checks if a fraction is not equal to another fraction and returns a bool.  
    def __ne__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        return((self.numer/self.denom)!=(fract.numer/fract.denom))    
    
    # checks if a fraction is less then another fraction and returns a bool.
    def __lt__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        return((self.numer/self.denom)<(fract.numer/fract.denom))
    
    # checks if a fraction is less then or equal to another fraction and 
    # returns a bool.
    def __le__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        return((self.numer/self.denom)<=(fract.numer/fract.denom))
    
    # checks if a fraction is greater then another fraction and returns a bool.
    def __gt__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        return((self.numer/self.denom)>(fract.numer/fract.denom))
     
     # checks if a fraction is greater then or equal to another fraction and 
     # returns a bool.
    def __ge__(self, fract):
        if isinstance(fract, Fraction) != True:
            raise(Exception(
                "The inputted fraction must be under the class of 'Fraction'"))
        
        return((self.numer/self.denom)>=(fract.numer/fract.denom))


# This function tests out the class Fraction's functionality.  
def main():
    fract1 = Fraction(1, 2)
    Fraction(1,2)
    
    fract2 = Fraction(3, 4)
    
    print("\nAddition of 1/2 + 3/4 =", fract1.__add__(fract2), "\n")
    print("Subtraction of 1/2 - 3/4 =", fract1.__sub__(fract2), "\n")
    print("Multiplication of 1/2 * 3/4 =", fract1.__mul__(fract2), "\n")
    print("Division of (1/2) / (3/4) =", fract1.__div__(fract2), "\n")
    print("Is 1/2 == 3/4: ", fract1.__eq__(fract2), "\n")
    print("Is 1/2 != 3/4: ", fract1.__ne__(fract2), "\n")
    print("Is 1/2 < 3/4: ", fract1.__lt__(fract2), "\n")
    print("Is 1/2 <= 3/4: ", fract1.__le__(fract2), "\n")
    print("Is 1/2 > 3/4: ", fract1.__gt__(fract2), "\n")
    print("Is 1/2 >= 3/4: ", fract1.__ge__(fract2), "\n")
#-------------------------------------------------------------------------------

# Program 2
#-------------------------------------------------------------------------------

import random # Get access to the randint function for shuffling and dealing.

class Card:
    
    # Initialize the card class. While checking to see if the value is either
    # 1, 11, 12, 13. If it is then it will be stored to there respective card 
    # names first letter. I.E: 1 = Ace = A
    def __init__(self, value, suit):
        if value == 1:
            self._value = 'A'
        elif value == 11:
            self._value = 'J'
        elif value == 12:
            self._value = 'Q'
        elif value == 13:
            self._value = 'K'
        else:
            self._value = value
        self._suit  = suit.upper()
    
    # Show the card as if you would say it. But in abbriviated terms. 
    # I.E.: Ace of Spades = AS
    def __repr__(self):
        return str(self._value) + self._suit
    
    # Check to see if another card is the same as the current one.
    def __eq__(self, card2):
        if isinstance(card2, Card) != True: # Check to see if the other is in 
                                            # the class Card.
            raise(
                Exception("Error the inputted card is not from the card class.")
            )
        
        return ((self._value == card2._value) and (self._suit == card2._suit))
    
    # Check to see if another card is not the same as the current one.
    def __ne__(self, card2):
        if isinstance(card2, Card) != True:
            raise(
                Exception("Error the inputted card is not from the card class.")
            )        
        return ((self._value != card2._value))


class Deck:
    
    # Initialize the function by creating the deck 52 cards using the class 
    # cards
    def __init__(self):
        self._deck = []
        self.hand = []
        for i in ['S', 'C', 'H', 'D']: # Use a for loops to cycle through the 
            # suits and values A = Ace, J = Jack, Q = Queen, K = King.
            # S = spades, C = Clubs, H = Hearts, D = Diamonds
            for j in range(1, 14):
                self._deck.append(Card(j,i))
    
    # repr to display the current deck, before shuffle each card will be with 
    # there respective suits
    def __repr__(self):
        return str(self._deck[0:13]) + "\n" + str(self._deck[13:26]) + "\n" + \
               str(self._deck[26:39]) + "\n"+ str(self._deck[39:])
    
    # Shuffles the deck(list) by using import random's randint function.
    def shuffle(self):
        for i in range(len(self._deck)):
            cardChoice = random.randint(0, len(self._deck)-1) # Get a new number
            # every loop from a range of 0-52      
            self._deck.append(self._deck.pop(cardChoice)) # pop out a number 
            # from the random integer and append to the end of the list.
    
    # Deal uses a very similar code structure to shuffle but instead of the for 
    # loop going through the whole deck it goes through the specified number of 
    # cards for a hand. Once the specified number has been inputted it will pop 
    # out the card from the deck and append it to the deck.
    def Deal(self, numHand):
        for i in range(numHand):
            cardChoice = random.randint(0, len(self._deck)-1)
            self.hand.append(self._deck.pop(cardChoice))

# main2 tests out every aspect of Deck() and Card() classes.           
def main2():
    deck = Deck()
    print(deck)
    print("\nShuffling...\n")
    deck.shuffle()
    print(deck)
    print("\nIs the first card the same as the second:", 
          deck._deck[0].__eq__(deck._deck[1]))
    print("Is the first card not the same as the second:", 
          deck._deck[0].__ne__(deck._deck[1]))
    print("\nDealing...\n")
    deck.Deal(2)
    print("This is your hand:", deck.hand, "\n")
    print("Remaining deck:\n")
    print(deck)
    
#-------------------------------------------------------------------------------