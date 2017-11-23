

#Avery Tan(altan:1392212), Canopus Tong(canopus:1412275)


import time
import numpy as np
import p4
import p5


"""
this is the actual exp program that carries out our experiments
"""
if __name__ == '__main__':
	
	files  = ['T1','T2','T3','T4','T5']
	runtimes_alp = np.zeros(5)
	runtimes_neg = np.zeros(5)
	stats_alp = []
	stats_neg=[]

	
	for i in range(5): #running on all 5 of our exp

		input_list = list()

		f = open(files[i],'r')
		for line in f:
			line = line.split()
			input_list.append(line)

		name, player_to_move = input_list[0]
		board = list()
		for j in range(1,7):
			row_board = list(input_list[j][0])
			board.append(row_board)
		h = None
		if len(input_list)==8:
			h= input_list[7][0]
			
		state = (name, player_to_move, board,h)

		f.close()


		#run exp
		start_neg = time.time()
		val_neg,bestMove_neg = p4.NegaMax(state,int(state[3]), False)
		end_neg = time.time()
		runtime_neg = abs(start_neg- end_neg)
		runtimes_neg[i]=runtime_neg


		statistics = p4.getStats(state,int(state[3]), False)
		stats_neg.append(statistics)



		start_alp = time.time()
		val_alp,bestMove_alp = p5.AlphaBeta(state,state[3],False,-9999,9999)
		end_alp = time.time()
		runtime_alp = abs(start_alp- end_alp)
		runtimes_alp[i]=runtime_alp

		statistics = p5.getStats(state,state[3],False,-9999,9999)
		stats_alp.append(statistics)

		avg_runtime_NEGAMAX = (runtimes_neg.sum())/5.0
		avg_runtime_ALPHABETA = (runtimes_alp.sum())/5.0



	print(runtimes_neg,runtimes_alp)
	print(stats_neg,'\n',stats_alp,'\n')


	max_nodes_visited_NEGAMAX = 0
	min_nodes_visited_NEGAMAX = 99999
	avg_nodes_NEGAMAX = 0.0
	for i in stats_neg:
		avg_nodes_NEGAMAX+=i[2]
		if i[2]>max_nodes_visited_NEGAMAX:
			max_nodes_visited_NEGAMAX = i[2]
		if i[2]<min_nodes_visited_NEGAMAX:
			min_nodes_visited_NEGAMAX = i[2]
	avg_nodes_NEGAMAX/=5.0



	max_nodes_visited_ALPHABETA = 0
	min_nodes_visited_ALPHABETA = 99999
	avg_nodes_ALPHABETA = 0.0
	for i in stats_alp:
		avg_nodes_ALPHABETA+=i[2]
		if i[2]>max_nodes_visited_ALPHABETA:
			max_nodes_visited_ALPHABETA = i[2]
		if i[2]<min_nodes_visited_ALPHABETA:
			min_nodes_visited_ALPHABETA = i[2]
	avg_nodes_ALPHABETA/=5.0



	print ('max_nodes_visited_NEGAMAX: ',max_nodes_visited_NEGAMAX)
	print ('max_nodes_visited_ALPHABETA: ', max_nodes_visited_ALPHABETA)
	print ('min_nodes_visited_NEGAMAX: ', min_nodes_visited_NEGAMAX)
	print ("min_nodes_visited_ALPHABETA: ", min_nodes_visited_ALPHABETA)
	print ('avg_nodes_NEGAMAX: ', avg_nodes_NEGAMAX)
	print ('avg_nodes_ALPHABETA: ', avg_nodes_ALPHABETA)
	print ('avg_runtime_NEGAMAX: ', avg_runtime_NEGAMAX)
	print ('avg_runtime_ALPHABETA: ', avg_runtime_ALPHABETA)














