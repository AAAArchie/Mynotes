class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def in_order_array(tree, array=[]):
    if tree is None:
        return []
    else:
        in_order_array(tree.left, array)
        array.append(tree.value)
        in_order_array(tree.right, array)
    return array


# 设置节点

a = BST(0)
print(a.left)
a.left = BST(1)
a.left.left = BST(2)
a.right = BST(3)
a.right.right = BST(4)

print(in_order_array(a))
