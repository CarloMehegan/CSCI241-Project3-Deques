import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.

  #initialize variables
  #read the file with open() and store its contents in a string
  passed = True
  s = Stack()
  f = open(filename, "r")
  string = f.read()

  #iterate through every character in string, checking for delimiters
  for val in string:
    #if open delimiter, push to stack
    if (val == "(" or val == "[" or val == "{"):
      s.push(val)

    #if closed delimiter, check if the top of the stack
    #is a matching opening delimiter. if it is, pop the stack.
    #if it isn't, closing delimiters are imbalanced
    elif (val == ")"):
      if (s.peek() == "("):
        s.pop()
      else:
        passed = False
    elif (val == "]"):
      if (s.peek() == "["):
        s.pop()
      else:
        passed = False
    elif (val == "}"):
      if (s.peek() == "{"):
        s.pop()
      else:
        passed = False
  
  #finally, check if the stack is empty. if it isn't,
  #if it isn't, opening delimiters are imbalanced
  print(str(s))
  if (str(s) != "[ ]"):
    passed = False
  
  #passed defaults to True, and changes to False if the
  #tests above find imbalanced delimiters anywhere
  return passed
    

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


