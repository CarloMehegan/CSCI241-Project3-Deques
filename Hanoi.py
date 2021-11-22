import timeit
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  # # TODO replace pass with your base and recursive cases.
  # #base case: one ring to move
  #     #move ring to goal stack
  # #recursive case: more than one ring to move
  #     #call 
  # pass
  if n == 0:
    d.push(s.pop())
  else:
    #move n-1 to aux
    Hanoi_rec(n-1, s, d, a)
    #move n to goal
    d.push(s.pop())
    #move n-1 to goal
    Hanoi_rec(n-1, a, s, d)


  print(n, s, a, d)
  print()

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=3
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")
