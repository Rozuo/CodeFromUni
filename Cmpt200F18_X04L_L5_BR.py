print("Cmpt200F18_X04L_L5_BR.py 1.00 3048109 Ross Beaudin")
'''*****************************************************************************
CMPT200- LAB 5 - Linked List
Section: X04L
Cmpt200

This shipyard function will simulate how a shipyard would function in it's base 
fundamentals. You may add a package, ship off all shipping containers. Look for 
specific packages or ID's and remove remove those specific packages. And look 
show all shipping containers/containers heading to specific destination/shipping 
containers and there contents.

REFS: 
Lecture slides on Linked lists by Alex Kreiger
Lab 4 linkedqueue program
Lab 5 skel.py program
Lectures presented by Alex Kreiger
*****************************************************************************'''
# This class is to define the contents within a container.
class Package:
    
    def __init__(self, name, dest, weight, idNum):
        self._name   = name
        self._dest   = dest
        self._weight = weight
        self._idNum  = idNum
        
    def __repr__(self):
        return self._name + " " + self._dest + " " + str(self._weight) + " "\
               + self._idNum
    
    def __gt__(self, pkg):
        return (self._weight > pkg._weight)

    def demo():
        print("Package.demo():")
        pkg1 = Package('Sam', 'England', 456, '002')
        pkg2 = Package('June', 'France', 123, '003')
        print("Here are the packages:", pkg1, "\n"+ pkg2)
        print("pkg1 > pkg2:", pkg1 > pkg2)
    
class Container:
    
    class _Node:
        def __init__(self, pkg, nex):
            self._pkg  = pkg
            self._nex  = nex
    
    def __init__(self, dest):
        self._dest = dest
        self._first = None
        self._totalWeight = 0
        self._size        = 0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def insert(self, pkg) :  
        # See if the new element will be inserted as _first.
        if self.isEmpty() or pkg > self._first._pkg :
            self._first = self._Node(pkg, self._first)
            self._size += 1
            self._totalWeight += pkg._weight
            return
        
        # Find insertion point: advance til we hit end of list or next element
        # is strictly greater than the one to insert
        tmpRef = self._first
        while tmpRef._nex != None and pkg._weight <= tmpRef._nex._pkg._weight:
            tmpRef = tmpRef._nex
        
        tmpRef._nex = self._Node(pkg, tmpRef._nex)
        self._size += 1  
        self._totalWeight += pkg._weight
    
    def __repr__(self):
        s = "\n"
        tempVar =  self._first
        # utilize a loop to fix this problem
        while tempVar != None:
            if tempVar._nex == None:        # An if statment to terminate the 
                s += str(tempVar._pkg)      # loop at the last item within the 
                break                       # container and too prevent an extra
            s += str(tempVar._pkg) + " -> " # arrow.
            tempVar = tempVar._nex
        s += "\nTotal weight: " + str(self._totalWeight)
        return s
    
    def __eq__(self, container):
        return self._dest == container._dest
    
    def demo():
        p1 = Package('June', 'France', 456, '003')
        p2 = Package('Sam', 'England', 123, '002')
        c1 = Container("ENGL")
        print("inserting packages...")
        c1.insert(p1)
        c1.insert(p2)
        print("Current container: ", c1)
    
