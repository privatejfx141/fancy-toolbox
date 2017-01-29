/**
 * LinkedList is an implementation of a pythonic linked list ADT.
 * 
 * @author Jeffrey L.
 * @version 1.1
 * @since 2017-01-26
 */
public class LinkedList {
	// linked list of nodes holding integers

	private class Node {
		// linked node with data
		Object data;
		Node nextNode;
		Node(Object item) {
			// create an unlinked node with data
			this.data = item;
		}
		public String toString() {
			// return the string representation of this node
			return "Node(" + data + ")";
		}
	}

	private Node head;
	private final int lastIndex = -1;

	// constructor
	LinkedList(Object... datas) {
		// create a linked list with a head.
		for (Object data : datas) {
			append(data);
		}
	}

	private int realIndex(int index) {
		if (index < 0) {
			index += size();
		}
		return index;
	}

	private Node getNode(int index) {
		index = realIndex(index);
		// create a counter and the node 'counter'
		Node current = head;
		int count = 0;
		// while loop until last node is reached or counter matches.
		while (current != null && count != index) {
			count += 1;
			current = current.nextNode;
		}
		// return the node reached.
		return current;
	}
	
	private Node tail() {
		// the last node reached is the tailNode.
		return getNode(lastIndex);
	}
	
	/**
	 * Recursively traverses and builds the string representation
	 * of this LinkedList.
	 * 
	 * @param current the current node.
	 * @return the current iteration of the string representation.
	 */
	private String toString(Node current) {
		// base case
		String repr = current.data == null ? "null" : current.data.toString();
		// recursive decomposition: n-1 approach
		if (current.nextNode != null) {
			repr += ", " + toString(current.nextNode);
		}
		return repr;
	}

	/**
	 * Returns the string representation of this list,
	 * enclosed in square brackets.
	 */
	public String toString() {		
		return "[" + (isEmpty() ? "" : toString(head)) + "]";
	}
	
	/**
	 * Returns the item in this linked list at position index.
	 * @param index the position index where an item is to be found.
	 * @return the item at position index.
	 */
	public Object getItem(int index) {
		int count = 0;
		Node current = head;
		// if given index is negative, add list length to get actual value.
		index = realIndex(index);
		// loop and count until item is matched.
		while (current.nextNode != null && count != index) {
			count += 1;
			current = current.nextNode;
		}
		// return item at position index
		return current.data;
	}

	/**
	 * Returns a new LinkedList containing the contents of both lists,
	 * in the order in which they were originally added.
	 * 
	 * @param other another LinkedList to be append to
	 * @return a LinkedList containing the contents of both lists.
	 */
	public LinkedList add(LinkedList other) {
		// get the shallow copies of both lists.
		LinkedList selfCopy = copy();
		LinkedList otherCopy = other.copy();
		// connect the copies to create the sum of the lists.
		if (selfCopy.isEmpty()) {
			selfCopy.head = otherCopy.head;
		} else {
			selfCopy.tail().nextNode = otherCopy.head;
		}
		LinkedList sumList = selfCopy;
		// return sumList;
		return sumList;
	}

	public LinkedList mul(int n) {
		LinkedList mulList = new LinkedList();
		// loop and append copies of this list.
		for (int i = 0; i < n; ++i) {
			mulList = mulList.add(copy());
		}
		// return the multiplied list.
		return mulList;
	}

	/**
	 * Append the item to the end of this LinkedList.
	 * 
	 * @param item the item to be added to the end of this LinkedList.
	 */
	public void append(Object item) {
		// create the newNode.
		Node newNode = new Node(item);
		// if the list is empty, set newNode as head.
		if (head == null) {
			head = newNode;
		// otherwise, link the tailNode to the newNode.
		} else {
			tail().nextNode = newNode;
		}
	}
	
	/**
	 * Remove all items from this LinkedList.
	 */
	public void clear() {
		// remove all items from this list.
		head = null;
	}

