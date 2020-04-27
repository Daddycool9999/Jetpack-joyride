from board import board1
import random
from character import man

class magnet:
	def __init__(self):
		self.__x=1230
		self.__y=random.randint(3,30)
		board1.mat[self.__y][self.__x]='G'
	def attract(self):
		if self.x>=man.xl:
			for i in range(man.yl,man.yl+3):
				if board1.mat[i][man.xl+3]=='c':
					man.score+=1	
				if board1.mat[i][man.xl+4]=='c':
					man.score+=1
				if board1.mat[i][man.xl+3]=='o':
					man.life-=1
					for k in range(i-5,i+6):
						for l in range(man.xl-2,man.xl+9):
							if k>=3 and k<=30 and l>=0 and l<=1350:
								if board1.mat[k][l]=='o':
									board1.mat[k][l]=' '
				if board1.mat[i][man.xl+4]=='o':
					man.life-=1
					for k in range(i-5,i+6):
						for l in range(man.xl-1,man.xl+10):
							if k>=3 and k<=30 and l>=0 and l<=1350:
								if board1.mat[k][l]=='o':
									board1.mat[k][l]=' '
				if board1.mat[i][man.xl+3]=='n':
					man.boost=1	
				if board1.mat[i][man.xl+4]=='n':
					man.boost=1
				if board1.mat[i][man.xl+3]=='s':
					man.shield=1	
				if board1.mat[i][man.xl+4]=='s':
					man.shield=1
			if man.xl<board1.itr+134:
				man.xl+=2
				for j in range(man.yl,man.yl+3):
					board1.mat[j][man.xl-2]=' '
				for j in range(man.yl,man.yl+3):
					board1.mat[j][man.xl-1]=' '
		else:
			for i in range(man.yl,man.yl+3):
				if board1.mat[i][man.xl-1]=='c':
					man.score+=1	
				if board1.mat[i][man.xl-1]=='o':
					man.life-=1
					for k in range(i-5,i+6):
						for l in range(man.xl-6,man.xl+5):
							if k>=3 and k<=30 and l>=0 and l<=1350:
								if board1.mat[k][l]=='o':
									board1.mat[k][l]=' '
				if board1.mat[i][man.xl-1]=='n':
					man.boost=1
				if board1.mat[i][man.xl-1]=='s':
					man.shield=1

			if man.xl>board1.itr:
				man.xl-=1
				for j in range(man.yl,man.yl+3):
					board1.mat[j][man.xl+2]=' '
	@property
	def x(self):
		return self.__x
	@x.setter
	def x(self,y):
		self.__x=y
	@property
	def y(self):
		return self.__y
	
	@y.setter
	def y(self,x):
		self.__y=x
	
	


mag=magnet()