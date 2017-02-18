class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_node_value(self, value):
        self.value = value

    def get_node_value(self):
        return self.value

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.right = self.right
            self.right = tree

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            self.left = tree
            tree.left = self.left

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1


def print_tree(tree):
    if tree:
        print_tree(tree.get_left_child())
        print(tree.get_node_value()),
        print_tree(tree.get_right_child())


# test tree

if __name__ == '__main__':
    """myTree = BinaryTree("Maud")
    myTree.insert_left("Bob")
    myTree.insert_right("Tony")
    myTree.insert_right("Steven")
    print_tree(myTree)
    """
    print 'Enter your tree:'
    li = [int(x) for x in raw_input().split()]
    my_tree = BinaryTree(li[0])
    for i in li[1:]:
        my_tree.insert(i)
    print_tree(my_tree)
    print '\n Height is: {0}'.format(height(my_tree))

