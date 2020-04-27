import time
from colorama import *
#from character import man
class board:
	def __init__(self):
		self.__mat = [[] for y in range(33)] 
		for i in range(0,33):
			for j in range(0,1351):
				self.mat[i].append(' ')

		for i in range(1,2):
			for j in range(0,1351):
				self.mat[i][j]="*"
		for i in range(31,33):
			for j in range(0,1351):
				self.mat[i][j]="*"
		self.__itr=0
	def printt(self,man):
		print("\033[0;0H")
		for i in range(0,33):
			for j in range(0+self.itr,136+self.itr):
				if board1.mat[i][j]=='M':
					if man.shield==1:
						print(Fore.WHITE + board1.mat[i][j] + '\x1b[0m',end='')
					else:
						print(Fore.BLUE + board1.mat[i][j] + '\x1b[0m',end='')

				elif board1.mat[i][j]=='o':
					print(Fore.RED + board1.mat[i][j] + '\x1b[0m',end='')

				elif board1.mat[i][j]=='c':
					print(Fore.YELLOW + board1.mat[i][j] + '\x1b[0m',end='')

				elif board1.mat[i][j]=='n':
					print(Fore.GREEN + board1.mat[i][j] + '\x1b[0m',end='')

				elif board1.mat[i][j]=='B':
					print(Fore.RED + board1.mat[i][j] + '\x1b[0m',end='')
				elif board1.mat[i][j]=='>':
					print(Fore.BLUE + board1.mat[i][j] + '\x1b[0m',end='')
				elif board1.mat[i][j]=='<':
					print(Fore.RED + board1.mat[i][j] + '\x1b[0m',end='')
				elif board1.mat[i][j]=='*':
					print(Fore.GREEN + board1.mat[i][j] + '\x1b[0m',end='')

				else:
					print(board1.mat[i][j],end='')




			print()
		if self.itr+136<1351:
			if man.boost:
				self.itr+=2
			else:
				self.itr+=1		
	@property
	def mat(self):
		return self.__mat
	@mat.setter
	def mat(self,x):
		self.__mat=x
	@property
	def itr(self):
		return self.__itr
	@itr.setter
	def itr(self,x):
		self.__itr=x
	
	
	

	

board1=board()