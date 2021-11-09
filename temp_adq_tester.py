from Deque_Generator import get_deque
from Stack import Stack

dq = get_deque(1)

print(str(dq))

dq.push_front(1)
print(str(dq))
dq.pop_front()


print(str(dq))

dq.push_front(0)

print(str(dq))

print(str(dq))

print("stack")

s = Stack()
print(s)
s.push(1)
s.pop()
# s.pop()
s.push(2)
s.push(3)
print(s)
popped = s.pop()
print(s)
print("popped " + str(popped))