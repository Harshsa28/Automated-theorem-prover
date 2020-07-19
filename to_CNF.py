class variable:
	def __init__(self, name):
		self.name = name
		self.left = None
		self.right = None

class negation:
	def __init__(self, left):
		self.left = left
		self.right = None

class conjunction:
	def __init__(self, left, right):
		self.left = left
		self.right = right

class disjunction:
	def __init__(self, left, right):
		self.left = left
		self.right = right

class implies:
	def __init__(self, left, right):
		self.left = left
		self.right = right

def to_NNF (tree):
	if isinstance(tree, implies):
		return disjunction(negation(to_NNF(tree.left)), to_NNF(tree.right))
	else:
		return tree

def to_CNF(tree):
	if isinstance(tree, negation):
		if isinstance(tree.left, negation):
			return to_CNF(tree.left.left)
		if isinstance(tree.left, conjunction):
			return disjunction(negation(to_CNF(tree.left.left)), negation(to_CNF(tree.left.right)))
		if isinstance(tree.left, disjunction):
			return conjunction(negation(to_CNF(tree.left.left)), negation(to_CNF(tree.left.right)))
		if isinstance(tree.left, variable):
			return tree
	if isinstance(tree, variable):
		return tree
	#if isinstance(tree, negation):
	#	if isinstance(tree.left, variable):
	#		return tree
	#	else:
	#		print("I screwed up in to_CNF -> is isinstance (tree, negation)")
	if isinstance(tree, conjunction):
		return conjunction(to_CNF(tree.left), to_CNF(tree.right))
	if isinstance(tree, disjunction):
		tree = disjunction(to_CNF(tree.left), to_CNF(tree.right))
		if isinstance(tree.left, conjunction):
			return conjunction(to_CNF(disjunction(tree.left.left, tree.right)), to_CNF(disjunction(tree.left.right, tree.right))) 
		elif isinstance(tree.right, conjunction):
			return conjunction(to_CNF(disjunction(tree.left, tree.right.left)), to_CNF(disjunction(tree.left, tree.right.right)))
		else:
			return tree
	
def print_tree(tree):
	if isinstance(tree, variable):
		return str(tree.name)
	if isinstance(tree, negation):
		return "(~"+print_tree(tree.left)+")"
	if isinstance(tree, conjunction):
		return "("+print_tree(tree.left)+" /\ "+print_tree(tree.right)+")"
	if isinstance(tree, disjunction):
		print(tree.left)
		return "("+print_tree(tree.left)+" \/ "+print_tree(tree.right)+")"
	if isinstance(tree, implies):
		return "("+print_tree(tree.left)+" -> "+print_tree(tree.right)+")"



formula_1 = disjunction(conjunction(variable("a"), variable("b")), conjunction(variable("c"), variable("d")))
formula_2 = disjunction(disjunction(conjunction(variable("a"), variable("b")), conjunction(variable("c"), variable("d"))), disjunction(conjunction(variable("e"), variable("f")), conjunction(variable("g"), variable("h"))))
formula_3 = implies(implies(variable("p"), variable("q")), variable("r"))
formula_4 = implies(implies(variable("p"), variable("q")), implies(negation(variable("q")), negation(variable("p"))))
print(print_tree(formula_1))
print(print_tree(to_CNF(to_NNF(formula_1))))




























