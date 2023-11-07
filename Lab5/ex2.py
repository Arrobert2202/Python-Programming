class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
  
  def push(self, value):
    node = Node(value)
    node.next = None
    if self.is_empty():
      self.first = node
      self.last = node
    else:
      self.last.next = node
      self.last = node

  def pop(self):
    if self.is_empty():
      return None
    else:
      node = self.first
      self.first = node.next
      if self.first is None:
        self.last = None
      return node.value
    
  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.first.value
  
  def is_empty(self):
    return self.first is None
  
queue = Queue()
queue.push('a')
queue.push('b')
queue.push('c')

while not queue.is_empty():
  print(queue.peek())
  queue.pop()