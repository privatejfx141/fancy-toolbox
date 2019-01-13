from doublylinkedlist import *

class FullContainerError(Exception):
    '''A class to represent an error for a container being full.'''


class EmptyContainerError(Exception):
    '''A class to represent an error for a container being empty.'''


class Container(object):
    '''A class to represent a container.'''

    def __init__(self):
        '''(Container) -> NoneType

        Creates an empty container.
        '''
        self._items = DLList()

    def _set_list(self, new_list):
        '''(Container, DLList) -> NoneType

        Sets the DLList representation of this container.
        '''
        self._items = new_list

    def _get_list(self):
        '''(Container) -> DLList

        Returns the DLList representation of this container.
        '''
        return self._items

    def _put(self, item, index_put=None):
        '''(Container, object) -> NoneType

        Put a new item into this container.
        '''
        if index_put == None:
            self._items.add_to_tail(item)
        else:
            self._items.add(index_put, item)

    def _peek(self, index_peek=FIRST_ELEMENT_INDEX):
        '''(Container) -> object

        Return the item at index_peek from this container.
        '''
        if self.is_empty():
            raise EmptyContainerError(self.__class__.__name__ + ' is empty')
        return self._items[index_peek]

    def _get(self, index_pop=FIRST_ELEMENT_INDEX):
        '''(Container) -> object

        Return and remove the item at index_pop from this container.
        '''
        if self.is_empty():
            raise EmptyContainerError(self.__class__.__name__ + ' is empty')
        return self._items.pop(index_pop)

    def clear(self):
        '''(Container) -> NoneType

        Remove all the objects in this container.
        '''
        self._items.clear()

    def size(self):
        '''(Container) -> int

        Return the size of this container.
        '''
        return len(self._items)

    def is_empty(self):
        '''(Container) -> bool

        Return True if this container is empty.
        '''
        return self._items.is_empty()


class Bucket(Container):
    '''A class to represent a Bucket, container that contains 1 object.'''

    def __init__(self, item=tuple()):
        '''(Bucket) -> NoneType

        Create an empty bucket.
        '''
        Container.__init__(self)

    def _set_list(self, new_list):
        '''(Bucket, DLList) -> NoneType

        Set the DLList representation of this bucket.
        '''
        if len(new_list) > 1:
            raise FullContainerError('number of items in list is invalid')
        Container._set_list(self, new_list)

    def put(self, new_item):
        '''(Bucket, object) -> NoneType

        Fill this bucket with a new item.
        '''
        if not self.is_empty():
            raise FullContainerError('Bucket already has an item')
        self._put(new_item)

    def peek(self):
        '''(Bucket) -> object

        Return the value of the item in this bucket.
        '''
        return self._peek(FIRST_ELEMENT_INDEX)

    def get(self):
        '''(Bucket) -> object

        Return and remove the item in this bucket.
        '''
        return self._get(FIRST_ELEMENT_INDEX)


class Stack(Container):
    '''A class to represent a Stack, LIFO data structure container.'''

    def __init__(self):
        '''(Stack) -> NoneType

        Create an empty stack.
        '''
        Container.__init__(self)

    def push(self, new_item):
        '''(Stack, object) -> NoneType

        Add a new item on top of this stack.
        '''
        self._put(new_item)

    def peek(self):
        '''(Stack) -> object

        Return the value of the item on top of this stack.
        '''
        return self._peek(LAST_ELEMENT_INDEX)

    def pop(self):
        '''(Stack) -> object

        Return and remove the top item from this stack.
        '''
        return self._get(LAST_ELEMENT_INDEX)


class Queue(Container):
    '''A class to represent a Queue, FIFO data structure container.'''

    def __init__(self):
        '''(Queue) -> NoneType

        Create an empty queue.
        '''
        Container.__init__(self)

    def enqueue(self, new_item):
        '''(Queue, object) -> NoneType

        Adds a new item at the end of this queue.
        '''
        self._put(new_item)

    def dequeue(self):
        '''(Queue, object) -> NoneType

        Return and remove the item at the front of this queue.
        '''
        return self._get(FIRST_ELEMENT_INDEX)


class Deque(Container):
    '''A class to represent a Deque, double-ended queue.'''

    def __init__(self):
        '''(Deque) -> NoneType

        Create an empty deque.
        '''
        Container.__init__(self)

    def add_front(self, new_item):
        '''(Deque, object) -> NoneType

        Add a new item to the front of this deque.
        '''
        self._put(new_item)

    def add_rear(self, new_item):
        '''(Deque, object) -> NoneType

        Add a new item to the rear of this deque.
        '''
        self._put(new_item, FIRST_ELEMENT_INDEX)

    def remove_front(self):
        '''(Deque, object) -> NoneType

        Remove and return the front item from this deque.
        '''
        return self._get(LAST_ELEMENT_INDEX)

    def remove_rear(self):
        '''(Deque, object) -> NoneType

        Remove and return the rear item from this deque.
        '''
        return self._get(FIRST_ELEMENT_INDEX)


if (__name__ == '__main__'):
    import doctest
    bucket = Bucket()
    stack = Stack()
    queue = Queue()
    deque = Deque()
