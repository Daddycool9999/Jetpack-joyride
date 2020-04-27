from board import board1
from character import man,boss
lit=[]
lit1=[]
vit=[]
vit1=[]
fl=[]
fl1=[]
class bullet:
	def __init__(self):
		self.__x=man.xl+2
		self.__y=man.yl
		lit.append(self.__x)
		vit.append(self.__y)
		fl.append(0)
		board1.mat[man.yl][self.__x]='>'
	
class vilbullet:
	def __init__(self):
		self.__x=1337
		self.__y=boss.yl
		lit1.append(self.__x)
		vit1.append(self.__y)
		fl1.append(0)
		board1.mat[self.__y][self.__x]='<'
		board1.mat[self.__y+5][self.__x]='<'
