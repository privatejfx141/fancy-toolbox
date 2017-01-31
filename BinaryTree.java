/**
 * BinaryTree is an implementation of a binary tree ADT.
 * 
 * @author Jeffrey Li
 * @version 1.0
 * @since 2017-01-27
 */
public class BinaryTree {

	protected class Node {
		Integer data;
		Node leftChild, rightChild;
		// Node constructor
		Node(Integer data) {
			this.data = data;
		}
		/**
		 * Builds and returns the string representation of this node.
		 * 
		 * @return the string representation of this node.
		 */
		public String toString() {
			return "Node(" + MultitypeObjects.toString(data) + ")";
		}
		/**
		 * Unlinks all child nodes from this node.
		 */
		public void unlink() {
			leftChild = null;
			rightChild = null;
		}
		/**
		 * Returns whether or not this node is a leaf node.
		 * A leaf is a bottom-most node in a tree, with no children. 
		 * 
		 * @return true iff this node is a leaf.
		 */
		public boolean isLeaf() {
			return (leftChild == null && rightChild == null);
		}
	}

	protected Node root;
	protected String name;
	protected final int left = 0;
	protected final int right = 1;
	
	// BinaryTree constructor
	/**
	 * Constructor for this <code>BinaryTree</code>.
	 * 
	 * @param seed
	 */
	BinaryTree(Integer seed) {
		// representation invariant
		// 
		this.root = new Node(seed);
		this.name = "BinaryTree";
	}
	
	public String toString() {
		String treeString = this.name + "(";
		treeString += "root " + root.data + ", ";
		treeString += "size " + size() + ", ";
		treeString += "height " + height() + ")";
		return treeString;
	}
	
	/**
	 * Recursively counts and returns the height of this <code>BinaryTree</code>.
	 * The height is the number of <code>Object</code>s in the longest branch of this tree.
	 * 
	 * @param curNode the current <code>Node</code>.
	 * @return the current iteration of the height at <code>curNode</code>.
	 */
	private int height(Node curNode) {
		// base case
		Integer count = 0;
		// recursive decomposition: n-1 approach
		Integer leftHgt = curNode.leftChild == null ? 0 : height(curNode.leftChild);
		Integer rightHgt = curNode.rightChild == null ? 0 : height(curNode.rightChild);
		// add the longest sub-height to the count.
		count += 1 + (leftHgt >= rightHgt ? leftHgt : rightHgt);
		// final count is tree height.
		return count;
	}
	
	/**
	 * Calculates and returns the height of this <code>BinaryTree</code>.
	 * The height is the number of <code>Object</code>s in the longest branch of this tree.
	 * 
	 * @return the height of this tree.
	 */
	public int height() {
		return (isSapling() ? 1 : height(root));
	}
	
	/**
	 * 
	 * @param curNode
	 * @return
	 */
	private int size(Node curNode) {
		// base case
		Integer count = 1;
		// recursive decomposition
		Integer leftHgt = curNode.leftChild == null ? 0 : height(curNode.leftChild);
		Integer rightHgt = curNode.rightChild == null ? 0 : height(curNode.rightChild);
		count += leftHgt + rightHgt;
		// final count is the size of this tree.
		return count;
	}
	
	/**
	 * Calculates and returns the size of this <code>BinaryTree</code>,
	 * which is the number of item <code>Object</code>s in this list.
	 * 
	 * @return the number of item <code>Object</code>s in this <code>BinaryTree</code>.
	 */
	public int size() {
		return size(root);
	}
	
	/**
	 * 
	 * @return
	 */
	public boolean isSapling() {
		return root.isLeaf();
	}
	
	/**
	 * 
	 * @param curNode
	 * @return
	 */
	private String preOrder(Node curNode) {
		String str = ".";
		if (curNode != null) { str += "|";
			str += curNode.data.toString();
			str += preOrder(curNode.leftChild);
			str += preOrder(curNode.rightChild);
		}
		return str;	
	}
	
	/**
	 * Generate the contents of this <code>BinaryTree</code> pre-order.
	 * 
	 * @return the <code>String</code> of the items concatenated pre-order.
	 */
	public String preOrder() {
		return preOrder(root);
	}
	
	/**
	 * 
	 * 
	 * @param curNode
	 * @return
	 */
	private String inOrder(Node curNode) {
		String str = ".";
		if (curNode != null) { str += "|";
			str += inOrder(curNode.leftChild);
			str += curNode.data.toString();
			str += inOrder(curNode.rightChild);
		}
		return str;
	}
	
	/**
	 * Generate the contents of this BinaryTree in-order.
	 * 
	 * @return the String of the items concatenated in-order.
	 */
	public String inOrder() {
		return inOrder(root);
	}
	
	private String postOrder(Node curNode) {
		String str = ".";
		if (curNode != null) { str += "|";
			str += postOrder(curNode.leftChild);
			str += postOrder(curNode.rightChild);
			str += curNode.data.toString();
		}
		return str;
	}
	
	/**
	 * Generate the contents of this BinaryTree post-order.
	 * 
	 * @return the String of the items concatenated post-order.
	 */
	public String postOrder() {
		return postOrder(root);
	}
	
	/**
	 * 
	 * @param curNode
	 * @param level
	 * @return
	 */
	private String buildTree(Node curNode, int level) {
		
		String strTree = "";
		String tab = "";
		for (int i=0; i<level; i++) {
			tab += "\t";
		}
		strTree = tab + MultitypeObjects.toString(curNode.data) + "\n";
		if (curNode.leftChild != null) {
			strTree += buildTree(curNode.leftChild, level+1);
		}
		if (curNode.rightChild != null) {
			strTree += buildTree(curNode.rightChild, level+1);
		}
		return strTree;
		
	}
	
	/**
	 * Builds and prints this <code>BinaryTree</code>.
	 */
	public void printTree() {
		String strTree = buildTree(root, 0);
		System.out.println(strTree);
	}
	
}

class BST extends BinaryTree {

	/**
	 * Constructor for <code>BinarySearchTree</code>.
	 * @param seed
	 * @param items
	 */
	BST(Integer seed, Integer... items) {
		super(seed);
		this.name = "BinarySearchTree";
		for (Integer item : items) {
			insert(item);
		}
	}
	
	private void insert(Integer data, Node curNode) {
		// create the new node to add.
		Node newNode = new Node(data);
		// if data is less than curNode.data, focus on leftChild.
		if (data < curNode.data) {
			// if there is no leftChild, link the data.
			if (curNode.leftChild == null) {
				curNode.leftChild = newNode;
			} else {
				// otherwise, recursively traverse to the leftChild.
				insert(data, curNode.leftChild);
			}
		}
		// if data is greater than curNode.data, focus on rightChild.
		else if (data >= curNode.data) {
			// if there is no rightChild, link the data.
			if (curNode.rightChild == null) {
				curNode.rightChild = newNode;
			} else {
				// otherwise, recursively traverse to the rightChild.
				insert(data, curNode.rightChild);
			}
		}
	}
	
	public void insert(Integer... dataList) {
		// start recursion for insertion at rootNode.
		for (Integer data : dataList) {
			insert(data, root);
		}
	}
	
}