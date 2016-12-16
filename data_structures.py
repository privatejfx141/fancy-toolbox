class EmptyStackError(Exception):
    '''A class to represent an error relating to an empty stack.'''


class EmptyQueueError(Exception):
    '''A class to represent an error relating to an empty queue.'''


class Stack():
    '''A class to represent a stack, a LIFO linear data structure.'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create an empty stack.
        '''
        self._items = list()

    def push(self, new_item):
        '''(Stack, object) -> NoneType
        Adds a new item on top of this stack.
        '''        
        self._items.append(new_item)

    def size(self):
        '''(Stack) -> int
        Return the number of items on this stack.
        '''
        return len(self._items)

    def pop(self):
        '''(Stack) -> object
        Return and remove the top item from this stack.
        '''
        try:
            return self._items.pop()
        except:
            raise EmptyStackError('Cannot pop an empty stack.')
    
    def peek(self):
        '''(Stack) -> object
        Return the top item from this stack.
        '''
        try:
            return self._items[-1]
        except:
            raise EmptyStackError('Cannot peek into an empty stack.')

    def is_empty(self):
        '''(Stack) -> bool
        Return True if this stack is empty.
        '''
        return self._items == list()


class Queue():
    '''A class to represent a Queue, a FIFO linear data structure.'''

    def __init__(self):
        '''(Queue) -> NoneType
        Create an empty queue.
        '''
        self._items = list()

    def enqueue(self, new_item):
        '''(Queue, object) -> NoneType
        Adds a new item on top of this queue.
        '''        
        self._items.append(new_item)

    def size(self):
        '''(Queue) -> int
        Return the number of items on this queue.
        '''
        return len(self._items)

    def dequeue(self):
        '''(Queue) -> object
        Return and remove the top item from this queue.
        '''
        try:
            return self._items.pop(0)
        except:
            raise EmptyQueueError('Cannot dequeue an empty queue.')

    def is_empty(self):
        '''(Queue) -> bool
        Return True if this queue is empty.
        '''
        return self._items == list()


class Tree():
    '''A class to represent a tree node.'''

    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


class Node():
    '''A class to represent a node of a linked list.'''

    def __init__(self, data):
        '''(Node, object) -> NoneType
        Create a node that stores an object and a pointer to the next node.
        '''
        self._cargo = data
        self._next = None


class LinkedList():
    '''A class to represent a linked list.'''
    
    def __init__(self, *items):
        '''(LinkedList) -> NoneType
        '''
        self._head = None
        self._tail = None
        for cur_item in items:
            self.add_node(cur_item)       

    def add_node(self, data):
        '''(LinkedList, object) -> NoneType
        '''
        # Create a node.
        new_node = Node(data)
        if self._head == None:
            self._head = new_node
        if self._tail != None:
            self._tail._next = new_node
        # Set the new node as the tail.
        self._tail = new_node

    def remove_node(self, index):
        '''(LinkedList, int) -> NoneType
        '''
        prev = None
        node = self._head
        count = 0
        while (node != None) and (count < index):
            prev = node
            node = node._next
            count += 1
        if prev == None:
            self._head = node._next
        else:
            prev._next = node._next
    
    def get_node(self, index):
        '''(LinkedList, int) -> object
        '''
        prev = None
        node = self._head
        count = 0
        while (node != None) and (count < index):
            prev = node
            node = node._next
            count += 1
        cargo = node._cargo
        
        return cargo

    def print_list(self):
        '''(LinkedList) -> NoneType
        '''
        node = self._head
        while node != None:
            print(node._cargo)
            node = node._next
    
    def __str__(self):
        '''(LinkedList) -> str
        '''
        node = self._head
        result = '['
        while node != None:
            result += str(node._cargo)
            if node._next != None:
                result += ', '
            node = node._next
        result += ']'
        return result


def size_of_stk(stk):
    '''(Stack) -> int
    Return the number of items in stack stk.

    >>> stk = Stack()
    >>> [stk.push(i) for i in range(10) if i % 2 == 0]
    [None, None, None, None, None]
    >>> size_of_stk(stk)
    5
    '''
    # Create an empty temporary stack.
    temp_stk = Stack()
    # Initialize the number of items to be zero.
    num_items = 0
    # Loop, add, and count each item from stk to temp_stk, until stk is empty.
    while not(stk.is_empty()):
        temp_stk.push(stk.pop())
        num_items += 1
    # Re-add each item from temp_stk to stk.
    while not(temp_stk.is_empty()):
        stk.push(temp_stk.pop())
    # Return the number of items in stk.
    return num_items


if __name__ == '__main__':
    import doctest
