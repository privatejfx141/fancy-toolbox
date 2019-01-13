/**
 * <code>LinkedList</code> is an implementation of a pythonic linked list ADT.
 * 
 * @author Jeffrey L.
 * @version 1.1
 * @since 2017-01-26
 */
public class LinkedList {
	// linked list of nodes holding Objects.

	/**
	 * <code>Node</code> is an implementation of a linked node containing data.
	 * 
	 * @author Jeffrey L.
	 * @version 1.1
	 * @since 2017-01-26
	 */
	protected class Node {
		/*
		 * Representation invariant:
		 * data is an object.
		 * nextNode is the pointer to the next node.
		 */
		Object data;
		Node nextNode;
		/**
		 * Constructor for this <code>Node</code>.
		 * 
		 * @param item the given item <code>Object</code> for the Node to hold.
		 */
		Node(Object item) {
			// create an unlinked node with data.
			this.data = item;
		}
		public String toString() {
			// return the string representation of this node.
			return "Node(" + data + ")";
		}
	}

	protected Node head;
	protected final int lastIndex = -1;

	/**
	 * Constructor for this <code>LinkedList</code>.
	 * 
	 * @param datas unlimited arguments of item <code>Object</code>s to initialize with.
	 */
	LinkedList(Object... values) {
		/*
		 * Representation invariant:
		 * values is a varargs of objects,
		 * which are to be the items stored in me.
		 * size() is the number of items in me.
		 * if size() > 0 then,
		 *   head is the first Node in me.
		 *   tail() is the last Node in me.
		 */
		for (Object data : values) {
			append(data);
		}
	}

	/**
	 * Calculates and returns the actual position <code>index</code> value
	 * iff the given <code>index</code> is negative.
	 * 
	 * @param index given position <code>index</code>.
	 * @return actual <code>index</code> value iff <code>index</code> is negative.
	 */
	protected int realIndex(int index) {
		// if index is negative, add size to get realIndex.
		if (index < 0) {
			index += size();
		}
		return index;
	}

	/**
	 * Traverses and returns the <code>Node</code> in this <code>LinkedList</code>
	 * at the given position <code>index</code>.
	 * 
	 * @param index the given position <code>index</code>.
	 * @return the <code>Node</code> at position <code>index</code> in this
	 * <code>LinkedList</code>
	 */
	protected Node getNode(int index) {
		index = realIndex(index);
		// create a counter and the node 'counter'
		Node curNode = head;
		int count = 0;
		// while loop until last node is reached or counter matches.
		while (curNode != null && count != index) {
			count += 1;
			curNode = curNode.nextNode;
		}
		// return the node reached.
		return curNode;
	}
	
	/**
	 * Traverses and returns the <code>tailNode</code>, the last <code>Node</code>,
	 * of this <code>LinkedList</code>.
	 * 
	 * @return the <code>tailNode</code> of this list.
	 */
	protected Node tail() {
		// the last node reached is the tailNode.
		return getNode(lastIndex);
	}
	
	/**
	 * Recursively traverses and builds the <code>String</code> representation
	 * of this <code>LinkedList</code>.
	 * 
	 * @param curNode the current <code>Node</code>.
	 * @return the current iteration of the <code>String</code> representation.
	 */
	private String toString(Node curNode) {
		// base case
		String repr = curNode.data == null ? "null" : curNode.data.toString();
		// recursive decomposition: n-1 approach
		if (curNode.nextNode != null) {
			repr += ", " + toString(curNode.nextNode);
		}
		return repr;
	}
	
	/**
	 * Returns the <code>String</code> representation of this <code>LinkedList</code>,
	 * enclosed in square brackets.
	 */
	public String toString() {		
		return "[" + (isEmpty() ? "" : toString(head)) + "]";
	}
	
	/**
	 * Returns the item in this <code>LinkedList</code> at position <code>index</code>.
	 * 
	 * @param index the position <code>index</code> where an item is to be found.
	 * @return the item <code>Object</code> at position <code>index</code>.
	 */
	public Object getItem(int index) {
		// get the Node at position index and return its item.
		return getNode(index).data;
	}

	/**
	 * Returns a new <code>LinkedList</code> containing the contents of both lists,
	 * in the order in which they were originally added.
	 * 
	 * @param other another <code>LinkedList</code> to be append to
	 * @return a <code>LinkedList</code> containing the contents of both lists.
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

	/**
	 * Builds and returns a shallow copy of this <code>LinkedList</code>, where all item
	 * <code>Object</code>s in this list are duplicated <code>n</code> times.
	 * 
	 * @param n <code>integer</code> for multiplier.
	 * @return the shallow copy of this list where all items are duplicated
	 * <code>n</code> times.
	 */
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
	 * Append the item to the end of this <code>LinkedList</code>.
	 * 
	 * @param item the item to be added to the end of this <code>LinkedList</code>.
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
	 * Removes all item <code>Object</code>s from this <code>LinkedList</code>.
	 */
	public void clear() {
		// remove all items from this list.
		head = null;
	}

	/**
	 * Returns a <code>boolean</code> determining whether or not the given
	 * item object exists in this <code>LinkedList</code>.
	 * @param item the given item object to be searched for.
	 * @return <code>true</code> iff the item exists in the list.
	 */
	public boolean contains(Object item) {
		// loop until object is found in linked list.
		boolean found = false;
		Node curNode = head;
		while (curNode.nextNode != null && !found) {
			Object curItem = curNode.data;
			// if the items are the same, then the given item is found.
			if (MultitypeObjects.sameObjects(item, curItem)) {
				found = true;
			} else {
			// if item is not found yet, go to the nextNode.
				curNode = curNode.nextNode;
			}
		}
		// return true iff object is found in list.
		return found;
	}
	
