class Node:
  def __init__(self, data=None, next=None): 
    self.data = data
    self.next = next

class linked_list:
  def __init__(self):  
    self.head = None
  
  def insertion(self, data):
    new_node = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = new_node
    else:
      self.head = new_node
  
  def print_list(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next


def list_reverse(linked_list):
  previous = None
  current = linked_list.head
  following = current.next
  while current:
      current.next = previous
      previous = current
      current = following
      if following:
          following = following.next
  linked_list.head = previous

my_list = linked_list()
my_list.insertion(0)
my_list.insertion(1)
my_list.insertion(1)
my_list.insertion(2)
my_list.insertion(3)
my_list.insertion(5)
my_list.insertion(8)
print('----Linked List----')
my_list.print_list()
print('----Formated List----')
list_reverse(my_list)
my_list.print_list()