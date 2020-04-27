from board import board1
class person:
	#__blo=1
	def __init__(self,x,y):
		self._xl=x
		self._yl=y
	#	self.__life=life
	def gravity(self):
		pass
	def scoreprint(self):
		pass
	
	
class hero(person):
	def __init__(self,x,y,life):
		super().__init__(x,y)
		self.__score=0
		self.__boost=0
		self.__shield=0
		self.__rech=1
		self.__life=life
	def herprint(self):
		if self.yl<=28 and self.yl>=3:
			if self.xl>board1.itr:
				for i in range((self.yl),self.yl+3):
					for j in range(self.xl,(self.xl)+2):
						board1.mat[i][j]= 'M' 
			else:
				self.xl=board1.itr
				for i in range(self.yl,self.yl+3):
					for j in range(board1.itr,board1.itr+2):
						board1.mat[i][j]='M'
		elif self.yl>28:
			
			if self.xl>board1.itr:
				for i in range(28,31):
					for j in range(self.xl,(self.xl)+2):
						board1.mat[i][j]='M'
			else:
				self.xl=board1.itr

				for i in range(28,31):
					for j in range(board1.itr,board1.itr+2):
						board1.mat[i][j]='M'
		else:
			
			if self.xl>board1.itr:
				for i in range(3,6):
					for j in range(self.xl,(self.xl)+2):
						board1.mat[i][j]='M'
			else:
				self.xl=board1.itr

				for i in range(3,6):
					for j in range(board1.itr,board1.itr+2):
						board1.mat[i][j]='M'	
	def scoreprint(self):
		board1.mat[0][board1.itr]='S'
		board1.mat[0][board1.itr+1]='c'
		board1.mat[0][board1.itr+2]='o'
		board1.mat[0][board1.itr+3]='r'
		board1.mat[0][board1.itr+4]='e'
		board1.mat[0][board1.itr+5]='='
		board1.mat[0][board1.itr+6]=self.score

	def lifeprint(self):
		board1.mat[0][board1.itr+7]=' '
		board1.mat[0][board1.itr+8]='L'
		board1.mat[0][board1.itr+9]='i'
		board1.mat[0][board1.itr+10]='f'
		board1.mat[0][board1.itr+11]='e'
		board1.mat[0][board1.itr+12]='='
		board1.mat[0][board1.itr+13]=self.life

	def boostprint(self):
		board1.mat[0][board1.itr+14]=' '

		board1.mat[0][board1.itr+15]='N'
		board1.mat[0][board1.itr+16]='i'
		board1.mat[0][board1.itr+17]='t'
		board1.mat[0][board1.itr+18]='r'
		board1.mat[0][board1.itr+19]='o'
		board1.mat[0][board1.itr+20]='='
		if self.boost:
			board1.mat[0][board1.itr+21]='o'
			board1.mat[0][board1.itr+22]='n'
			board1.mat[0][board1.itr+23]=' '
		else:
			board1.mat[0][board1.itr+21]='o'
			board1.mat[0][board1.itr+22]='f'
			board1.mat[0][board1.itr+23]='f'
	def shieldprint(self):
		board1.mat[0][board1.itr+24]=' '

		board1.mat[0][board1.itr+25]='S'
		board1.mat[0][board1.itr+26]='h'
		board1.mat[0][board1.itr+27]='i'
		board1.mat[0][board1.itr+28]='e'
		board1.mat[0][board1.itr+29]='l'
		board1.mat[0][board1.itr+30]='d'
		board1.mat[0][board1.itr+31]='='
		if self.shield:
			board1.mat[0][board1.itr+32]='o'
			board1.mat[0][board1.itr+33]='n'
			board1.mat[0][board1.itr+34]=' '

		else:
			board1.mat[0][board1.itr+32]='o'
			board1.mat[0][board1.itr+33]='f'
			board1.mat[0][board1.itr+34]='f'




	def gravity(self,godo):
		
		for i in range(self.xl,self.xl+2):
			if self.yl+godo<=28:
				for j in range(self.yl+3,self.yl+godo+2):	
					if board1.mat[j][i]=='c':
						self._hero__score+=1
						board1.mat[j][i]=' '
					if board1.mat[j][i]=='o':
						if self._hero__shield==0:
							self._hero__life-=1
						for k in range(j-5,j+6):
							for l in range(i-5,i+6):
								if k>=3 and k<=30 and l>=0 and l<=1350:
									if board1.mat[k][l]=='o':
										board1.mat[k][l]=' '
				
					if board1.mat[j][i]=='n':
						self._hero__boost=1
						board1.mat[j][i]=' '
					
		if self.yl+godo<=28:
			for i in range(self.xl,self.xl+2):
				for j in range(self.yl,self.yl+godo):
					if board1.mat[j][i]=='M':
						board1.mat[j][i]=' '
			self.yl+=godo
				
		else:
			for i in range(self.xl,self.xl+2):
				for j in range(self.yl,30):
					if board1.mat[j][i]=='M':
						board1.mat[j][i]=' '
			self.yl=28
	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self,x):
		self.__score=x
	@property
	def boost(self):
		return self.__boost
	@boost.setter
	def boost(self,x):
		self.__boost=x

	@property
	def shield(self):
		return self.__shield
	@shield.setter
	def shield(self,x):
		self.__shield=x
	@property
	def rech(self):
		return self.__rech
	@rech.setter
	def rech(self,x):
		self.__rech=x
	@property
	def life(self):
		return self.__life

	@life.setter
	def life(self,x):
		self.__life=x

	@property
	def xl(self):
		return self._xl
	@xl.setter
	def xl(self,x):
		self._xl=x
	@property
	def yl(self):
		return self._yl
	@yl.setter
	def yl(self,x):
		self._yl=x
		
	
	
	
		
