from pydatastructsalgorithms import tree_class as tree


# r = tree.BinaryTree('a')
# print r.get_root_val()
# print r.get_left_child()
# r.insert_left('b')
# print r.get_left_child()
# print r.get_left_child().get_root_val()
# r.insert_right('c')
# print r.get_right_child()
# print r.get_right_child().get_root_val()
# print r.get_right_child().set_root_val('hello')
# print r.get_right_child().get_root_val()


r = tree.BinaryTree('a')
r.insert_left('b')
r.get_left_child().insert_right('d')
r.insert_right('c')
r.get_right_child().insert_left('e')
r.get_right_child().insert_right('f')

print r

print "preorder"
tree.preorder(r)

print "inorder"
tree.inorder(r)
