from board import board1
import random
class nitro:
	def __init__(self):
		self.__x=random.randint(0,1150)
		self.__y=random.randint(3,30)
	def nitprin(self):
		board1.mat[self.__y][self.__x]='n'

			