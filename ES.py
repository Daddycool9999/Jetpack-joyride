from board import board1 
class ES:
	def __init__(self):
		for i in range(0,33):
			for j in range(0,1351):
				board1.mat[i][j]=' '

	def win(self):
		with open("b.txt") as fl_in:
			lnes=fl_in.readlines()
			for i in range(3,3+len(lnes)):
				for j in range(board1.itr,board1.itr+len(lnes[i-3])):
					if lnes[i-3][j-board1.itr]=='\t' or lnes[i-3][j-board1.itr]=='\n':
						board1.mat[i][j]=' '
					else:
						board1.mat[i][j]=lnes[i-3][j-board1.itr]

	def loss(self):
		with open("a.txt") as fl_in: 						

			lnes = fl_in.readlines()
			for i in range(3,3+len(lnes)):
				for j in range(board1.itr,board1.itr+len(lnes[i-3])):
					if lnes[i-3][j-board1.itr] == '\t' or lnes[i-3][j-board1.itr]=='\n':
						board1.mat[i][j]=' '
					else :
						board1.mat[i][j]=lnes[i-3][j-board1.itr]