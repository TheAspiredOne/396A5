
#Avery Tan(altan:1392212), Canopus Tong(canopus:1412275)


import sys


ROW = 6
COL = 7


def read():
	'''
	returns state
	'''
	global ROW 
	input_list = list()
	for line in sys.stdin:
		line = line.split()
		input_list.append(line)

	name, player_to_move = input_list[0]
	board = list()
	for i in range(1,ROW+1):
		row_board = list(input_list[i][0])
		board.append(row_board)
	h = None
	if len(input_list)==8:
		h= input_list[7][0]
		
	return (name, player_to_move, board,h)

def write(state):
	global ROW
	name,player_to_move,board,h = state
	for i in range(ROW):
		res_str = ''
		for j in board[i]:
			res_str+=j
		print (res_str)
	return



if __name__ == '__main__':
	state = read()
	write(state)