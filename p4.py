
#Avery Tan(altan:1392212), Canopus Tong(canopus:1412275)



import p1
import p2
import p3
import copy

COL = 7
ROW = 6
c = 1 # number of negamx calls
v = None #root value in view of player to move
best_move = None
t = 0# number of terminal nodes
nt = 0 # number of non terminal nodes
move_values = {}




def NegaMax(state, height,cf):
	global COL, ROW, c, v, best_move, t, nt, move_values

	name, player_to_move, board, h = state #unpack the tuple
	move=None
	isTerminal = False #termination flag
	O,X,full = p2.evaluate_state(state) #these will tell us whether we are at terminal state

	if O ==1 or X ==1 or full == 1:
		isTerminal = True
	# print('also here')

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
				return (eval_O,None)
			else:
				return (eval_X,None)
		return (value,None)
	# print('here')


	score = -999999 #approximation of -inf?
	bestMove=None

	if cf == True:
		if player_to_move=='X': #setting the next player to move
				player_to_move = 'O'
		else:
			player_to_move = 'X'



	for i in range(COL): #each COL represents a possible move, and so we consider all 7 moves if possible
		board_copy = copy.deepcopy(board) #copy board so we don't mess it up
		
		if board_copy[0][i]=='-': #ensure it is possible to play this move
			for jk in range(ROW): # process move
				if board_copy[jk][i]=='X' or board_copy[jk][i]=='O':
					board_copy[jk-1][i] = player_to_move
					break
				if jk == 5:
					board_copy[jk][i]=player_to_move
			

			

			new_state = (name, player_to_move, board_copy, h) # packing tuple
			c+=1 #increase negamax counter
			# print (new_state,height-1)

			

			value,successor_move = NegaMax(new_state, height-1, True)
			value = -value
			if value > score:
				bestMove = i
				score = value


	return (score,bestMove)

def getStats(a,b,cc):
	global c,t,nt
	val,bestMove = NegaMax(a,b,cc)
	return (bestMove,val,c,t,nt)


if __name__ == '__main__':
	state = p1.read()
	val,bestMove = NegaMax(state,int(state[3]),False)
	print('move: '+str(bestMove)+' v: '+str(val)+' c: '+str(c)+' t: '+str(t)+' nt: '+str(nt))





