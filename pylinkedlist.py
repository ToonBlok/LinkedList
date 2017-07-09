import unittest

class LinkedList():
    # 50, 15, 10
    # insert at 1
    # prev needs new connection to new node
    # new node needs connection to 10
    def insertAt(self, pos, node):
        if pos < 0:
           raise IndexError("Value given out of range") 
        elif self.head == None and pos > 0: # list.count() = ? and pos is out of range
           raise IndexError("Value given out of range") 
        elif self.head == None and pos == 0: # List.count() = 0 and pos = 0
           self.head = node
        elif pos == 0: # List.count() = 0 and pos = 0
            node.next = self.head 
            self.head = node
        else:
            count = 0
            currentNode = self.head 

            while currentNode.next != None:
                prevNode = currentNode
                currentNode = currentNode.next
                count += 1
                if pos == count:
                    currentNode = node.next
                    prevNode.next = node 












        ## I want to insert at pos higher than 0, but 0 doesn't exist
        #if self.head == None and pos != 0:
        #   raise IndexError("Value given out of range") 
        #elif self.head == None and pos == 0:
        #   self.head = node
        #else:
        #    count = 0
        #    currentNode = self.head 

        #    while currentNode.next != None:
        #        prevNode = currentNode
        #        currentNode = currentNode.next
        #        count += 1
        #        if pos == count:
        #            currentNode = node.next
        #            prevNode.next = node 

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            currentNode = self.head 

            while currentNode.next != None:
                currentNode = currentNode.next

            currentNode.next = node

    def prepend(self, node):
        if self.head == None:
            self.head = node
        else:
            remember = self.head 
            self.head = node
            self.head.next = remember

    def logAll(self):
        if self.head == None:
            print ""
        else:
            currentNode = self.head 
            print self.head.getData()

            while currentNode.next != None:
                currentNode = currentNode.next
                print currentNode.getData()

    def count(self):
        count = 0

        if self.head == None:
            return count 
        else:
            currentNode = self.head 
            count += 1

            while currentNode.next != None:
                currentNode = currentNode.next
                count += 1

            return count

    def getValueAt(self, pos):
        if pos < 0:
           raise IndexError("Value given out of range") 

        count = 0

        if self.head == None:
            return "Invalid position given"
        else:
            currentNode = self.head 
            if pos == count:
                return self.head.getData()
            else:
                while currentNode.next != None:
                    count += 1
                    currentNode = currentNode.next
                    if pos == count:
                        return currentNode.getData()
                # If pos is STILL higher than max count reached, it is out of range
                if pos > count:
                   raise IndexError("Value given out of range") 

    def clear(self):
        if self.head != None:
            self.head = None
           
    def removeAt(self, pos):
        if pos < 0:
           raise IndexError("Value given out of range") 

        count = 0

        if self.head == None:
           raise IndexError("Value given out of range") 
        else:
            if pos == 0 and self.head.next == None:
                self.head = None
            elif pos == 0:
                head = currentNode.next 
            else:
                currentNode = self.head 

                while currentNode.next != None:
                    prevNode = currentNode
                    currentNode = currentNode.next
                    count += 1
                    if pos == count:
                        address = currentNode.next
                        prevNode.next = address

                # If pos is STILL higher than max count reached, it is out of range
                if pos > count:
                   raise IndexError("Value given out of range") 

    def __init__(self):
        self.head = None

class Node():

    def __init__(self, data):
        self.next = None
        self.data = data 

    def getData(self):
       return self.data

mll = LinkedList()
mll.append(node = Node(15))
mll.append(node = Node(45))
mll.insertAt(1, node = Node(25))
mll.logAll()
