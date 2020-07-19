import sys
#class AST:
#    def __init__(self, LAST, RAST, symbol):
#        self.LAST = LAST
#        self.RAST = RAST
#        self.symbol = symbol
#ATOMS = set()

class variable:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.id = "variable"

class negation:
    def __init__(self, left):
        self.left = left
        self.right = None
        self.id = "negation"

class conjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.id = "conjunction"

class disjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.id = "disjunction"

class implies:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.id = "implies"

def get_var(string, index):
    #global ATOMS
    while (string[index] == ' '):
        index += 1
    var = ""
    while ((index < len(string)) and string[index].isalnum()):
        var += string[index]
        index += 1
    #ATOMS.add(var)
    return [string, index, var]



def get_sym(string, index):
    while (string[index] == ' '):
        index += 1
    symbol = ""
    while (string[index] != ' ' and string[index] != ')'): #take care about /\\ /\ ..
        symbol += string[index]
        index += 1
    return [string, index, symbol]

def check_not (string, index):
    symbol = ""
    [string, index, symbol] = get_sym (string, index);
    if symbol == "~":
        return 1
    else:
        return 0

def check_and (string, index):
    symbol = ""
    [string, index, symbol] = get_sym (string, index)
    if symbol == "/\\":
        return 1
    else:
        return 0

def check_or (string, index):
    symbol = ""
    [string, index, symbol] = get_sym (string, index)
    if symbol == "\\/":
        return 1
    else:
        return 0

def check_implies (string, index):
    symbol = ""
    [string, index, symbol] = get_sym(string, index)
    if symbol == "->":
        return 1
    else:
        return 0



def parse(string, index): 
    while (string[index] == ' '):
        index += 1
    if string[index] == ')':
        print("error in string[index] in parse")
        sys.exit()
    if string[index] != '(':
        var = ""
        [string, index, var] = get_var (string , index)
        #p = AST(None, None, atom)
        p = variable(var)
        return [string, index, p]
    if string[index] == '(':
        index += 1
    if check_not (string , index) == 0:
        #[string, index, LAST] = parse (string, index)
        [string, index, left] = parse (string, index)
    else:
        #LAST = None
        left = None
    [string, index, symbol] = get_sym(string, index)
    #[string, index, RAST] = parse (string, index)
    [string, index, right] = parse (string, index)
    if left == None:
        p = negation(right)
    elif symbol == "/\\":
        p = conjunction(left, right)
    elif symbol == "\\/":
        p = disjunction(left, right)
    elif symbol == "->":
        p = implies (left, right)
    #elif symbol == "~":
    #    p = negation(right)
    #p = AST (LAST, RAST, symbol)
    
    while (string[index] == ' '):
        index += 1
    if string[index] == ')':
        index += 1
    else:
        print("error 765")
        sys.exit()
    return [string, index, p]
'''
def print_AST(p):
    if p is None:
        print(p)
        return
    print(p.symbol)
    print_AST (p.LAST)
    print_AST (p.RAST)
'''
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


def fire(string):
    #string = str(input("give formula : "))
    index = 0
    [string, index, p] = parse (string, index)
    #print_AST(p)
    print('*'*20)
    print(print_tree(p))
    print('*'*20)
    #return [p, ATOMS]
    return p

def to_parse(formula):
    [string, index, p] = parse(formula, 0)
    return p

#print_tree(to_parse("(p -> q)"))
#print_tree(fire("(p -> q)"))
