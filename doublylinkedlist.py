from copy import deepcopy
FIRST_ELEMENT_INDEX = 0
LAST_ELEMENT_INDEX = -1


class UnlinkedDLLNodeError(Exception):
    '''A class to represent an error relating to unlinked DLLNodes.'''


class EmptyDLListError(Exception):
    '''A class to represent an error relating to empty DLLists.'''


class DLListIndexError(Exception):
    '''A class to represent an error relating to DLList position values.'''


class DLListValueError(Exception):
    '''A class to represent an error relating to DLList values.'''


class DLLNode(object):
    '''A class to represent a node in a doubly linked list.'''

    def __init__(self, data, prev_node=None, next_node=None):
        '''(DLLNode, object[, DLLNode[, DLLNode]]) -> NoneType

        Create an empty DLLNode.
        '''
        self._data = data
        self._prev = prev_node
        self._next = next_node

    def set_data(self, data):
        '''(DLLNode, object) -> NoneType
        '''
        self._data = data

    def get_data(self):
        '''(DLLNode) -> object
        '''
        return self._data

    def set_prev(self, prev_node):
        '''(DLLNode, DLLNode) -> NoneType
        '''
        self._prev = prev_node
        prev_node._next = self

    def get_prev(self):
        '''(DLLNode) -> DLLNode
        '''
        return self._prev

    def remove_prev(self):
        '''(DDLNode) -> NoneType
        '''
        if self._prev is None:
            raise UnlinkedDLLNodeError('previous node does not exist')
        self._prev._next = None
        self._prev = None

    def set_next(self, next_node):
        '''(DLLNode, DLLNode) -> NoneType
        '''
        self._next = next_node
        next_node._prev = self

    def get_next(self):
        '''(DLLNode) -> DLLNode
        '''
        return self._next

    def remove_next(self):
        '''(DDLNode) -> NoneType
        '''
        if self._next is None:
            raise UnlinkedDLLNodeError('next node does not exist')
        self._next._prev = None
        self._next = None


class DLList(object):
    '''A class to represent a doubly linked list.'''

    def __init__(self):
        '''(DLList) -> NoneType

        Create an empty doubly linked list.
        '''
        self._head = None

    def __len__(self):
        '''(DLList) -> int

        Return the length or size of this list.
        '''
        return self._get_size(self._head)

    def __add__(self, other):
        '''(DLList, DLList) -> DLList

        Return the concatenation of this list with the other list.
        '''
        list1 = deepcopy(self)
        list2 = deepcopy(other)
        list1._tail().set_next(list2._head)
        return list1

    def __mul__(self, n):
        '''(DLList, int) -> DLList

        Return a copy of this list, where the items are all
        duplicated n times.
        '''
        if not n.is_integer():
            raise DLListValueError('n must be an integer')
        if n < 0:
            raise DLListValueError('illegal operation')
        elif n == 0:
            mul_list = DLList()
        else:
            mul_list = deepcopy(self)
            for i in range(n-1):
                mul_list += deepcopy(self)
        return mul_list

    def __rmul__(self, n):
        '''(DLList, int) -> DLList)

        Return a copy of this list, where the items are all
        duplicated n times.
        '''
        return self.__mul__(n)

    def __eq__(self, other):
        '''(DLList, DLList) -> bool
        '''
        equiv = False
        if len(self) == len(other):
            while 
        return equiv

    def _get_size(self, cur_node):
        '''(DLList, DLLNode) -> int

        Return the size of this list via recursion.
        '''
        # Base case
        if cur_node is None:
            result = 0
        # Recursive decomposition
        else:
            result = (1 + self._get_size(cur_node.get_next()))
        return result

    def __getitem__(self, index):
        '''(DLList, int) -> object

        Return the object at the position index in this list.
        '''
        # Get the node and its item.
        node = self._get_node(index)
        item = node.get_data()
        return item

    def _get_node(self, index):
        position = FIRST_ELEMENT_INDEX
        current = self._head
        found = False
        if index < FIRST_ELEMENT_INDEX:
            index = len(self) + index

        while (current is not None) and (not found):
            if index == position:
                found = True
            else:
                position += 1
                current = current.get_next()
        if current is None:
            raise DLListIndexError('position out of range')

        return current

    def __str__(self):
        '''(DLList) -> str

        Return the string representation of this list.
        '''
        result = '['
        if not self.is_empty():
            result += self._build_str_rep(self._head)
        result += ']'
        return result

    def _build_str_rep(self, cur_node):
        '''(DLList, DLLNode) -> str

        Build and return the string representation of this list.
        Traverse via recursion.
        '''
        # Base case
        if type(cur_node.get_data()) == str:
            rep = "'%s'" % cur_node.get_data()
        else:
            rep = str(cur_node.get_data())
        # Recursive decomposition
        if cur_node.get_next() is not None:
            rep += ', ' + self._build_str_rep(cur_node.get_next())
        return rep

    def _tail(self):
        '''(DLList) -> DLLNode

        Return the tail (last node) of this list.
        '''
        return self._get_tail(self._head)

    def _get_tail(self, cur_node):
        '''(DLList, DLLNode) -> DLLNode

        Return the tail (last node) of this list via recursion.
        '''
        # Base case
        if cur_node.get_next() is None:
            result = cur_node
        # Recursive decomposition
        else:
            result = self._get_tail(cur_node.get_next())
        return result

    def add_to_head(self, item):
        '''(DLList, object) -> NoneType

        Add item to the head (first index) of this list.
        '''
        new_node = DLLNode(item)
        if self.is_empty():
            self._head = new_node
        else:
            self._head.set_prev(new_node)
            self._head = new_node

    def add_to_tail(self, item):
        '''(DLList, object) -> NoneType

        Add item to the tail (last index) of this list.
        '''
        new_node = DLLNode(item)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail().set_next(new_node)

    def add(self, index, item):
        '''(DLList, int, object) -> NoneType

        Add item to position index in this list.
        '''
        if index < FIRST_ELEMENT_INDEX:
            index = len(self) + index

        if index == FIRST_ELEMENT_INDEX:
            self.add_to_head(item)
        elif index >= len(self):
            self.add_to_tail(item)
        else:
            new_node = DLLNode(item)
            # Get the prev and next nodes and unlink them.
            next_to_new_node = self._get_node(index)
            prev_to_new_node = next_to_new_node.get_prev()
            next_to_new_node.remove_prev()
            # Link the prev and next nodes to the new node.
            new_node.set_prev(prev_to_new_node)
            new_node.set_next(next_to_new_node)

    def pop_head(self):
        '''(DLList) -> object

        Remove and return the head from this list.

        RAISES: EmptyDLListError if list is empty.
        '''
        if self.is_empty():
            raise EmptyDLListError('cannot remove from an empty list')
        head_item = self._head.get_data()
        self._head = self._head.get_next()
        if self._head is not None:
            self._head.remove_prev()
        return head_item

    def pop_tail(self):
        '''(DLList) -> object

        Remove and return the tail item from this list.

        RAISES: EmptyDLListError if list is empty.
        '''
        if self.is_empty():
            raise EmptyDLListError('cannot remove from an empty list')
        # Get the tail node and the node before the tail.
        tail_node = self._tail()
        before_tail_node = tail_node.get_prev()
        # Remove the tail node (if it exists).
        if before_tail_node is not None:
            before_tail_node.remove_next()
        # Return the former tail item.
        return tail_node.get_data()

    def pop(self, index):
        '''(DLList, int) -> object

        Remove and return the item at position index from this list.
        '''
        LIST_LEN = len(self)
        if index in (FIRST_ELEMENT_INDEX, -LIST_LEN):
            item = self.pop_head()
        elif index in (LIST_LEN-1, LAST_ELEMENT_INDEX):
            item = self.pop_tail()
        else:
            # Get the target node, its item and its surrounding nodes.
            target_node = self._get_node(index)
            item = target_node.get_data()
            prev_node = target_node.get_prev()
            next_node = target_node.get_next()
            # Remove the nodes around the target node,
            # and link those nodes together.
            target_node.remove_prev()
            target_node.remove_next()
            prev_node.set_next(next_node)
        # Return the item.
        return item

    def search(self, item):
        '''(DLList, object, DLLNode) -> bool

        Return the index of item in this list.
        '''
        index = 0
        current = self._head
        found = False

        while (current is not None) and (not found):
            if item == current.get_data():
                found = True
            else:
                index += 1
                current = current.get_next()
        if not found:
            index = -1

        return index

    def clear(self):
        '''(DLList) -> NoneType

        Remove all items from this list.
        '''
        self._head = None

    def is_empty(self):
        '''(DLList) -> bool

        Return True if this list is empty.
        '''
        return (self._head is None)


