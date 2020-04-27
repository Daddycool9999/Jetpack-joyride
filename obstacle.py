from board import board1
import random

class obstacle:
	def __init__(self):
		self.__type=random.randint(0,3)
		self.__type1=random.randint(0,2)
		if self.__type==0:
			self.__x1=random.randint(0,1209)
			self.__y1=random.randint(3,30)
		if self.__type==1:
			self.__x1=random.randint(0,1215)
			self.__y1=random.randint(4,24)
		if self.__type==2:
			self.__x1=random.randint(6,1209)
			self.__y1=random.randint(6,24)
	def obsprin(self):
		
		if self.__type==0:
			for i in range(self.__x1,self.__x1+6):
				board1.mat[self.__y1][i]='o'
		if self.__type==1:
			for i in range(self.__y1,self.__y1+6):
				board1.mat[i][self.__x1]='o'
		if self.__type==2:
			#l=random.randint(0,2)
			if self.__type1==0:
				for i in range(self.__x1,self.__x1+6):
					board1.mat[self.__y1+i-self.__x1][i]='o'
			else:
				for i in range(self.__x1-6,self.__x1):
					board1.mat[self.__y1+i-self.__x1][i]='o'