	public boolean contains(Object item) {
		// loop until object is found in linked list.
		boolean found = false;
		Node current = head;
		while (current.nextNode != null && !found) {
			Object curItem = current.data;
			// if the items are the same, then the given item is found.
			if (MultitypeObjects.sameObjects(item, curItem)) {
				found = true;
			} else {
			// if item is not found yet, go to the nextNode.
				current = current.nextNode;
			}
		}
		// return true iff object is found in list.
		return found;
	}
	
	/**
	 * Build and return a shallow copy of this LinkedList.
	 * A shallow copy since data structures stored inside the new list
	 * can still be mutated.
	 * 
	 * @return a shallow copy of this LinkedList.
	 */
	public LinkedList copy() {
		// build a shallow copy of this list.
		LinkedList shallowCopy = new LinkedList();
		for (int selfIndex = 0; selfIndex < size(); selfIndex++) {
			shallowCopy.append(getItem(selfIndex));
		}
		// return the shallow copy of this list.
		return shallowCopy;
	}

	public int index(Object item) {
		int index = 0;
		Node current = head;
		// loop and count until item is matched.
		while (current.nextNode != null && current.data != item) {
			index += 1;
			current = current.nextNode;
		}
		// final count is the index of the item.
		return index;
	}
	
	public void insert(int item, int index) {
		index = realIndex(index);
		Node newNode = new Node(item);
		Node current = head;
		Node previous = null;
		int count = 0;
		// loop until the node at position index and its previous are found
		while (current.nextNode != null && count != index) {
			count += 1;
			previous = current;
			current = current.nextNode;
		}
		// if newNode is to be inserted at the end, append it.
		if (index >= size()) {
			append(item);
		// if newNode is to be inserted at head, set newNode as the head.
		} else if (index == 0) {
			newNode.nextNode = head;
			head = newNode;
		// otherwise, unlink the node at position index, link previous and next around.
		} else {
			previous.nextNode = newNode;
			newNode.nextNode = current;
		}
	}

	public Object pop(int index) {		
		int count = 0;
		Node current = head;
		Node previous = null;
		// loop until the node at position index and its previous are found
		while (current.nextNode != null && count != index) {
			count += 1;
			previous = current;
			current = current.nextNode;
		}
		// get the item and the next node.
		Object item = current.data;
		Node next = current.nextNode;
		// if the head to be removed, unlink the old head, set next as new head.
		if (current == head) {
			head.nextNode = null;
			head = next;
		// otherwise, unlink the node at position index, link previous and next around.
		} else {
			previous.nextNode = next;
		}
		// return item removed at position index.
		return item;
	}

	public Object pop() {
		return pop(lastIndex);
	}

		
	private int size(Node current) {
		// base case
		int count = 1;
		// recursive decomposition: n-1 approach
		if (current.nextNode != null) {
			count = 1 + size(current.nextNode);
		}
		return count;
	}
	
	public int size() {
		// create the counter
		int count = 0;
		// if list is not empty, recursively count
		if (!isEmpty()) {
			count = size(head);
		}
		// final count is list length.
		return count;
	}

	public LinkedList subList(int headIndex) {
		return subList(headIndex, lastIndex);
	}

	public LinkedList subList(int headIndex, int tailIndex) {
		headIndex = realIndex(headIndex);
		tailIndex = realIndex(tailIndex);
		LinkedList sliceLL = copy();
		Node sliceHead = sliceLL.getNode(headIndex);
		Node sliceTail = sliceLL.getNode(tailIndex);
		// if the sliced head is not at original head, unlink prevHead.
		if (headIndex > 0) {
			Node prevHead = sliceLL.getNode(headIndex-1);
			prevHead.nextNode = null;
		}
		// set the slice's head and remove the nodes after tail.
		sliceLL.head = sliceHead;
		sliceTail.nextNode = null;
		// return the sliced linked list.
		return sliceLL;
	}

	/**
	 * Returns whether or not this LinkedList has no items.
	 * @return true iff this LinkedList is empty.
	 */
	public boolean isEmpty() {
		// if the head is null, the list is empty
		return (head == null);
	}
	
}