class SortedDLList(DLList):
    '''A class to represent a sorted (non-decreasing) doubly linked list.'''

    def __init__(self):
        '''(SortedDLList) -> NoneType

        Create an empty sorted list.
        '''
        DLList.__init__(self)

    def add(self, item):
        '''(SortedDLList, object) -> NoneType
    
        Add item to this sorted list.
        '''
        new_node = DLLNode(item)
        prev_node = None
        if self.is_empty():
            self._head = new_node
        else:
            stop = False
            current = self._head
            while (current is not None) and (not stop):
                if current.get_data() > item:
                    stop = True
                else:
                    prev_node = current
                    current = current.get_next()

            # If the new node is to be added at the end of the list,
            # link the node to prev_node.
            if (prev_node is not None) and (current is None):
                prev_node.set_next(new_node)
            # If the new node is to be added at the beginning of the list,
            # link the node to current, and set the head to the new node.
            elif (prev_node is None) and (current is not None):
                current.set_prev(new_node)
                self._head = new_node
            # Otherwise, cut the links between prev_node and current,
            # and link the new node to both prev_node and current.
            else:
                current.remove_prev()
                new_node.set_prev(prev_node)
                new_node.set_next(current)

    def remove(self, item):
        '''(SortedDLList, object) -> NoneType

        Remove item from this list.
        '''
        trg_index = self.search(item)
        self.pop(trg_index)

    def middle(self):
        '''(SortedDLList) -> object

        Return the object that is in the 'middle' of this list.
        If this list has an number of items, return the item closest
        to the head.
        '''
        LIST_LEN = len(self)
        mid_index = LIST_LEN // 2
        if (LIST_LEN % 2 == 0):
            mid_index -= 1
        mid_node = self._get_node(mid_index)
        return mid_node.get_data()


if __name__ == '__main__':
    '''
    test = DLList()
    test.add_to_head('head')
    test.add_to_tail('connect')
    test.add_to_tail(1)
    test.add_to_tail(2)
    test.add_to_tail(3)
    print(test)
    '''
    new = SortedDLList()
    new.add('g')
    new.add('a')
    new.add('c')
    new.add('d')

    print(new, new.middle())
