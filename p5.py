import p1
import p2
import p3

COL = 7
ROW = 6
c = 1 # number of negamx calls
v = None #root value in view of player to move
best_move = None
t = 0# number of terminal nodes
nt = 0 # number of non terminal nodes



def AlphaBeta(state, height,alpha,beta):
	global COL, ROW, c, v, best_move, t, nt

	name, player_to_move, board = state #unpack the tuple
	move=None
	isTerminal = False #termination flag
	O,X,full = p2.evaluate_state(state) #these will tell us whether we are at terminal state
	
	if O ==1 or X ==1 or full == 1:
		isTerminal = True
	if height == 0  or isTerminal:
		value = 0
		if full == 1:
			t+=1
			value = 0
		elif O==1 or X==1:
			t+=1
			value = -10000
		elif height == 0: #at a non-terminating leaf. Calculate heuristic
			nt+=1
			ext4_1_X,ext4_1_O,ext4_2_X,ext4_2_O,ext4_3_X,ext4_3_O,eval_O,eval_X = p3.calculate_heuristics(state) #unpack the tuple
			if player_to_move=='X':
				return eval_X
			else:
				return eval_O
		return value



	score = -999999 
	for i in range(COL): #each COL represents a possible move, and so we consider all 7 moves if possible
		board_copy = board.copy() 
		if board_copy[0][i]=='-': #ensure it is possible to play this move
			for jk in range(ROW): # process move
				if board_copy[jk][i]=='X' or board_copy[jk][i]=='O':
					board_copy[jk-1][i] = player_to_move
					break
			move = i #the curr move under consideration is the index i
			if player_to_move=='X': #setting the next player to move
				player_to_move = 'O'
			else:
				player_to_move = 'X'
			new_state = (name, player_to_move, board_copy) # packing tuple
			c+=1 #increase negamax counter
			value = - AlphaBeta(new_state, height-1,-beta,-alpha)
		
		if value >= score: #get max(score,value)
			best_move = move
			score = value

		if score >= beta: # beta cut-off. No need to consider further movies
			return score
		if score > alpha:
			alpha = score

	return score


if __name__ == '__main__':
	state = p1.read()
	h = int(input())
	val = AlphaBeta(state,h,-9999,9999)
	print ('move:',best_move,'v:',val,'c:',c,'t:',t,'nt',nt)
