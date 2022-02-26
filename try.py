# import uuid
a = "dinesh"
print (a)
# count = 0
# class Node:
#
#     def __init__(self, data):
#
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
# # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#
#     @staticmethod
#     def count_nodes(node):
#         if node == None:
#             return 0
#         if node.data:
#             val = 1 + count_nodes(node.left) + count_nodes(node.right)
#         return val
#
#     @staticmethod
#     def print_static_tree(node):
#         if node.left:
#             node.print_static_tree(node.left)
#         print(node.data)
#         if node.right:
#             node.print_static_tree(node.right)
#
#
# # Print the tree
#     def PrintTree(self):
#         value = 1
#         if self.left:
#             self.left.PrintTree()
#         print( self.data)
#         if self.right:
#            self.right.PrintTree()
#
# def count_nodes(root):
#     if root == None:
#         return 0
#     if root.data:
#         val = 1 + count_nodes(root.left) + count_nodes(root.right)
#     return val
#
# def getfullCount(root):
#     if (root == None):
#         return 0
#     val = root.data
#     res = 0
#     lef = root.left
#     rig = root.right
#     if root.left and root.right:
#         res = res+ 1
#
#     res = res+(getfullCount(root.left) +
#             getfullCount(root.right))
#     return res
#
#
# root = Node(2)
# root.insert(7)
# root.insert(5)
# root.insert(6)
# root.insert(1)
# root.insert(11)
# root.insert(9)
# root.insert(4)
# # root.PrintTree()
# # print(count_nodes(root))
# Node.print_static_tree(root)
# print(Node.count_nodes(root))

# h1 = "dinesh"
# h2 = "sruthi"
# h3 = "ishan"
#
#
# def print_fun(*headers):
#     print(*headers)
#     for each_header in headers:
#         print(each_header)
#
# print_fun(h1,h2,h3)
print(uuid.uuid1())