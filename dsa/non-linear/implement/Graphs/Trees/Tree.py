"""
Trees are graphs, more specifically , they are connected acyclic, and generally undirected, graphs.

Tree  constraints:
- n nodes, n-1 edges (All nodes have exactly one parent, except the topmost root node, which has none.)
- acyclic 

Each non-root node can be treated as the root node of its own subtree, which includes that node and all its descendants 

General Tree Representations are similar to graphs
1. EdgeList
2. Adjacency List
3. Adjacency Matrix

-------- ROOTED TREES --------
'A rooted tree is a tree in which one node has been designated the root.'
- in-tree  (directed edges towards the root node )
- out-tree (directed edges away from the root node )

In dsa, we generally think of trees as hierarchal out-trees.

			 ()         --> root node
		()        ()    --> child nodes
	 ()    ()  ()    () --> leaf nodes

Key words:
---------
1. Neighbor :- Parent or child.
2. Ancestor :- A node reachable by repeated proceeding from child to parent.
3. Descendant :- A node reachable by repeated proceeding from parent to child. Also known as subchild.
4. Degree :- For a given node, its number of children. A leaf has necessarily degree zero.
5. Degree of tree
The degree of a tree is the maximum degree of a node in the tree.
6. Distance :- The number of edges along the shortest path between two nodes.
7. Level :- The level of a node is the number of edges along the unique path between it and the root node.This is the same as depth when using zero based counting.
8. Width :- The number of nodes in a level.
9. Breadth :- The number of leaves.
10. Forest :- A set of one or more disjoint trees.
11. Size of a tree :- Number of nodes in the tree.
12. Height :- The height of a node is the length of the longest downward path to a leaf from that node. The height of the root is the height of the tree. 
13. Depth :- The depth of a node is the length of the path to its root (i.e., its root path). When using zero-based counting, the root node has depth zero, leaf nodes have height zero, and a tree with only a single node (hence both a root and leaf) has depth and height zero. Conventionally, an empty tree (tree with no nodes, if such are allowed) has height −1.
"""

# add traversal 

# -------- directed, unordered, tree
generalTree = {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

# -------- undirected, unordered rooted tree
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
cellphone = TreeNode("Cell Phone")
laptop = TreeNode("Laptop")
tv = TreeNode("TV")

laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Surface"))
laptop.add_child(TreeNode("Thinkpad"))

cellphone.add_child(TreeNode("iPhone"))
cellphone.add_child(TreeNode("Google Pixel"))
cellphone.add_child(TreeNode("Vivo"))

tv.add_child(TreeNode("Samsung"))
tv.add_child(TreeNode("LG"))

root.add_child(laptop)
root.add_child(cellphone)
root.add_child(tv)

root.print_tree()