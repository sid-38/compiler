def grammar_checker(rules,start_symbol):
	if start_symbol not in rules:
		print("Start symbol is not present in the production rules")
		exit()

	for x in rules.values():
		for y in x:
			if y.isupper():
				if y not in rules:
					print("Rule for the terminal symbol",y,"was not found.")
					exit()



start_symbol = input("Start Symbol:")
production_no = int(input("Number of production rules:"))

production_rules = {}

#Asking for the grammar
for x in range(production_no):
	lhs = input("LHS:")
	rhs = input("RHS:")
	production_rules[lhs] = rhs

#Checking the format of the grammar
grammar_checker(production_rules,start_symbol)

#Confirming the grammar
print("Is this the grammar?")

for x in production_rules:
	print(x,'->',production_rules[x])

while True:
	
	confirm = input("Type yes/no: ")

	if confirm == "no":
		exit()
	elif confirm == "yes":
		break

#Asking for the input sequence of tokens
input_seq = input("Enter the input sequence: ")

derivation = start_symbol
derivation_tree = ''
ptr1 = ptr2 = 0

while ptr2<len(input_seq):

	if derivation[ptr1].islower():
		if derivation[ptr1] != input_seq[ptr2]:
			print("Syntax error")
			exit()
		else:
			ptr1 += 1
			ptr2 += 1
	else:
		if derivation[ptr1] not in production_rules:
			print("Syntax error")
			exit()

		derivation_tree += derivation
		derivation_tree += ' => '
		derivation = derivation[0:ptr1] + production_rules[derivation[ptr1]] + derivation[ptr1+1:]
		derivation_tree += derivation
		derivation_tree += '\n'
print(derivation_tree)