class boss(person):
	def __init__(self):
		self.__life=9
		super().__init__(1340,25)
	def vilprint(self):
		if self.yl<=25 and self.yl>=3:
			
			for i in range(self.yl,self.yl+6):
				for j in range(self.xl,(self.xl)+4):
					board1.mat[i][j]='B'
			board1.mat[self.yl][self.xl-1]='='
			board1.mat[self.yl][self.xl-2]='='

			board1.mat[self.yl+5][self.xl-1]='='
			board1.mat[self.yl+5][self.xl-2]='='

		elif self.yl>25:
			
			#if self.xl>board1.itr:
			for i in range(25,31):
				for j in range(self.xl,(self.xl)+4):
					board1.mat[i][j]='B'
			board1.mat[25][self.xl-1]='='
			board1.mat[25][self.xl-2]='='

			board1.mat[30][self.xl-1]='='
			board1.mat[30][self.xl-2]='='

			#else:
			#	self.xl=board1.itr

		else:
			
			#if self.xl>board1.itr:
			for i in range(3,9):
				for j in range(self.xl,(self.xl)+4):
					board1.mat[i][j]='B'
			board1.mat[3][self.xl-1]='='
			board1.mat[3][self.xl-2]='='

			board1.mat[8][self.xl-1]='='
			board1.mat[8][self.xl-2]='='

			#else:
			#	self.xl=board1.itr
	def lifeprint(self):
		board1.mat[0][1342]=' '
		board1.mat[0][1343]='L'
		board1.mat[0][1344]='i'
		board1.mat[0][1345]='f'
		board1.mat[0][1346]='e'
		board1.mat[0][1347]='='
		board1.mat[0][1348]=self.__life
	@property
	def life(self):
		return self.__life
	@life.setter
	def life(self,x):
		self.__life=x
	@property
	def xl(self):
		return self._xl
	@xl.setter
	def xl(self,x):
		self._xl=x
	@property
	def yl(self):
		return self._yl
	@yl.setter
	def yl(self,x):
		self._yl=x
	

        
man=hero(10,28,4)
boss=boss()