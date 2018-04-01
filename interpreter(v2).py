INT,PLUS,MINUS,MULT,DIV,EOF,WHITE='INT','PLUS','MINUS','MULT','DIV','EOF','WHITE'

class Token:
	'''Token Class to generate tokens'''
	def __init__(self,type,value):
		'''Token will have a type and a value'''
		self.type=type
		self.value=value

	def __str__(self):
		return 'Token {} {}'.format(self.type,self.value)

class Interpreter:
	'''Interpreter class which contains lexer and parser'''

	def __init__(self,text):
		self.text=text #input expression to be evaluated
		self.pos=0#pointer to point to xharacters
		self.curr_token=None
		self.curr_char=self.text[self.pos]


	def advance(self):
		'''increments pointer value'''
		self.pos+=1
		if self.pos>len(self.text)-1:
			self.curr_char=None

		else:
			curr_char=self.text[self.pos]

	def error(self):
		raise Exception('wrong')		
	def ignore_white(self):
		'''Ignore white spaces'''
		while self.curr_char.isspace() and self.curr_char is not None:
			self.advance()			
	def integer(self):
		result=''
		while self.curr_char.isdigit() and self.curr_char is not None:
			result=result+self.curr_char
			self.advance()	
		return int(result)			
	def get_next_token(self):
		while self.curr_char is not None:
			if self.curr_char.isspace():
				self.ignore_white()
				continue

			if self.curr_char.isdigit():
				return Token(INT,self.integer())		

			if self.curr_char=='+':
				self.advance()
				return Token(PLUS,'+')
				

			if self.curr_char=='-':
				self.advance()
				return Token(MINUS,'-')
			self.error()	
				
		return Token(EOF,None)

	def match(self,token_type):
		if self.curr_token.type==token_type:
			self.curr_token=get_next_token()
		else:
			print('syntax error')		
		
	def term(self):
		token=self.curr_token
		self.match(INT)
		return token.value

	def expr(self):
		self.curr_token=get_next_token()

		result=self.term()
		while self.curr_token.type in (PLUS,MINUS):
			token=self.curr_token
			if token.type==PLUS:
				result=result+self.term()					
			elif token.type==MINUS:
				result=result-self.term()
		return result
					



			
if __name__ == '__main__':
  a=Interpreter(' 55-2+1')
  for x in range(6):

      print(a.get_next_token())
  

  # print(a.expr())				
					
