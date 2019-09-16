### General Information ###
# To use this red black tree implementation you need to use a class that has implemented all the methods
# to compare two items from that class. (__lt__, __eq__, etc.)
### General Information ###


### Static Methods ###
def get_from_subtree(subtree, key):
    """
    Find the value associated to the key in the given subtree
    :param subtree: the subtree to search in
    :param key: the key to search for
    :return: the value associated to the key in the given subtree or None if this key is not in the subtree
    """
    temp_subtree = subtree
    while temp_subtree is not None:
        if key == temp_subtree.key:
            return temp_subtree.value
        elif key < temp_subtree.key:
            temp_subtree = temp_subtree.left
        elif key > temp_subtree.key:
            temp_subtree = temp_subtree.right
    return None


def put_in_subtree(subtree, key, value):
    """
    Recursively put the key-value pair in the right place in the tree
    :param subtree: the subtree to put the key-value pair in
    :param key: the given key
    :param value: the given value
    :return: the subtree, or a new subtree if the given subtree was empty
    """
    if subtree is None:
        return RedBlackTree.Node(key, value, True, 1)

    if key < subtree.key:
        subtree.left = put_in_subtree(subtree.left, key, value)
    elif key > subtree.key:
        subtree.right = put_in_subtree(subtree.right, key, value)
    else:
        subtree.value = value

    # Make sure that the red black tree is correct
    if is_red(subtree.right) and not is_red(subtree.left):
        subtree = rotate_subtree_left(subtree)
    if is_red(subtree.left) and is_red(subtree.left.left):
        subtree = rotate_subtree_right(subtree)
    if is_red(subtree.left) and is_red(subtree.right):
        flip_subtree_colours(subtree)

    # Make sure that the subtree has the correct size
    subtree.size = size_node(subtree.left) + size_node(subtree.right) + 1

    return subtree


def is_red(node):
    """
    Check if this node is red
    :return: True if and only if this node is red and not None
    """
    if node is None:
        return False
    return node.colour is True


def size_node(node):
    """
    Check the size of this node
    :param node: the node to check
    :return: 0 if the node is None, the size of the node otherwise
    """
    if node is None:
        return 0
    return node.size


def rotate_subtree_right(subtree):
    """
    Rotate the subtree right
    :param subtree: the subtree to rotate
    :return: the new node at the top of the subtree
    """
    left = subtree.left
    subtree.left = left.right
    left.right = subtree
    left.colour = subtree.colour
    subtree.colour = True # set red
    left.size = subtree.size
    subtree.size = size_node(subtree.left) + size_node(subtree.right) + 1
    return left


def rotate_subtree_left(subtree):
    """
    Rotate the subtree left
    :param subtree: the subtree to rotate
    :return: the new node at the top of the subtree
    """
    right = subtree.right
    subtree.right = right.left
    right.left = subtree
    right.colour = subtree.colour
    subtree.colour = True # set red
    right.size = subtree.size
    subtree.size = size_node(subtree.left) + size_node(subtree.right) + 1
    return right


def flip_subtree_colours(subtree):
    """
    Flip the colours of this subtree and its children
    :param subtree: the subtree whose colours to flip
    """
    subtree.colour = not subtree.colour
    subtree.left.colour = not subtree.left.colour
    subtree.right.colour = not subtree.right.colour
### Static Methods ###


### Red Black Tree ###
class RedBlackTree:
    def __init__(self):
        """
        Initialise this tree
        """
        self.root = None

    class Node:
        def __init__(self, key, value, colour, size):
            """
            Initialise this node
            :param key: the key
            :param value: the value
            :param colour: the colour of this node
            :param size: the size of this subtree
            """
            self.key = key
            self.value = value
            self.colour = colour
            self.size = size
            # initialise empty left and right subtrees
            self.left = None
            self.right = None

    def size(self):
        """
        Check the size of this tree
        :return: 0 if the root is None, the size of this tree otherwise
        """
        if self.root is None:
            return 0
        return self.root.size

    def get(self, key):
        """
        Find and return the value associated to the key
        :param key: the key to search for
        :return: the value associated to this key or None if this key is not in the tree
        """
        if key is None:
            return None # None is not a valid key
        return get_from_subtree(self.root, key)

    def put(self, key, value):
        """
        Add the given key-value pair to the tree
        :param key: the given key
        :param value: the given value
        :return: If the key is None, the tree remains unchanged, otherwise the key-value pair is added to the tree,
        possibly overwriting a node with the same key
        """
        if key is None:
            return
        self.root = put_in_subtree(self.root, key, value)
        self.root.colour = False # make sure that the root is black
### Red Black Tree ###