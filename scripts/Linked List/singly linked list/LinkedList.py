# Simple implemenatation of a singly linked list in python

'''
    -------------------------------------------------------------------

    Linked list:
    It is a simple data structure similar to an array.
    It is used to store a collection of data in a linear manner.
    Elements arent stored together, rather, are linked with pointers.

    -------------------------------------------------------------------

    Advantages over arrays:
        1. Dynamic size
        2. Easier to insert and delete as compared to an array

    -------------------------------------------------------------------

    Disadvantages over arrays:
        1. Can't access elements randomly
        2. Memory wasted for storing pointer
        3. Not Cache friendly

    -------------------------------------------------------------------

    Big O notation stats:
        Indexing: O(n)
        Search: O(n)
        Optimized Search: O(n)
        Insertion: O(1)
        Space complexity : O(n)

    -------------------------------------------------------------------

'''

class Element(object):
    # This class is made to store the element of the list
    def __init__(self, value):
        # Stores value of element and pointer to next object
        self.value = value
        self.next = None

class LinkedList(object):
    # This class is to create the linked list
    def __init__(self, head = None):
        self.head = head

    # List Operations

    # Append element to list
    def add_element(self, other):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = other
        
        else:
            self.head = other


    # Function to delete element form linked list
    def del_element(self, other):
        
        current = self.head
        if self.head:
            while True:
                if current.next == other:
                    # Starts pointing to next element
                    current.next = other.next




