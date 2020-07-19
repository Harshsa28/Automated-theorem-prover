def dpp(S):
	while S != [set()] and S != []:
		#pick a variable
		for i in S:
			for var in i:
				break
		if '~' in var:
			var = var[1:]
		#remove all elements with p and ~p
		for i in S:
			if var in i and '~'+var in i:
				S.remove(i)
		T = [x for x in S if var in x or '~'+var in x]
		U = []
		for i in T:
			for j in T:
				if (var in i and '~'+var in j) or ('~'+var in i and var in j):
					U.append((i.union(j))-{var, '~'+var})
		S = [x for x in S if x not in T]
		S.extend(U)
		S = list(set(map(frozenset, S)))
		S = [set(i) for i in S]
		print(S)
	if S == [set()]:
		print("Not Satisfiable which is Valid!")
	elif S == []:
		print("Satisfiable which is Invalid!")

def solve():
	formulas = [{'p','q'},{'p','r'},{'~p'},{'~q','~r'}]
	formulas = [{'p','q'},{'p','r'},{'~p','~q'},{'~p','~r'}]
	print(formulas)
	dpp(formulas)

solve()

