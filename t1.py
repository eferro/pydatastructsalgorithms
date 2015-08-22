from pydatastructsalgorithms import tree

r = tree.binary_tree(3)
tree.insert_left(r, 4)
tree.insert_left(r, 5)
tree.insert_right(r, 6)
tree.insert_right(r, 7)

l = tree.get_left_child(r)
print l

print "---"
tree.set_root_val(l, 9)
print l
tree.insert_left(l, 11)
print l


print "---"
print r
print(tree.get_right_child(tree.get_right_child(r)))
