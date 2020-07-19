import sys

class variable:
	def __init__(self, name):
		self.name = name
		self.left = None
		self.right = None
		#self.id = "variable"

class negation:
	def __init__(self, left):
		self.left = left
		self.right = None
		#self.id = "negation"

class conjunction:
	def __init__(self, left, right):
		self.left = left
		self.right = right
		#self.id = "conjunction"

class disjunction:
	def __init__(self, left, right):
		self.left = left
		self.right = right
		#self.id = "disjunction"

class implies:
	def __init__(self, left, right):
		self.left = left
		self.right = right
		#self.id = "implies"

def get_var(string, index):
	while (string[index] == ' '):
		index += 1
	var = ""
	while ((index < len(string)) and string[index].isalnum()):
		var += string[index]
		index += 1
	#if var == "":
	#	index += 1
	#	while ((index < len(string)) and string[index].isalnum()):
	#		var += string[index]
	#		index += 1
	return [string, index, var]

def get_sym(string, index):
	while (string[index] == ' '):
		index += 1
	symbol = ""
	#while (string[index] != ' ' and string[index] != ')' and string[index] != '(' and not string[index].isalnum): 
	while (string[index] not in ['', '(', ')'] and not string[index].isalnum()):
		symbol += string[index]
		index += 1
	return [string, index, symbol]

def check_not (string, index):
	symbol = ""
	[string, index, symbol] = get_sym (string, index)
	if symbol == "~":
		print("check returning 1 and symbol is :", symbol)
		return 1
	else:
		print("check ret 0 and symbol is :", symbol)
		return 0


def check_var (string, index):
	while (string[index] == ' '):
		index += 1
	[string, index, symbol] = get_sym(string, index)
	if symbol not in ['~', '/\\', '\\/', '->', '']:
		return 1
	elif symbol == "":
		index += 1
		[string, index, symbol] = get_sym(string, index)
		if symbol not in ['~', '/\\', '\\/', '->', '']:
			return 1
	else:
		print("fuck, symbol is :", symbol)
	return 0



def parse(string, index): 
	print("string is :", string[index:])
	while (string[index] == ' '):
		index += 1
	if string[index] == ')':
		print("error in string[index] in parse")
		sys.exit()
	if string[index] != '(':
		var = ""
		[string, index, var] = get_var (string , index)
		p = variable(var)
		return [string, index, p]
	if string[index] == '(':
		index += 1
	if check_not (string , index) == 0:
		#if check_var(string, index) == 1:
		#	var = ""
		#	[string, index, var] = get_var(string, index)
		#	p = variable(var)
		#	return [string, index, p]
		[string, index, left] = parse (string, index)
		[string, index, symbol] = get_sym(string, index)
		[string, index, right] = parse(string, index)
	else:
		left = None
		[string, index, symbol] = get_sym(string, index)
		#print(symbol)
		assert symbol == "~"
		[string, index, right] = parse(string, index)
		#print(right)
	if left == None and symbol == '~':
		p = negation(right)
	elif symbol == "/\\":
		p = conjunction(left, right)
	elif symbol == "\\/":
		p = disjunction(left, right)
	elif symbol == "->":
		p = implies (left, right)
	#else:
		#p = variable(symbol)
	
	while (string[index] == ' '):
		index += 1
	if string[index] == ')':
		index += 1
	else:
		print("error 765")
		sys.exit()
	return [string, index, p]

def print_tree(tree):
	if isinstance(tree, variable):
		return str(tree.name)
	if isinstance(tree, negation):
		return "(~"+print_tree(tree.left)+")"
	if isinstance(tree, conjunction):
		return "("+print_tree(tree.left)+" /\ "+print_tree(tree.right)+")"
	if isinstance(tree, disjunction):
		return "("+print_tree(tree.left)+" \/ "+print_tree(tree.right)+")"
	if isinstance(tree, implies):
		return "("+print_tree(tree.left)+" -> "+print_tree(tree.right)+")"

def to_parse(formula):
	[string, index, p] = parse(formula, 0)
	return p

def fire():
	formula = str(input("give the fucking formula : "))
	[string, index, p] = parse(formula, 0)
	print(print_tree(p))
	return 

if __name__ == '__main__':
	fire()