class Shipyard:
    
    pkg_id = '001'
    
    class _Node:
        
        def __init__(self, cont, nex = None):
            self._cont = cont
            self._nex  = nex
    
    def __init__(self, port):
        self._port = port
        self._start = None
        self._size = 0
        self._pkgId = '001'
        
    def __repr__(self):
        s = ""
        tempVar = self._start
        while self._start != None:
            pass
    
    def isEmpty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    # This function is for inserting any new containers we may need incase the 
    # weight exceeds 2000 lbs. Using a similar method to the previous insert 
    # function from the Container class.
    def insert(self, cont):
        if cont._dest.upper() < self._start._cont._dest.upper():
            self._start = self._Node(cont, self._start)
            print(self._start._nex._cont)
            return
        
        tempVar = self._start
        while tempVar._nex != None and \
              cont._dest.upper() >= tempVar._cont._dest.upper(): 
            tempVar = tempVar._nex
        tempVar._nex = self._Node(cont, tempVar._nex)
        self._size += 1
    
    def add(self, owner, dest, weight):
        
        print("\nSending pkg from", owner, "to", dest, ',', weight, "lbs")
        package = Package(owner, dest, weight, self._pkgId) # Establish package 
                                                           # into package class.
        
        # Increase the package ID for the next package to be added.
        self._pkgId = '00' + str(int(self._pkgId) + 1)
        
        if self.isEmpty():
            print("First package and container will be established")
            container = Container(package._dest)
            container.insert(package)
            self._start = self._Node(container, self._start)
            self._size += 1
            return
        
        tempVar = self._start
        
        # If there is only one container in the shipyard proccess the package 
        # without traversing through the linked list.        
        if tempVar._nex == None:
            if tempVar._cont._dest.upper() == package._dest.upper() and \
               ((tempVar._cont._totalWeight + package._weight) <= 2000):
                print("inserting a new package into an existing container.")
                tempVar._cont.insert(package)
                self._size += 1
                return
            
            # If the container has a total weight higher then 2000lbs and a 
            # container already exists. Create another container and insert the
            # package. and check to see if another container already exist while
            # making sure it is not none.
            elif tempVar._cont._dest.upper() == package._dest.upper() and \
                 ((tempVar._cont._totalWeight + package._weight) >= 2000) and \
                 (tempVar._nex != None and tempVar._nex._cont._dest.upper() !=\
                  package._dest.upper()):
                print("Creating new container due to maxed out weight.")
                container = Container(package._dest)
                self.insert(container)
                container.insert(package)
                self._size += 1
                return        
        
        # If there is multiple containers in the shipyard. Traverse through the 
        # linked list and insert the package in it's respective container.
        while tempVar._nex != None:
            
            # If the container has a total weight lower then 2000lbs and already
            # exists. Insert the package to the container.
            if (tempVar._cont._dest.upper() == package._dest.upper()) and \
               ((tempVar._cont._totalWeight + package._weight) <= 2000):
                print("inserting a new package into an existing container.")
                tempVar._cont.insert(package)
                self._size += 1
                return
            
            # If the container has a total weight higher then 2000lbs and a 
            # container already exists. Create another container and insert the
            # package.
            elif (tempVar._cont._dest.upper() == package._dest.upper()) and \
                 ((tempVar._cont._totalWeight + package._weight) >= 2000) and\
                 ((tempVar._nex._cont._dest.upper() != package._dest.upper())):
                print("Creating new container due to maxed out weight.")
                container = Container(package._dest)
                self.insert(container)
                container.insert(package)
                self._size += 1
                return
            
            tempVar = tempVar._nex
        
        # If there is no container going to the packages destnation insert 
        # create a new one and insert the package.     
        print("container doesn't exist creating new one")
        container = Container(dest)
        container.insert(package)
        self.insert(container)
        self._size += 1
        return
        
    #prints manifest of whole system
    def printAll(self):
        if self.isEmpty():
            print("Nothing is in this shipyard. Please "+\
                  "come back when packages are inserted.")
            return
        
        s = ''
        tempVar = self._start
        while tempVar._nex != None:
            s += "\nTo " + tempVar._cont._dest + " : "
            s += tempVar._cont.__repr__() + "\n"
            tempVar = tempVar._nex
        return print(s)
            
    #prints manifest of a single destination
    def printDest(self, dest):
        if self.isEmpty():
            print("Nothing is in this shipyard. Please "+\
                  "come back when packages are inserted.")
            return
        
        s = ''
        tempVar = self._start
        while tempVar._nex != None:
            if tempVar._cont._dest == dest:
                s += "\nTo " + tempVar._cont._dest + " : "
                s += tempVar._cont.__repr__() + "\n"
            tempVar = tempVar._nex
        return print(s)
    
    #prints container info list
    def printContainers(self):
        if self.isEmpty():
            print("Nothing is in this shipyard. Please "+\
                  "come back when packages are inserted.")
            return
        
        s = ''
        tempVar = self._start
        while tempVar._nex != None:
            s += "\nTo " + tempVar._cont._dest + " : "
            s += str(2000 - tempVar._cont._totalWeight) + \
                " Weight left before maximum capacity.\n"
            tempVar = tempVar._nex
        return print(s)
    
    def remove(self, own, dest, weight):
        if self.isEmpty():
            print("Nothing is in this shipyard. Please "+\
                  "come back when packages are inserted.")
            return
        if self.search(own, dest, weight) != True:
            print("The package is no where to be found in the shipyard.")
            return
        
        s = ''
        tempVar = self._start
        tempPkgVar = None           # create a temp pkg variable
        tempPkgParVar = None        # create a temp parent pkg variable
        while tempVar._nex != None: 
            if tempVar._cont._dest.upper() == dest.upper():
                # If the first package in the container is the specified 
                # variable remove it.
                if tempVar._cont._first._pkg._name.lower() == own.lower() and \
                   tempVar._cont._first._pkg._weight == weight:
                    tempVar._cont._first = tempVar._cont._first._nex
                    print("Removing specified package.")
                    return
                
                # Get a variable that will be the next item within the LL and 
                # get the item that preceeds it. Once the name and the weight 
                # match the package shall be removed by using the parents nex 
                # value to become the nex nex variable.
                tempPkgVar = tempVar._cont._first._nex
                tempPkgParVar = tempVar._cont._first
                while tempPkgVar._nex != None:
                    if tempPkgVar._pkg._name.lower() == own.lower() and \
                       tempPkgVar._pkg._weight == weight:                    
                        tempPkgParVar._nex = tempPkgVar._nex
                        print("Removing specified package.")
                        return
                    tempPkgVar = tempPkgVar._nex
                    tempPkgParVar = tempPkgParVar._nex
                    
                # If the last value is None check one more time to unsure the 
                # package is not present.
                if tempPkgVar._pkg._name.lower() == own.lower() and \
                   tempPkgVar._pkg._weight == weight:                    
                    tempPkgParVar._nex = tempPkgVar._nex
                    print("Removing specified package.")
                    return     
                
            tempVar = tempVar._nex
        
        print("The Specified package is no where to be found or has been " + \
              "already removed.")
                        
    
    def removeByID(self, idNum):
        if self.isEmpty():
            print("Nothing is in this shipyard. Please "+\
                  "come back when packages are inserted.")
            return
        
        # If the package cannot be found we're done.
        if self.searchID(idNum) != True:
            print("The package is no where to be found in the shipyard.")
            return
                
        s = ''
        tempVar = self._start
        tempPkgVar = None
        tempPkgParVar = None
        # Go through every single container and pkg to locate the Id Number.
        while tempVar._nex != None:
            tempPkgVar = tempVar._cont._first._nex
            tempPkgParVar = tempVar._cont._first
            # check if it's the first item within the current contaire
            if tempVar._cont._first._pkg._idNum == idNum:
                    tempVar._cont._first = tempVar._cont._first._nex
                    print("Removing specified package.")
                    
            # cycle through the current container to locate the package
            while tempPkgVar._nex != None:
                if tempPkgVar._pkg._idNum == idNum:
                    print("Deleting package.")
                    tempPkgParVar._nex = tempPkgVar._nex
                    return
                tempPkgVar = tempPkgVar._nex
                tempPkgParVar = tempPkgParVar._nex
            
            # Final check for the last item.
            if tempPkgVar._pkg._idNum == idNum:
                tempPkgParVar._nex = tempPkgVar._nex
                return
            tempVar = tempVar._nex
        print("The Specified package is no where to be found.")
        
    
    def search(self, own, dest, weight):
        if self.isEmpty():
            print("Nothing is in this shipyard. Please "+\
                  "come back when packages are inserted.")
            return
        
        s = ''
        tempVar = self._start
        tempPkgVar = None           # create a temp pkg variable
        while tempVar._nex != None: 
            if tempVar._cont._dest.upper() == dest.upper():
                # If the first package in the container is the specified 
                # variable remove it.
                if tempVar._cont._first._pkg._name.lower() == own.lower() and \
                   tempVar._cont._first._pkg._weight == weight:
                    print("Package found.")
                    return True
                
                # Get a variable that will be the next item within the LL and 
                # get the item that preceeds it. Once the name and the weight 
                # match the package shall be removed by using the parents nex 
                # value to become the nex nex variable.
                tempPkgVar = tempVar._cont._first._nex
                while tempPkgVar._nex != None:
                    if tempPkgVar._pkg._name.lower() == own.lower() and \
                       tempPkgVar._pkg._weight == weight:                    
                        print("Package found.")
                        return True
                    tempPkgVar = tempPkgVar._nex
                    
                # If the last value is None check one more time to unsure the 
                # package is not present.
                if tempPkgVar._pkg._name.lower() == own.lower() and \
                   tempPkgVar._pkg._weight == weight:                    
                    print("Package found.")
                    return True     
                
            tempVar = tempVar._nex
        
        print("The Specified package is no where to be found.")
        return False
    
    def searchID(self, idNum):
        if self.isEmpty():
            print("Nothing is in this shipyard. Please "+\
                  "come back when packages are inserted.")
            return
        
        s = ''
        tempVar = self._start
        tempContVar = None
        # Go through every single container and pkg to locate the Id Number.
        while tempVar._nex != None: 
            tempContVar = tempVar._cont._first
            # Cycle through current container.
            while tempContVar._nex != None:
                if tempContVar._pkg._idNum == idNum:
                    print("Package found.")
                    return True
                tempContVar = tempContVar._nex
            tempVar = tempVar._nex
        print("The Specified package is no where to be found.")
        return False
    
    def ship(dest):
        self._start = None
        print("All containers have been shipped.")
    
    def demo():
        global sy
        from random import shuffle
        sy = Shipyard('Edmonton')
        pkgList = [ ('Jim', 'AFR', 750), ('Sam', 'AFR', 450), 
                    ('Bob', 'AFR', 300), ('Fil', 'ENG', 750),
                    ('Wil', 'ENG', 650), ('Jil', 'ENG', 300), 
                    ('Lil', 'ENG', 200), ('Sue', 'ENG', 500), 
                    ('Rik', 'ENG', 450), ('Jan', 'ENG', 350) ]
        shuffle(pkgList)
        print("Package list:", pkgList, '\n')
        for pkg in pkgList:
            sy.add(*pkg) 
            
        input("\nPress enter to printAll items in the shipyard... ")
        print("\n\n\nPrinting the entire shipyard:")
        sy.printAll()
        
        input("\nPress enter to print all items heading to ENG items in the" + \
              " shipyard... ")
        print("\n\n\nPrinting all containers going to ENG:")
        sy.printDest('ENG')
        
        input("\nPress enter to printAll containers with there remaining" + \
              " weight capacity in the shipyard... ")
        print("\n\n\nPrinting all containers with there remaining capacity:")
        sy.printContainers()
        
        input("\nPress enter to search in the shipyard... ")
        print("\n\n\nLocating Jim's package heading to AFR.")
        sy.search('Jim', 'AFR', 750)
        
        input("\nPress enter to search by ID in the shipyard... ")
        print("\n\n\nLocating package 002.")
        sy.searchID("002")
        
        input("\nPress enter to remove an items by ID in the shipyard... ")
        print("\n\n\nRemoving package 002.")
        sy.removeByID('002')
        sy.printAll()
        
        input("\nPress enter to remove a package by specifications" +\
              " in the shipyard... ")
        print("\n\n\nRemoving Bob's package heading to AFR.")
        sy.remove('Bob', 'AFR', 300)
        sy.printAll()
        
        input("\nPress enter to ship out all containers and packages...")
        print("\n\n\nShipping all containers.")
        sy.ship()
        sy.printAll()
        
if __name__ == "__main__":
    if input("Package demo? y/n: ").lower() == 'y':
        Package.demo()
    if input("Container demo? y/n: ").lower() == 'y':
        Container.demo()
    if input("Shipyard demo? y/n: ").lower() == 'y':
        Shipyard.demo()        