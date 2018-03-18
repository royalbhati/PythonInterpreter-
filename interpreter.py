class Token:

	def __init__(self,type,value):
		self.type=type
		self.value=value


	def __str__(self):
		return 'Token {} {} '.format(self.type,self.value)



class Interpreter:
	
	def __init__(self,text):
		self.text=text
		self.pos=0
		self.curr_token=None
		self.curr_char=self.text[self.pos]


	def get_next_token(self):
		text=self.text
		if self.pos>len(text)-1:
			return Token('end',None)
		curr_char=self.text[self.pos]	
		if curr_char.isdigit():
			token=Token('int',int(curr_char))
			self.pos+=1

			return token

		elif curr_char =='+':
			token=Token('op',curr_char)
			self.pos+=1
			return token
		elif curr_char =='-':
			token=Token('op',curr_char)
			self.pos+=1
			return token	
		elif curr_char.isspace():
			token=Token('whitespace',curr_char)
			self.pos+=1
			return token


	def match(self,token_type):
		if self.curr_token.type==token_type:
		
			self.curr_token=self.get_next_token()

		else:
			return('error')

	def expr(self):
		left=''
		right=''
		self.curr_token=self.get_next_token()
		while self.curr_token.type=='whitespace':
			self.match('whitespace')
		while self.curr_token.type=='int':

			left=left+str(self.curr_token.value)
			self.match('int')
			lv=int(left)
		while self.curr_token.type=='whitespace':
			self.match('whitespace')
		op=self.curr_token.value
		self.match('op')

		while self.curr_token.type=='whitespace':
			self.match('whitespace')
		while self.curr_token.type=='int':

			right=right+str(self.curr_token.value)
			self.match('int')
			rv=int(right)
		while self.curr_token.type=='whitespace':
			self.match('whitespace')
		if op=='+':	
			return lv+rv
		else:
			return lv-rv	

if __name__=='__main__':
  a=Interpreter(' 55    -20')
  # print(a.get_next_token())
  # print(a.get_next_token())
  # print(a.get_next_token())

  print(a.expr())
