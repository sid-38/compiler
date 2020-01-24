strtpointer = 0
movpointer = 0
state = 0

def fail():
	global state
	if state == 0:
		print("lexical error")
		state = 1
	movpointer = strtpointer
	return
	

def id_lex(inpstring):
	
	global strtpointer
	global movpointer
	outstring = ""
	while inpstring[movpointer] == ' ':
		movpointer += 1
	if inpstring[movpointer].isalpha():
		outstring += inpstring[movpointer]
		movpointer += 1
			
		while inpstring[movpointer].isalpha() or inpstring[movpointer].isdigit():
			outstring += inpstring[movpointer]
			movpointer += 1
		strtpointer = movpointer
		return outstring
	else:
		outstring = ''
		fail()
		return "end"
		
def lex(inpstring):
	token_string = ''
	while token_string != 'end':
		token_string = id_lex(inpstring)
		print(token_string)

strtpointer = 0
movpointer = 0
state = 0
lex("hello people")


