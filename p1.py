
ROW = 6
COL = 7


def read():
	global ROW
	name, player_to_move = input().split()
	board = list()
	for i in range(ROW):
		row_board = list(input())
		board.append(row_board)
	return (name, player_to_move, board)

def write(state):
	global ROW
	name,player_to_move,board = state
	for i in range(ROW):
		res_str = ''
		for j in board[i]:
			res_str+=j
		print (res_str)
	return



if __name__ == '__main__':
	state = read()
	write(state)