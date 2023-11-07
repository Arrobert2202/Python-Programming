class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.top = None

  def push(self, value):
    node = Node(value)
    node.next = self.top
    self.top = node

  def pop(self):
    if self.is_empty():
      return None
    else:
      node = self.top
      self.top = self.top.next
      return node.value
  
  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.top.value
    
  def is_empty(self):
    return self.top is None
  
stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')

while not stack.is_empty():
  print(stack.peek())
  stack.pop()