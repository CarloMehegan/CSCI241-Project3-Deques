from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE

  # front will be the header.next
  # back will be the trailer.prev
  
  def push_front(self, val):
    #insert an element at index 0
    self.__list.insert_element_at(val, 0)
  
  def pop_front(self):
    #remove element at index 0
    return self.__list.remove_element_at(0)

  def peek_front(self):
    #get element at index 0
    return self.__list.get_element_at(0)

  def push_back(self, val):
    #append element
    self.__list.append_element(val)
  
  def pop_back(self):
    #remove element at index length-1
    return self.__list.remove_element_at( len(self.__list) - 1 )

  def peek_back(self):
    #get element at index length-1
    return self.__list.get_element_at( len(self.__list) - 1 )

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
