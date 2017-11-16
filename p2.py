import p1

ROW=6
COL=7

def evaluate_state(state):
	global ROW,COL
	O = 0
	X = 0
	full = 1
	name, player_to_move, board = state
	
	for j in range(ROW):
		for i in range(4): #check for horitzontal 4s
			if board[j][i]=='O' and board[j][i+1]=='O' and board[j][i+2]=='O' and board[j][i+3]=='O':
				O = 1
			if board[j][i]=='X' and board[j][i+1]=='X' and board[j][i+2]=='X' and board[j][i+3]=='X':
				X = 1


			if j <3:#checking diagonals
				if board[j][i]=='O' and board[j+1][i+1]=='O' and board[j+2][i+2]=='O' and board[j+3][i+3]=='O':
					O = 1
				if board[j][i]=='X' and board[j+1][i+1]=='X' and board[j+2][i+2]=='X' and board[j+3][i+3]=='X':
					X = 1

				#checking diagonals
				if board[j+3][i]=='O' and board[j+2][i+1]=='O' and board[j+1][i+2]=='O' and board[j][i+3]=='O':
					O = 1
				if board[j+3][i]=='X' and board[j+2][i+1]=='X' and board[j+1][i+2]=='X' and board[j][i+3]=='X':
					X = 1


		if j < 3: #checking verticals
			for q in range(COL):
				if board[j][q]=='O' and board[j+1][q]=='O' and board[j+2][q]=='O' and board[j+3][q]=='O':
					O = 1
				if board[j][q]=='X' and board[j+1][q]=='X' and board[j+2][q]=='X' and board[j+3][q]=='X':
					X = 1


		for k in board[j]: # check if boardis full
			if k=='-':
				full = 0

	
	return (O,X,full)



if __name__ == '__main__':
	state = p1.read()
	O,X,full = evaluate_state(state)
	print('has 4 O : '+str(O))
	print('has 4 X : '+str(X))
	print('full : '+str(full))
