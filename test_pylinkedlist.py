import pylinkedlist
import pytest

class TestAppend:
    linkedList = None
        
    def setup(self):
        TestAppend.linkedList = pylinkedlist.LinkedList()

    # Evaluates whether append insert a value at the end of the linked list.
    def test_append(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        TestAppend.linkedList.append(node = pylinkedlist.Node(31))
        TestAppend.linkedList.append(node = pylinkedlist.Node(11))
        expectedOrder = [21, 31, 11, 91]
        
        # act
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))

        actualOrder = [
            TestAppend.linkedList.getValueAt(0),
            TestAppend.linkedList.getValueAt(1),
            TestAppend.linkedList.getValueAt(2),
            TestAppend.linkedList.getValueAt(3),
        ]

        # assert
        assert expectedOrder == actualOrder

    # Evaluates whether prepend insert a value at the beginning of the linked list.
    def test_prepend(self):
        # arrange 
        TestAppend.linkedList.prepend(node = pylinkedlist.Node(10))
        TestAppend.linkedList.prepend(node = pylinkedlist.Node(20))
        TestAppend.linkedList.prepend(node = pylinkedlist.Node(30))
        expectedOrder = [40, 30, 20, 10]
        
        # act
        TestAppend.linkedList.prepend(node = pylinkedlist.Node(40))

        actualOrder = [
            TestAppend.linkedList.getValueAt(0),
            TestAppend.linkedList.getValueAt(1),
            TestAppend.linkedList.getValueAt(2),
            TestAppend.linkedList.getValueAt(3),
        ]

        # assert
        assert expectedOrder == actualOrder

    # Evaluates whether this method is able to retrieve the value of the last node. 
    def test_last(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(10))
        TestAppend.linkedList.append(node = pylinkedlist.Node(20))
        TestAppend.linkedList.append(node = pylinkedlist.Node(30))
        
        # act
        lastNode = TestAppend.linkedList.last()

        # assert
        assert lastNode.data == 30

    # Evaluates whether this method is able to retrieve the value of the a specific node and whether the list handles index out of range exception.
    def test_getValueAt(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))
        TestAppend.linkedList.append(node = pylinkedlist.Node(51))
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        TestAppend.linkedList.append(node = pylinkedlist.Node(11))
        TestAppend.linkedList.append(node = pylinkedlist.Node(81))
        
        # act
        valOne = TestAppend.linkedList.getValueAt(0)
        valTwo = TestAppend.linkedList.getValueAt(2)
        valThree = TestAppend.linkedList.getValueAt(4)

        with pytest.raises(IndexError) as excinfo:
            TestAppend.linkedList.getValueAt(-99)

        with pytest.raises(IndexError) as excinfo:
            TestAppend.linkedList.getValueAt(99)

        # assert
        assert valOne == 91
        assert valTwo == 21
        assert valThree == 81
        assert excinfo.value.message == "Value given out of range"
        assert excinfo.value.message == "Value given out of range"

    # Evaluates whether this method is able to retrieve the count of a list.
    def test_count(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))
        TestAppend.linkedList.append(node = pylinkedlist.Node(51))
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        TestAppend.linkedList.append(node = pylinkedlist.Node(11))
        TestAppend.linkedList.append(node = pylinkedlist.Node(81))
        
        # act
        # ...

        # assert
        assert TestAppend.linkedList.count() == 5

    # Evaluates whether this method is able to clear the contents of a list.
    def test_clear(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))
        TestAppend.linkedList.append(node = pylinkedlist.Node(51))
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        
        # act
        TestAppend.linkedList.clear()

        # assert
        assert TestAppend.linkedList.count() == 0

    # Evaluates whether this method is able to remove a node at a specific position.
    def test_removeAt(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))
        TestAppend.linkedList.append(node = pylinkedlist.Node(51))
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        TestAppend.linkedList.append(node = pylinkedlist.Node(11))
        TestAppend.linkedList.append(node = pylinkedlist.Node(81))
        
        # act
        TestAppend.linkedList.removeAt(1)
        valOne = TestAppend.linkedList.getValueAt(0)
        valTwo = TestAppend.linkedList.getValueAt(1)

        with pytest.raises(IndexError) as excinfoOne:
            TestAppend.linkedList.removeAt(-99)
        with pytest.raises(IndexError) as excinfoTwo:
            TestAppend.linkedList.removeAt(99)

        # assert
        assert valOne == 91
        assert valTwo == 21
        assert TestAppend.linkedList.count() == 4
        assert excinfoOne.value.message == "Value given out of range"
        assert excinfoTwo.value.message == "Value given out of range"

    # Evaluates whether this method is able to remove a node at a specific position when the list is empty.
    def test_removeAtWhenEmpty(self):
        # arrange 
        # ...
        
        # act
        with pytest.raises(IndexError) as excinfoOne:
            TestAppend.linkedList.removeAt(5)

        # assert
        assert excinfoOne.value.message == "Value given out of range"

    # Evaluates whether this method is able to insert a node at a specific position.
    def test_insertAt(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))
        TestAppend.linkedList.append(node = pylinkedlist.Node(51))
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        TestAppend.linkedList.append(node = pylinkedlist.Node(11))
        TestAppend.linkedList.append(node = pylinkedlist.Node(81))
        expectedOrder = [91, 51, 21, 66, 11, 81]

        # act
        TestAppend.linkedList.insertAt(3, node = pylinkedlist.Node(66))

        actualOrder = [
            TestAppend.linkedList.getValueAt(0),
            TestAppend.linkedList.getValueAt(1),
            TestAppend.linkedList.getValueAt(2),
            TestAppend.linkedList.getValueAt(3),
            TestAppend.linkedList.getValueAt(4),
            TestAppend.linkedList.getValueAt(5)
        ]

        assert expectedOrder == actualOrder

        
    # Evaluates whether this method is able to insert a node at a position 0 when the list is empty.
    def test_insertat0whenempty(self):
        # arrange 
        TestAppend.linkedList.insertAt(0, node = pylinkedlist.Node(81))
        valOne = TestAppend.linkedList.getValueAt(0)

        # act
        # ...

        # assert
        assert TestAppend.linkedList.count() == 1
        assert valOne == 81

    # Evaluates whether a exception is raised when an out of range index is given.
    def test_insertAt5WhenEmpty(self):
        # arrange 
        with pytest.raises(IndexError) as excinfoOne:
            TestAppend.linkedList.insertAt(5, node = pylinkedlist.Node(81))

        # act
        # ...

        # assert
        assert excinfoOne.value.message == "Value given out of range"

    # Evaluates whether a exception is raised when an out of range index is given.
    def test_insertAtOutOfIndex(self):
        # arrange 
        # ...

        # act
        with pytest.raises(IndexError) as excinfoOne:
            TestAppend.linkedList.insertAt(5, node = pylinkedlist.Node(81))

        # assert
        assert excinfoOne.value.message == "Value given out of range"



