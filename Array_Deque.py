from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # replace pass with any additional initializations you need.
    self.__length = 0
    self.__front_index = 0
    self.__back_index = 0
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.

    #start with open brackets
    adq_string = "[ "
    #loop through the list and add the values to a string
    for i in range(self.__length):
        adq_string = adq_string + str(self.__contents[(i + self.__front_index) % self.__capacity]) + ", "
    #make it pretty and return
    adq_string = adq_string + "]"
    adq_string = adq_string.replace(", ]", " ]")
    # print(adq_string)
    return adq_string
    
  def __len__(self):
    # replace pass with an implementation that Sreturns the number of
    # items in the deque. This method must run in constant time.
    
    # return len(self.__contents) this wont work
    #need to start at front and count every cell until we reach back
    #or keep track of length in all operations and return that value
    return self.__length

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)

    new_array = [None] * (self.__capacity * 2)

    #copy over values to the new array, BUT start at the front_index, so that the front
    #in the the new array is at index 0.
    #by using length as the range, if we start at front_index, then we will end at back_index
    for i in range(self.__length):
      new_array[i] = self.__contents[(i + self.__front_index) % self.__capacity]

    #our loop puts front at index 0 and back at index length-1
    self.__front_index = 0
    self.__back_index = self.__length-1
    self.__contents = new_array
    self.__capacity *= 2
    #self.__length stays the same
    
  """
  KEY
  front will be index 0 of the array after growth
  back will be index length-1 of the array after growth
  push front means front - 1
  pop front means front + 1
  push back means back + 1
  pop back means back - 1
  TODO how to make sure back and front dont cross?
  """

  def push_front(self, val):
    # replace pass with your implementation, growing the array before
    # pushing if necessary.

    #if at max capacity, then grow first
    if self.__length == self.__capacity:
      self.__grow()
    #change the front index of the deque to (front_index - 1) % self.__capacity
    self.__front_index = (self.__front_index - 1) % self.__capacity
    self.__contents[self.__front_index] = val
    self.__length += 1
    
  def pop_front(self):
    # replace pass with your implementation. Do not reduce the capacity.

    #check if array is empty, if it is, dont do anything
    if (self.__length == 0):
      return
      # raise IndexError

    #pop operations return the value that is removed
    returned = self.__contents[self.__front_index]
    #change the front index of the deque to (front_index + 1) % self.__capacity
    self.__front_index = (self.__front_index + 1) % self.__capacity
    #don't need to change contents and remove value, bc we will overwrite it
      #if we use this cell again anyways
    self.__length -= 1
    return returned
    
  def peek_front(self):
    # replace pass with your implementation.
    if self.__length == 0:
      return None
    else:
      return self.__contents[self.__front_index]
    
  def push_back(self, val):
    # replace pass with your implementation, growing the array before
    # pushing if necessary.

    if self.__length == self.__capacity:
      self.__grow()
    #change the back index of the deque to (back_index + 1) % self.__capacity
    self.__back_index = (self.__back_index + 1) % self.__capacity
    self.__contents[self.__back_index] = val
    self.__length += 1
  
  def pop_back(self):
    # replace pass with your implementation. Do not reduce the capacity.

    #check if array is empty, if it is, dont do anything
    if self.__length == 0:
      return
      # raise IndexError

    #pop operations return the value that is removed
    returned = self.__contents[self.__back_index]
    #change the back index of the deque to (back_index - 1) % self.__capacity
    self.__back_index = (self.__back_index - 1) % self.__capacity
    #don't need to change contents and remove value, bc we will overwrite it
      #if we use this cell again anyways
    self.__length -= 1
    return returned

  def peek_back(self):
    # replace pass with your implementation.
    if self.__length == 0:
      return None
    else:
      return self.__contents[self.__back_index]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
