from CNF import convert_to_CNF
from parser import to_parse, variable, negation, conjunction, disjunction, implies

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

def add_in_set_clauses (i, set_clauses):
	if isinstance (i, variable):
		set_clauses = set_clauses.union(set(i.name))
	elif isinstance (i, negation):
		assert isinstance(i.left, variable)
		set_clauses = set_clauses.union({"~"+i.left.name})
	elif isinstance (i, conjunction):
		set_clauses = add_in_set_clauses(i.left, set_clauses)
		set_clauses = add_in_set_clauses(i.right, set_clauses)
	elif isinstance (i, disjunction):
		assert isinstance(i.left, conjunction) == False
		assert isinstance (i.right, conjunction) == False
		temp = set()
		temp = add_in_set_clauses (i.left, temp)
		temp = add_in_set_clauses (i.right, temp)
		assert isinstance(temp, set) == True
		set_clauses = set_clauses.union(temp)
	elif isinstance(i, implies):
		print("fuck its implies")
		return
	else:
		print("fuck")
		return
	return set_clauses


def get_clauses():
	string = str(input("give formula : "))
	formulas = string.split(',')
	conclusion = formulas[-1].split('|-')[-1]
	formulas[-1] = formulas[-1].split('|-')[0]
	if conclusion.alnum():#conc is a variable
		formulas.appen('(~ ' + conclusion + ')') #the space after '~' is very imp
	else:
		formulas.append('(~(' + conclusion + '))')
	print(formulas)
	clauses = []
	for i in formulas:
		print("i is :", i)
		#print('*'*10)
		print(print_tree(to_parse(i)))
		#print('*'*10)
		print("CNF is :", print_tree(convert_to_CNF(to_parse(i))))
		clauses.append(convert_to_CNF(to_parse(i)))
	print(clauses)
	print("print_tree ing members of clauses")
	for i in clauses:
		print(print_tree(i))
	set_clauses = []
	for i in clauses:
		print(add_in_set_clauses(i, set()))
		set_clauses.append(add_in_set_clauses(i, set()))
	print(set_clauses)
	

if __name__ == '__main__':
	get_clauses()
	print(add_in_set_clauses(variable("p"), {1,2}))
