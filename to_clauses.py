#from to_CNF import convert_to_CNF
#from parser import to_parse
#import CNF
#import parser
from CNF import convert_to_CNF
from parser import to_parse

'''
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
'''

def print_tree(tree):
	if isinstance(tree, variable):
		print("variable")
		return str(tree.name)
	if isinstance(tree, negation):
		print("negation")
		return "(~"+print_tree(tree.left)+")"
	if isinstance(tree, conjunction):
		print("conjunction")
		return "("+print_tree(tree.left)+" /\ "+print_tree(tree.right)+")"
	if isinstance(tree, disjunction):
		print("disjunction")
		#print(tree.left)
		return "("+print_tree(tree.left)+" \/ "+print_tree(tree.right)+")"
	if isinstance(tree, implies):
		print("implies")
		return "("+print_tree(tree.left)+" -> "+print_tree(tree.right)+")"
	else:
		print("fuck", type(tree).__name__, type(tree), isinstance(tree, type(tree)))

def get_clauses():
	string = str(input("give formula : "))
	formulas = string.split(',')
	conclusion = formulas[-1].split('|-')[-1]
	formulas[-1] = formulas[-1].split('|-')[0]
	formulas.append('~(' + conclusion + ')')
	print(formulas)
	clauses = []
	for i in formulas:
		print("i is :", i)
		print('*'*10)
		print(print_tree(to_parse(i)))
		print('*'*10)
		print("CNF is :", convert_to_CNF(to_parse(i)))
		clauses.append(convert_to_CNF(to_parse(i)))
	print(clauses)

if __name__ == '__main__':
	get_clauses()
