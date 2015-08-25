
class BinaryTree(object):
	__slots__ = ['root', 'left', 'right']

	def __init__(self, root):
		self.root = root
		self.left = None
		self.right = None

	def insert_left(self, value):
		act_left = self.left
		new = BinaryTree(value)
		if act_left:
			new.left = act_left
		self.left = new

	def insert_right(self, value):
		act_right = self.right
		new = BinaryTree(value)
		if act_right:
			new.right = act_right
		self.right = new	

	def get_root_val(self):
		return self.root

	def set_root_val(self, value):
		self.root = value

	def get_left_child(self):
		return self.left

	def get_right_child(self):
		return self.right
