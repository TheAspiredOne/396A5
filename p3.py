import p1
import p2

ROW = 6
COL = 7

def calculate_heuristics(state):
	global ROW, COL
	ext4_1_O = 0
	ext4_1_X = 0
	ext4_2_O = 0
	ext4_2_X = 0
	ext4_3_O = 0
	ext4_3_X = 0
	eval_O = 0
	name, player_to_move, board = state
	X=list()
	O=list()

	
	for j in range(ROW):
		for i in range(4): #check for horitzontal 4s
			if (board[j][i]=='O' or board[j][i]=='-') and (board[j][i+1]=='O' or board[j][i+1]=='-') and (board[j][i+2]=='O' or board[j][i+2]=='-') and (board[j][i+3]=='O' or board[j][i+3]=='-'):
				O.append([board[j][i], board[j][i+1], board[j][i+2],board[j][i+3]])

			if (board[j][i]=='X' or board[j][i]=='-') and (board[j][i+1]=='X' or board[j][i+1]=='-') and (board[j][i+2]=='X' or board[j][i+2]=='-') and (board[j][i+3]=='X' or board[j][i+3]=='-'):
				X.append([board[j][i], board[j][i+1], board[j][i+2],board[j][i+3]])
				# print('1',j,i,board[j][i], board[j][i+1], board[j][i+2],board[j][i+3])


			if j <3:			
				if (board[j][i]=='O' or board[j][i]=='-') and (board[j+1][i+1]=='O' or board[j+1][i+1]=='-') and (board[j+2][i+2]=='O' or board[j+2][i+2]=='-') and (board[j+3][i+3]=='O' or board[j+3][i+3]=='-'):
					O.append([board[j][i],board[j+1][i+1],board[j+2][i+2],board[j+3][i+3]])
				if (board[j][i]=='X' or board[j][i]=='-') and (board[j+1][i+1]=='X' or board[j+1][i+1]=='-') and (board[j+2][i+2]=='X' or board[j+2][i+2]=='-') and (board[j+3][i+3]=='X' or board[j+3][i+3]=='-'):
					X.append([board[j][i],board[j+1][i+1],board[j+2][i+2],board[j+3][i+3]])
					# print('2',j,i,board[j][i],board[j+1][i+1],board[j+2][i+2],board[j+3][i+3])


				if (board[j+3][i]=='O' or board[j+3][i]=='-') and (board[j+2][i+1]=='O' or board[j+2][i+1]=='-') and (board[j+1][i+2]=='O' or board[j+1][i+2]=='-') and (board[j][i+3]=='O' or board[j][i+3]=='-'):
					O.append([board[j+3][i],board[j+2][i+1],board[j+1][i+2],board[j][i+3]])
				if (board[j+3][i]=='X' or board[j+3][i]=='-') and (board[j+2][i+1]=='X' or board[j+2][i+1]=='-') and (board[j+1][i+2]=='X' or board[j+1][i+2]=='-') and (board[j][i+3]=='X' or board[j][i+3]=='-'):
					X.append([board[j+3][i],board[j+2][i+1],board[j+1][i+2],board[j][i+3]])
					# print('here',j+3,i,board[j+3][i],board[j+2][i+1],board[j+1][i+2],board[j][i+3])


		if j < 3:
			for q in range(COL):
				# print(j,q,ROW)
				if (board[j][q]=='O' or board[j][q]=='-') and (board[j+1][q]=='O' or board[j+1][q]=='-') and (board[j+2][q]=='O' or board[j+2][q]=='-') and (board[j+3][q]=='O' or board[j+3][q]=='-'):
					O.append([board[j][q],board[j+1][q],board[j+2][q],board[j+3][q]])
				if (board[j][q]=='X' or board[j][q]=='-') and (board[j+1][q]=='X' or board[j+1][q]=='-') and (board[j+2][q]=='X' or board[j+2][q]=='-') and (board[j+3][q]=='X' or board[j+3][q]=='-'):
					X.append([board[j][q],board[j+1][q],board[j+2][q],board[j+3][q]])
					# print('4',j,q,board[j][q],board[j+1][q],board[j+2][q],board[j+3][q])


	for i in X:
		count = i.count('X')
		if count == 1:
			ext4_1_X+=1
		elif count ==2:
			ext4_2_X+=1
		elif count==3:
			ext4_3_X+=1
	for i in O:
		count = i.count('O')
		if count ==1:
			ext4_1_O+=1
		elif count ==2:
			ext4_2_O+=1
		elif count==3:
			ext4_3_O+=1

	eval_O = 1*(ext4_1_O - ext4_1_X)+ 10*(ext4_2_O- ext4_2_X)+ 40*(ext4_3_O-ext4_3_X)
	eval_X = 1*(ext4_1_X - ext4_1_O)+ 10*(ext4_2_X- ext4_2_O)+ 40*(ext4_3_X-ext4_3_O)

	return (ext4_1_X,ext4_1_O,ext4_2_X,ext4_2_O,ext4_3_X,ext4_3_O,eval_O, eval_X)


if __name__ == '__main__':
	state = p1.read()
	ext4_1_X,ext4_1_O,ext4_2_X,ext4_2_O,ext4_3_X,ext4_3_O,eval_O,eval_X = calculate_heuristics(state)
	print('ext4_1_O : '+str(ext4_1_O))
	print('ext4_1_X : '+str(ext4_1_X))
	print('ext4_2_O : '+str(ext4_2_O)) 
	print('ext4_2_X : '+str(ext4_2_X))
	print('ext4_3_O : '+str(ext4_3_O)) 
	print('ext4_3_X : '+str(ext4_3_X)) 
	print('eval_O : '+str(eval_O))