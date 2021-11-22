class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class.
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class

        #header and trailer represent the sentinel nodes at the bookends of the LL.
        self.header = self.__Node(None)
        self.trailer = self.__Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        #keep track of size too
        self.size = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list.
        return self.size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position.

        #create a new node
        new = self.__Node(val)
        #the last node is the one before the trailer
        last_node = self.trailer.prev
        #switch pointers to put new in the right place
        last_node.next = new
        self.trailer.prev = new
        new.last = last_node
        new.next = self.trailer
        #increase self.size and end
        self.size += 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position.

        #if LL is empty, raise error. cannot be used to add item at the tail position
        if self.header.next == self.trailer:
            raise IndexError
        #if index is greater than size, it is out of bounds
        #if index is equal to size, it is trying to append, which we shouldn't
         #do here
        #if index is less than zero, it is out of bounds
        if index >= self.size or index < 0:
            raise IndexError
        #create a new node
        new = self.__Node(val)
        #if index is 0, take advantage of sentinel node so that we don't have
         #to repeat pointer assignment lines
        if index == 0:
            current = self.header
        else:
            current = self.header.next
        #move to the node before where we want to insert the new node
        for i in range(index-1):
            current = current.next
        #assign pointers to insert new node
        new.next = current.next
        current.next = new
        new.prev = current
        new.next.prev = new
        #increment size
        self.size += 1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. 
        
        #if LL is empty, cannot remove
        if self.header.next == self.trailer:
            return
        #if index is greater than or equal to size, it is out of bounds
        #if index is less than zero, it is out of bounds
        if index >= self.size or index < 0:
            raise IndexError
        #if index is 0, take advantage of sentinel node so that we don't have
         #to repeat lines
        if index == 0:
            current = self.header
        else:
            current = self.header.next
        #move to the node before the node we want to remove
        for i in range(index-1):
            current = current.next
        #remember value of the node being removed in order to return it
        removed_value = current.next.val
        #assign pointers to remove the node in front of current
        current.next = current.next.next
        current.next.prev = current
        #decrement size
        self.size -= 1
        return removed_value

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. 
        
        #if LL is empty, cannot get elements
        if self.header.next == self.trailer:
            raise IndexError
        #if index is greater than or equal to size, it is out of bounds
        #if index is less than zero, it is out of bounds
        if index >= self.size or index < 0:
            raise IndexError
        #start with node at zero and loop until you reach the node at index
        current = self.header.next
        for i in range(index):
            current = current.next
        #return the value of the node at index
        return current.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. 

        #if LL is empty, cannot rotate
        if self.header.next == self.trailer:
            return
        #remember the head node and tail node
        first = self.header.next
        last = self.trailer.prev
        #reassign .nexts
        last.next = first
        self.header.next = first.next
        first.next = self.trailer
        #reassign .prevs
        self.trailer.prev = first
        first.prev = last
        self.header.next.prev = self.header
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. 
        
        #start with open brackets
        string = "[ "
        #loop through the list and add the values to a string
        for val in self:
            string = string + str(val) + ", "
        #make it pretty and return
        string = string + "]"
        string = string.replace(", ]", " ]")
        return string

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__iter_node = self.header.next
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. 

        #self.__iter_node is the current node
        #if self.__iter_node is equal to the trailer, we've reached the end
        if self.__iter_node == self.trailer:
            raise StopIteration
        #set the return value to the value of the current node
        to_return = self.__iter_node.val
        self.__iter_node = self.__iter_node.next
        return to_return

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        
        reverse = Linked_List()
        #if original linked list is empty, do nothing
        if self.header.next == self.trailer:
            return reverse
        #insert_element_at cannot add a node to the tail position,
         #so let's add a temporary node to fill in the tail position
        reverse.append_element(None)
        #insert values one at a time at the head position of the LL
        for val in self:
            reverse.insert_element_at(val, 0)
        #remove temporary node from before
        reverse.remove_element_at(self.size)
        #return reversed linked list
        return reverse

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements.

    # Do the indexed methods position items correctly when given valid indices? 
    ll = Linked_List()
    ll.append_element(4)
    ll.append_element(5)
    ll.insert_element_at(2, 0)
    # Does the string representation of your list conform to the specified format?
    print("linked list:")
    print(ll)
    print("second element:")
    print(str(ll.get_element_at(1)))
    # Does removing an element function correctly regardless of that element's location?
    ll.remove_element_at(1)
    ll.remove_element_at(0)
    print("remove the first two nodes:")
    print(ll)
    ll.remove_element_at(0)
    print("remove the last node:")
    print(ll)
    ll.append_element(5)
    ll.append_element(6)
    ll.append_element(7)
    ll.append_element(8)
    print("new linked list:")
    print(ll)
    print("rotation:")
    ll.rotate_left()
    print(ll)
    ll.rotate_left()
    print(ll)
    ll.rotate_left()
    print(ll)
    ll.rotate_left()
    print(ll)
    print("reversed: ")
    print (reversed(ll))
    print("size of array: " + str(len(ll)))

    # Does a for loop iterate through your list from head to tail? 
    total = 0
    for val in ll:
        total += val
    print("total sum: " + str(total))

    # Does a for loop iterate through your reversed list from tail to head? 
    product = 1
    for val in reversed(ll):
        product *= val
    print("total product: " + str(product))


    # move on to testing error cases
    print("==============================================================")
    

    # Do the indexed methods raise exceptions when given invalid indices?
    empty = Linked_List()

    try:
        print("attempt to remove from an empty list:")
        empty.remove_element_at(0)
        print("  SUCCESS")
    except IndexError:
        print(" ERROR: the linked list is empty")

    try:
        print("attempt to insert element at negative index:")
        empty.insert_element_at(1, -1)
        print("  SUCCESS")
    except IndexError:
        print("  ERROR: out of bounds")

    try:
        print("attempt to insert element at too large of an index:")
        empty.insert_element_at(1, 40)
        print("  SUCCESS")
    except IndexError:
        print("  ERROR: out of bounds")

    try:
        print("attempt to get an element from an empty list:")
        empty.get_element_at(0)
        print("  SUCCESS")
    except IndexError:
        print("  ERROR: the linked list is empty")

    try:
        print("attempt to get element from out of bounds index:")
        empty.get_element_at(40)
        print("  SUCCESS")
    except IndexError:
        print("  ERROR: out of bounds")

    # the following should not raise an error
    try:
        print("attempting to rotate left with an empty list:")
        empty.rotate_left()
        print("  " + str(empty))
        print("  SUCCESS")
    except:
        print("  ERROR: how did you get here?")

    try:
        print("attempting to reverse an empty list:")
        print("  " + str(reversed(empty)))
        print("  SUCCESS")
    except:
        print("  ERROR: how did you get here?")

    # Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. 
    
