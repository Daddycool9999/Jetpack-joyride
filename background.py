from board import board1
from character import *
from alarmexception import *
from magnet import *
from obstacle import *
from ES import *
from coin import * 
from nitro import *
from bullet import *
from getch import _getChUnix as getChar
import signal
import os
import time
for i in range(25):
	cc=coin()
	cc.conprin()
for i in range(35):
	oo=obstacle()
	oo.obsprin()
for i in range(15):
	nit=nitro()
	nit.nitprin()
while True:
	board1.printt(man)	
	#print(board1.itr)
	def alarmhandler(signum,frame):
		raise AlarmException
	def user_input(timeout=0.5):
		signal.signal(signal.SIGALRM,alarmhandler)
		signal.setitimer(signal.ITIMER_REAL,timeout)
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''

	char = user_input()
	if man.boost:
		if time.time()-boostime>=10:
			man.boost=0
	if man.shield:
		if time.time()-shieldtime>=10:
			man.shield=0
			man.rech=0
			rechtime=time.time()
	if man.rech==0:
		if time.time()-rechtime>=60:
			man.rech=1
	if boss.life<=-1:
		end=ES()
#		os.system('clear')

		end.win()
		board1.printt(man)
		time.sleep(1)
		quit()
	if man.life<=-1:
		end=ES()
		#os.system('clear')
		end.loss()
		board1.printt(man)

		time.sleep(1)
		quit()
	if mag.x>=board1.itr and mag.x<=board1.itr+135:
		mag.attract()
	if man.yl==28:
		godo=0
	if char=='b':
		bb=bullet()
	if board1.itr<1215:
		for i in range(len(lit)):
			if lit[i]<=board1.itr+135 and fl[i]==0:
				if lit[i]<=1350:
					if board1.mat[vit[i]][lit[i]+1]=='o' or board1.mat[vit[i]][lit[i]+2]=='o' or board1.mat[vit[i]][lit[i]+3]=='o' or board1.mat[vit[i]][lit[i]+4]=='o':
						for j in range(vit[i]-5,vit[i]+6):
							for l in range(lit[i]-5,lit[i]+9):
								if l>=0 and l<=1350:
									if j>=3 and j<=30:
										if board1.mat[j][l]=='o':
											board1.mat[j][l]=' '
						board1.mat[vit[i]][lit[i]]=' '
						fl[i]=1
						
					else:
						board1.mat[vit[i]][lit[i]]=' '
						
						lit[i]+=4
						board1.mat[vit[i]][lit[i]]='>'

			elif lit[i]>board1.itr+135 and lit[i]<=1350:
				fl[i]=1
				board1.mat[vit[i]][lit[i]]=' '
	else:
		for i in range(len(lit)):
			if lit[i]<=board1.itr+135 and fl[i]==0:
				if lit[i]<=1348:
					if board1.mat[vit[i]][lit[i]+1]=='B' or board1.mat[vit[i]][lit[i]+2]=='B':
						boss.life-=1
						fl[i]=1
					else:
						lit[i]+=2
						board1.mat[vit[i]][lit[i]]='>'
					board1.mat[vit[i]][lit[i]-2]=' '
				else:
					fl[i]=0
					board1.mat[vit[i]][lit[i]]=' '
			elif lit[i]>board1.itr+135 and lit[i]<=1350:
				fl[i]=1
				board1.mat[vit[i]][lit[i]]=' '

	bb2=vilbullet()
	for i in range(len(lit1)):
		if lit1[i]<=board1.itr+135 and fl1[i]==0 and lit1[i]>=board1.itr:
			if board1.mat[vit1[i]][lit1[i]-1]=='M' or board1.mat[vit1[i]][lit1[i]-2]=='M':
				man.life-=1
				fl1[i]=1
			else:
				lit1[i]-=2
				board1.mat[vit1[i]][lit1[i]]='<'
				board1.mat[vit1[i]+5][lit1[i]]='<'
			board1.mat[vit1[i]][lit1[i]+2]=' '
			board1.mat[vit1[i]+5][lit1[i]+2]=' '

		elif lit1[i]<board1.itr:
			fl1[i]=1
			board1.mat[vit1[i]][lit1[i]]=' '
			board1.mat[vit1[i]+5][lit1[i]]=' '
			
		

	if char:
		if char=='w':
			if man.yl>3:
				for i in range(man.xl,man.xl+2):
					for j in range(man.yl-1,man.yl):	
						if board1.mat[j][i]=='c':
							man.score+=1
							board1.mat[j][i]=' '
						if board1.mat[j][i]=='o':
							if man.shield==0:
								man.life-=1

							for k in range(j-5,j+6):
								for l in range(i-5,i+6):
									if k>=3 and k<=30 and l>=0 and l<=1350:
										if board1.mat[k][l]=='o':
											board1.mat[k][l]=' '
						
						if board1.mat[j][i]=='n':
							man.boost=1
							board1.mat[j][i]=' '
							boostime=time.time()
					
				for j in range(man.xl,man.xl+2):
					if board1.mat[man.yl+2][j]=='M':
						board1.mat[man.yl+2][j]=' '
				man.yl-=1
			if board1.itr>=1215:
				if boss.yl>3 and man.yl<=25:
					
					for i in range(boss.yl,boss.yl+6):
						for j in range(boss.xl-2,boss.xl+4):
							board1.mat[i][j]=' '
					boss.yl=man.yl
				elif man.yl>25:
					boss.yl=25
				else:
					boss.yl=man.yl
				
		if char=='s':
			if man.yl<28:
				for i in range(man.xl,man.xl+2):
					for j in range(man.yl+3,man.yl+4):	
						if board1.mat[j][i]=='c':
							man.score+=1
							board1.mat[j][i]=' '
						if board1.mat[j][i]=='o':
							if man.shield==0:

								man.life-=1
							for k in range(j-5,j+6):
								for l in range(i-5,i+6):
									if k>=3 and k<=30 and l>=0 and l<=1350:
										if board1.mat[k][l]=='o':
											board1.mat[k][l]=' '
						
						if board1.mat[j][i]=='n':
							man.boost=1
							board1.mat[j][i]=' '
							boostime=time.time()
					
				for j in range(man.xl,man.xl+2):
					if board1.mat[man.yl][j]=='M':
						board1.mat[man.yl][j]=' '
				man.yl+=1
				if board1.itr>=1215:
					if man.yl<=25:
						
						for i in range(boss.yl,boss.yl+6):
							for j in range(boss.xl-2,boss.xl+4):
								board1.mat[i][j]=' '
						boss.yl=man.yl
					else:
						boss.yl=25
				
		if char=='a':
			if man.xl>board1.itr:
				for i in range(man.xl-3,man.xl):
					for j in range(man.yl,man.yl+3):	
						if board1.mat[j][i]=='c':
							man.score+=1
							board1.mat[j][i]=' '
						if board1.mat[j][i]=='o':
							if man.shield==0:
							
								man.life-=1
							for k in range(j-5,j+6):
								for l in range(i-5,i+6):
									if k>=3 and k<=30 and l>=0 and l<=1350:
										if board1.mat[k][l]=='o':
											board1.mat[k][l]=' '
						
						if board1.mat[j][i]=='n':
							man.boost=1
							board1.mat[j][i]=' '
							boostime=time.time()
					
				for j in range(man.yl,man.yl+3):
					if board1.mat[j][man.xl+1]=='M':
						board1.mat[j][man.xl+1]=' '
					if board1.mat[j][man.xl]=='M':
						board1.mat[j][man.xl]=' '
					if board1.mat[j][man.xl-1]=='M':
					 	board1.mat[j][man.xl-1]==''
				if man.xl-3>=board1.itr:
					man.xl-=3
				else:
					man.xl=board1.itr
				
		if char=='d':
			if man.xl<board1.itr+136:
				for i in range(man.xl+2,man.xl+5):
					for j in range(man.yl,man.yl+3):	
						if board1.mat[j][i]=='c':
							man.score+=1
							board1.mat[j][i]=' '
						if board1.mat[j][i]=='o':
							if man.shield==0:

								man.life-=1
							for k in range(j-5,j+6):
								for l in range(i-5,i+6):
									if k>=3 and k<=30 and l>=0 and l<=1350:
										if board1.mat[k][l]=='o':
											board1.mat[k][l]=' '
						
						if board1.mat[j][i]=='n':
							man.boost=1
							board1.mat[j][i]=' '
							boostime=time.time()
					
				
				for j in range(man.yl,man.yl+3):
					for i in range(man.xl,man.xl+3):	
						if board1.mat[j][i]=='M':
							board1.mat[j][i]=' '
				if man.xl+3<=board1.itr+135:
					man.xl+=3
				else:
					man.xl=board1.itr+135
		if char==' ':
			if man.rech==1:
				man.shield=1
				shieldtime=time.time()

		godo=0
		if char=='q':
			break
	else:
		godo+=1
		man.gravity(godo)

			
	man.herprint()
	man.scoreprint()
	man.lifeprint()
	man.boostprint()
	man.shieldprint()
	boss.vilprint()
	boss.lifeprint()
	#board1.printt(man)


	
	