	/**
	 * Build and return a shallow copy of this <code>LinkedList</code>.
	 * The returned <code>Object</code> is a shallow copy since data structures stored
	 * inside the new list can still be mutated.
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

	/**
	 * Finds and returns the position <code>index</code> of the
     * given item in this <code>LinkedList</code>.
	 * 
	 * @param item the item whose index is to be found.
	 * @return the position index of the item in this LinkedList.
	 */
	public int index(Object item) {
		int index = 0;
		Node curNode = head;
		// loop and count until item is matched.
		while (curNode.nextNode != null && curNode.data != item) {
			index += 1;
			curNode = curNode.nextNode;
		}
		// final count is the index of the item.
		return index;
	}
	
	/**
	 * Inserts the given item <code>Object</code> at position <code>index</code>.
	 * 
	 * @param item the item <code>Object</code> to be inserted.
	 * @param index the position <code>index</code> of where the item
	 * is to be inserted at.
	 */
	public void insert(int item, int index) {
		index = realIndex(index);
		Node newNode = new Node(item);
		Node curNode = head;
		Node prevNode = null;
		int count = 0;
		// loop until the node at position index and its previous are found
		while (curNode.nextNode != null && count != index) {
			count += 1;
			prevNode = curNode;
			curNode = curNode.nextNode;
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
			prevNode.nextNode = newNode;
			newNode.nextNode = curNode;
		}
	}

	/**
	 * Removes and returns the <code>item</code> object at the
     * given position <code>index</code>.
     * 
	 * @param index the given position <code>index</code>.
	 * @return the item at the given position <code>index</code>.
	 */
	public Object pop(int index) {		
		int count = 0;
		Node curNode = head;
		Node prevNode = null;
		// loop until the node at position index and its previous are found
		while (curNode.nextNode != null && count != index) {
			count += 1;
			prevNode = curNode;
			curNode = curNode.nextNode;
		}
		// get the item and the next node.
		Object item = curNode.data;
		Node next = curNode.nextNode;
		// if the head to be removed, unlink the old head, set next as new head.
		if (curNode == head) {
			head.nextNode = null;
			head = next;
		// otherwise, unlink the node at position index, link previous and next around.
		} else {
			prevNode.nextNode = next;
		}
		// return item removed at position index.
		return item;
	}

	/**
	 * Removes and returns the very last item <code>Object</code>
	 * in this <code>LinkedList</code>.
	 * 
	 * @return the item object at the position <code>-1</code>.
	 */
	public Object pop() {
		return pop(lastIndex);
	}

	/**
	 * Recursively traverses and counts the number of item <code>Object</code>s
	 * in this <code>LinkedList</code>.
	 * 
	 * @param curNode the current <code>Node</code>.
	 * @return the current count of the number of <code>Object</code>s.
	 */
	private int size(Node curNode) {
		// base case
		int count = 1;
		// recursive decomposition: n-1 approach
		if (curNode.nextNode != null) {
			count = 1 + size(curNode.nextNode);
		}
		return count;
	}
	
	/**
	 * Calculates and returns the size of this <code>LinkedList</code>,
	 * which is the number of item <code>Object</code>s in this list.
	 * 
	 * @return the number of item <code>Object</code>s in this <code>LinkedList</code>.
	 */
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

	/**
	 * Returns a <code>LinkedList</code> that is a <code>subList</code> of this list.
	 * The <code>subList</code> begins with the character at the specified
	 * <code>headIndex</code> and extends to the end of this list.
	 * 
	 * @param headIndex the beginning <code>index</code>, inclusive.
	 * @return the specified <code>subList</code>.
	 */
	public LinkedList subList(int headIndex) {
		return subList(headIndex, lastIndex);
	}
	
	/**
	 * Returns a <code>LinkedList</code> that is a <code>subList</code> of this list.
	 * The <code>subList</code> begins with the character at the specified
	 * <code>headIndex</code> and extends to the <code>tailIndex</code>.
	 * 
	 * @param headIndex the beginning <code>index</code>, inclusive.
	 * @param tailIndex the ending <code>index</code>, exclusive.
	 * @return the specified <code>subList</code>.
	 */
	public LinkedList subList(int headIndex, int tailIndex) {
		headIndex = realIndex(headIndex);
		tailIndex = realIndex(tailIndex) - 1;
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
	 * Returns a <code>boolean</code> determining whether or not this
	 * <code>LinkedList</code> has no items.
	 * 
	 * @return <code>true</code> iff this <code>LinkedList</code> is empty.
	 */
	public boolean isEmpty() {
		// if the head is null, the list is empty
		return (head == null);
	}
	
}


class CLList extends LinkedList {
	
	CLList(Object... items) {
		super(items);
	}
	
	public void append(Object item) {
		super.append(item);
		tail().nextNode = head;
	}
	
	public void insert(int index, Object item) {
		
	}
	
}


class DLList extends LinkedList {
	
	protected class DLNode extends Node {
		Node prevNode;
		DLNode(Object item) {
			super(item);
		}
		public String toString() {
			// return the string representation of this node.
			return "DL" + super.toString();
		}
	}
	
}
