"""
A n-ary tree is a rooted tree in which each node has at most n children. 2-ary trees are often called binary trees, while 3-ary trees are sometimes called ternary trees.

usually out-trees
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
		for child in self.children:
			child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Surface"))
laptop.add_child(TreeNode("Thinkpad"))

cellphone = TreeNode("Cell Phone")
cellphone.add_child(TreeNode("iPhone"))
cellphone.add_child(TreeNode("Google Pixel"))
cellphone.add_child(TreeNode("Vivo"))

tv = TreeNode("TV")
tv.add_child(TreeNode("Samsung"))
tv.add_child(TreeNode("LG"))

root.add_child(laptop)
root.add_child(cellphone)
root.add_child(tv)

root.print_tree()