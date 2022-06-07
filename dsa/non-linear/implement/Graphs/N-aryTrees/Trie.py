"""
Aka prefix tree
Rooted out-tree
"""
class Node:
	def __init__(self, letter):
		self.letter = letter
		self.children = {}
		self.endOfWord = False
		# self.occurence = 1
		
class Trie:
	def __init__(self):
		self.root = Node("")

	# Depth first Search Approach
	# add a word to the trie
	def addWord(self, word):
		# start at the root node, before streamlining
		currNode = self.root
		# add each letter to the trie
		for letter in word:
			# find out if letter exists in trie
			if letter not in currNode.children:
				currNode.children[letter] = Node(letter)
			currNode = currNode.children[letter]
		currNode.endOfWord = True

	def query(self, prefix):
		currNode = self.root
		self.__suggestions = []

		if not currNode.children:
			return self.__suggestions
		
		"""
		find the node path with the prefix
		"""
		for letter in prefix:
			if letter in currNode.children:
				currNode = currNode.children[letter]
			else:
				return self.__suggestions

		self.__dft__(currNode, prefix)
		
		return self.__suggestions

	def __dft__(self, node, prefix):
		
		if node.endOfWord:
			self.__suggestions.append(prefix)
		for childNode in node.children.values():
			self.__dft__(childNode, prefix+childNode.letter)


googleSearch = Trie()
textHistory = ["wallet", "wallet for men", "wallet for women", "wall", "chicken", "vegan chicken", "vegan wallet", "wallet vegan", "vegan wall", "vegan alternatives", "vegan", "wallet phone case", "vegan phone case", "wallet card", "vegan restaurant", "vegan restaurants in my area", "progress", "progressive", "program","progressive meaning", "programming"]

for word in textHistory:
	googleSearch.addWord(word)

def autocomplete(word):
	print("\nUser is typing: ", word)
	print("Suggestions:")
	for i,suggestion in enumerate(googleSearch.query(word)):
		print(f"\t{i}.{suggestion}")

autocomplete("vega")
autocomplete("wa")
autocomplete("progr")