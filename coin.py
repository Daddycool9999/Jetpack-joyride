from board import board1
import random

class coin:
	def __init__(self):
		self.__x=random.randint(0,1211)
		self.__xx=self.__x+3
		self.__y=random.randint(3,27)
		self.__yy=self.__y+2
	def conprin(self):
		for i in range(self.__x,self.__xx+1):
			for j in range(self.__y,self.__yy+1):
				board1.mat[j][i]='c'




