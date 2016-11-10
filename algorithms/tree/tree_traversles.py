class Tree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_print(node_list):
    level_values = []
    child_list = []
    for node in node_list:
        level_values.append(str(node.val))
        if node.left:
            child_list.append(node.left)
        if node.right:
            child_list.append(node.right)
    print " ".join(level_values)
    if child_list:
        level_order_print(child_list)


def in_order_traverse(node):
    if node is not None:
        in_order_traverse(node.left)
        print node.val,
        in_order_traverse(node.right)


def pre_order_traverse(node):
    if node is not None:
        print node.val,
        pre_order_traverse(node.left)
        pre_order_traverse(node.right)


def post_order_traverse(node):
    if node is not None:
        post_order_traverse(node.left)
        post_order_traverse(node.right)
        print node.val,


def level_order_traverse(root_node):
    li = []
    curr_level = [root_node]
    # print root_node.val
    # li.append(root_node.val)
    while curr_level:
        next_level = []
        for node in curr_level:
            #print node.val,
            li.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        # print
        curr_level = next_level
    return li


def bottom_up_level_order_traverse(root_node):

    height = tree_height(root_node)
    for i in range(height, 0, -1):
        li = get_given_level_nodes(root_node, i)
        print li,
    #li = []
    #return li


# Print nodes at a given level
def get_given_level_nodes(root, level, li=None):
    if root is None:
        return
    if level == 1:
        #print root.val,
        li.append(root.val)

    elif level > 1:
        get_given_level_nodes(root.left, level - 1, li)
        get_given_level_nodes(root.right, level - 1, li)

    return li


def tree_height(root_node):
    if root_node is None:
        return 0
    else:
        return max(tree_height(root_node.left), tree_height(root_node.right)) + 1

if __name__ == '__main__':
    t = Tree(50, Tree(20, Tree(10), Tree(30)), Tree(70, Tree(60), Tree(90)))

    print '****** In order Traverse ******'
    in_order_traverse(t)

    print '\n ****** Pre order Traverse ******'
    pre_order_traverse(t)

    print '\n ****** Post order Traverse ******'
    post_order_traverse(t)

    print '****** Level order Traverse ******'
    print level_order_traverse(t)

    print '****** Bottom Up Level order Traverse ******'
    bottom_up_level_order_traverse(t)


#                      50
#                  20      70
#               10    30  60  90
#
#          level_order_print:
#          50, 20, 70, 10, 30, 60, 90
