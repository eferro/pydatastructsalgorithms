from pydatastructsalgorithms import tree

# r = tree.binary_tree(3)
# tree.insert_left(r, 4)
# tree.insert_left(r, 5)
# tree.insert_right(r, 6)
# tree.insert_right(r, 7)
# l = tree.get_left_child(r)
# tree.set_root_val(l, 9)
# tree.insert_left(l, 11)
# print(tree.get_right_child(tree.get_right_child(r)))


x = tree.binary_tree('a')
tree.insert_left(x, 'b')
tree.insert_right(x, 'c')
print x

tree.insert_right(tree.get_right_child(x), 'd')
print x
tree.insert_left(tree.get_right_child(tree.get_right_child(x)), 'e')
print x