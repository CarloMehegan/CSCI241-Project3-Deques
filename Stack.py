from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    #string of a stack should look the same as a deque
    #the "top" of the stack will be at the start of the string
      #and the "bottom" will be at the end
    return str(self.__dq)

  def __len__(self):
    return len(self.__dq)

  def push(self, val):
    self.__dq.push_front(val)

  def pop(self):
    return self.__dq.pop_front()

  def peek(self):
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
