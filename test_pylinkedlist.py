import pylinkedlist
import pytest

class TestAppend:
    linkedList = None
        
    def setup(self):
        TestAppend.linkedList = pylinkedlist.LinkedList()

    def test_append(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        TestAppend.linkedList.append(node = pylinkedlist.Node(31))
        TestAppend.linkedList.append(node = pylinkedlist.Node(11))
        
        # act
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))

        # assert
        assert TestAppend.linkedList.getValueAt(3) == 91

    def test_prepend(self):
        # arrange 
        TestAppend.linkedList.prepend(node = pylinkedlist.Node(10))
        TestAppend.linkedList.prepend(node = pylinkedlist.Node(20))
        TestAppend.linkedList.prepend(node = pylinkedlist.Node(30))
        
        # act
        TestAppend.linkedList.prepend(node = pylinkedlist.Node(40))

        # assert
        assert TestAppend.linkedList.getValueAt(0) == 40

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

    def test_clear(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))
        TestAppend.linkedList.append(node = pylinkedlist.Node(51))
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        
        # act
        TestAppend.linkedList.clear()

        # assert
        assert TestAppend.linkedList.count() == 0

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

    def test_removeAtWhenEmpty(self):
        # arrange 
        # ...
        
        # act
        with pytest.raises(IndexError) as excinfoOne:
            TestAppend.linkedList.removeAt(5)

        # assert
        assert excinfoOne.value.message == "Value given out of range"

    def test_insertAt(self):
        # arrange 
        TestAppend.linkedList.append(node = pylinkedlist.Node(91))
        TestAppend.linkedList.append(node = pylinkedlist.Node(51))
        TestAppend.linkedList.append(node = pylinkedlist.Node(21))
        TestAppend.linkedList.append(node = pylinkedlist.Node(11))
        TestAppend.linkedList.append(node = pylinkedlist.Node(81))

        # act
        TestAppend.linkedList.insertAt(1, node = pylinkedlist.Node(66))
        valOne = TestAppend.linkedList.getValueAt(3)

        # assert
        assert valOne == 66 

    def test_insertat0whenempty(self):
        # arrange 
        TestAppend.linkedList.insertAt(0, node = pylinkedlist.Node(81))
        valOne = TestAppend.linkedList.getValueAt(0)

        # act

        # assert
        assert valOne == 81

    def test_insertAt5WhenEmpty(self):
        # arrange 
        with pytest.raises(IndexError) as excinfoOne:
            TestAppend.linkedList.insertAt(5, node = pylinkedlist.Node(81))

        # act

        # assert
        assert excinfoOne.value.message == "Value given out of range"


