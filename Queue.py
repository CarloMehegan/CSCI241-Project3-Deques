from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    #string of a queue should look the same as a deque
    #we will enqueue at the back, which will be the end of the string
    #and dequeue at the front, which will be the beginning of the string
    return str(self.__dq)

  def __len__(self):
    return len(self.__dq)

  def enqueue(self, val):
    self.__dq.push_back(val)

  def dequeue(self):
    return self.__dq.pop_front()

  def peek(self):
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
