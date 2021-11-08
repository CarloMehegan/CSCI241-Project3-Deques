from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__length = 0
    self.__front_index = 0
    self.__back_index = 0
    pass
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    pass
    
  def __len__(self):
    # TODO replace pass with an implementation that Sreturns the number of
    # items in the deque. This method must run in constant time.
    
    # return len(self.__contents) this wont work
    #need to start at front and count every cell until we reach back
    #or keep track of length in all operations and return that value
    pass

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)

    #new_array = [None] * (self.__capacity * 2)

    #copy over values to the new array, BUT start at the front_index, so that the front
    #in the the new array is at index 0.
    #for i in range(self.__contents):
      #new_array[i] = self.__contents[(i + self.__front_index) % self.__length]

    #self.__front_index = 0
    #self.__back_index = self.__length-1
    #self.__contents = new_array
    #self.__capacity *= 2
    #self.__length stays the same

    pass
    
  #front will be index 0 of the array
  #back will be index length-1 of the array
  #push front means front - 1
  #pop front means front + 1
  #push back means back + 1
  #pop back means back - 1
  #TODO how to make sure back and front dont cross?

  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.

    #if length == capacity:
      #self.__grow()
    #change the front index of the deque to (front_index - 1) % self.__capacity
    #self.__length += 1
    pass
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.

    #change the front index of the deque to (front_index + 1) % self.__capacity
    #self.__length -= 1
    pass
    
  def peek_front(self):
    # TODO replace pass with your implementation.

    #return self.__contents[self.__front_index]
    pass
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.

    #if length == capacity:
      #self.__grow()
    #change the back index of the deque to (back_index + 1) % self.__capacity
    #self.__length += 1
    pass
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.

    #change the back index of the deque to (back_index - 1) % self.__capacity
    #self.__length -= 1
    pass

  def peek_back(self):
    # TODO replace pass with your implementation.

    #return self.__contents[self.__back_index]
    pass

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
