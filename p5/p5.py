

#Avery Tan(altan:1392212), Canopus Tong(canopus:1412275)



import p1
import p2
import p3
import p4
import copy

COL = 7
ROW = 6
c = 1 # number of negamx calls
v = None #root value in view of player to move
best_move = None
t = 0# number of terminal nodes
nt = 0 # number of non terminal nodes
move_values = {}




def AlphaBeta(state, height,cf, alpha , beta):
	'''
	Our version of alphabeta retains the basic form of alphabeta with an added improvement
	in terms of keeping the height parameter and using it to 'bound' our search space.
	Maintaining the use of the height when running this algorithm will result in picking
	moves that result in either quickest victory or slowest loss.



	results of our experiments:

	max_nodes_visited_NEGAMAX:  292761
	max_nodes_visited_ALPHABETA: 26723

	min_nodes_visited_NEGAMAX:   25383
	min_nodes_visited_ALPHABETA:   643

	avg_nodes_NEGAMAX:          188128.6
	avg_nodes_ALPHABETA:         17544.2

	avg_runtime_NEGAMAX:   5.15889849663
	avg_runtime_ALPHABETA: 0.756984472275



	As we can see from the data above, there is a very marked difference between
	NegaMax and AlphaBeta. 

	Negamax visits approximately 10 times more nodes than Alphabeta does on average.

	The runtime difference between the 2 is also of key interest. On average, AlphaBeta
	takes less than a second to search.

	These results are unsurprising since AlphaBeta is able to prune off certain branches
	from the search tree and the savings in terms of computation and runtime is quite
	significant.


	The dataset used as well as the exp.py code used to implement this experiment is available
	from https://github.com/TheAspiredOne/396A5


	'''
	global COL, ROW, c, v, best_move, t, nt, move_values

	move_heuristic_dict=dict()


	if height == None:
		height = 10000000
	else:
		height = int(height)

	name, player_to_move, board, h = state #unpack the tuple
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
				return (eval_O,None)
			else:
				return (eval_X,None)
		return (value,None)


	score = -999999 #approximation of -inf
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
			value_of_move = p3.calculate_heuristics(new_state) #evaluating heuristic value after making move
			move_heuristic_dict[i]=value_of_move
			sorted_moves = sorted(move_heuristic_dict, reverse = True, key = move_heuristic_dict.get)
			
		

			c+=1 #increase negamax counter


			

			value,successor_move = AlphaBeta(new_state, height-1, True,-beta,- alpha)
			value = -value


			if value >= score:
				bestMove = i
				score = value

				if score > alpha:
					alpha = score
				if score >= beta: # beta cut-off. No need to consider further movies
					return (score, bestMove)
				

	return (score,bestMove)


def getStats(a,b,cc,d,e):
	global c,t,nt
	val,bestMove = AlphaBeta(a,b,cc,d,e)
	return (bestMove,val,c,t,nt)


if __name__ == '__main__':
	state = p1.read()
	val,bestMove = AlphaBeta(state,state[3],False,-9999, 9999)
	print('move: '+str(bestMove)+' v: '+str(val)+' c: '+str(c)+' t: '+str(t)+' nt: '+str(nt))


