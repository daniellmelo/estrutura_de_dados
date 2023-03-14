from python.tree.BinaryTree import BinaryTree
from python.tree.Node import Node

#         30 (n1 - root)
#       /    \
#     33     36
#    /  \    / \
#  41   44  47  52
#              /
#             55


tree2 = BinaryTree()
n1 = Node(30)
n2 = Node(33)
n3 = Node(36)
n4 = Node(41)
n5 = Node(44)
n6 = Node(47)
n7 = Node(52)
n8 = Node(55)


n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n7.left = n8

tree2.root = n1

tree2.postorder_traversal()

print(tree2.height())
