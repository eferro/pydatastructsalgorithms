

def binary_tree(root):
	return [root, [], []]

def insert_left(root, val):
	act_left = root.pop(1)
	if len(act_left) > 1:
		root.insert(1, [val, act_left, []])
	else:
		root.insert(1, [val, [], []])

def insert_right(root, val):
	act_right = root.pop(2)
	if len(act_right) > 1:
		root.insert(2, [val, [], act_right])
	else:
		root.insert(2, [val, [], []])

def get_root_val(root):
	return root[0]

def set_root_val(root, val):
	root[0] = val

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]