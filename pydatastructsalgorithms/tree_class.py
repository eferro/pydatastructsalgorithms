
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

def preorder(root):
	if root:
		print "Root:", root.get_root_val()
		preorder(root.get_left_child())
		preorder(root.get_right_child())

def inorder(root):
	if root:
		inorder(root.get_left_child())
		print "Root:", root.get_root_val()
		inorder(root.get_right_child())

def postorder(root):
	if root:
		inorder(root.get_left_child())
		inorder(root.get_right_child())
		print "Root:", root.get_root_val()



# 		#In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree.

# def inorder
# 		#In an inorder traversal, we recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree.
# def postorder
# 		#In a postorder traversal, we recursively do a postorder traversal of the left subtree and the right subtree followed by a visit to the root node.