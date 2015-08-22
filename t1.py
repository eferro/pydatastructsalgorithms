from pydatastructsalgorithms import tree

r = tree.binary_tree(3)
print r
tree.insert_left(r, 4)
print r
tree.insert_left(r, 5)
print r

tree.insert_right(r, 6)
print r
tree.insert_right(r, 7)
print r

print "---"
