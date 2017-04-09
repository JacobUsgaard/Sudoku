import sys
import copy

m_board = [[0,0,0,1,6,0,7,0,0],[1,0,0,0,2,5,4,0,0],[5,0,0,3,7,8,9,0,1],[0,1,5,0,0,9,0,0,0],[2,7,0,4,0,1,0,3,9],[0,0,0,7,0,0,1,4,0],[9,0,3,8,1,6,0,0,2],[0,0,1,5,4,0,0,0,6],[0,0,6,0,9,3,0,0,0]]

boards = 0

pos = [x+1 for x in range(9)]
board_length = range(len(m_board))

def check_rows(board):
	# for each row
	#	check that the row has only one of the possibilities
	for x in board_length:
		p = list(pos)
		for y in board_length:
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False
	return True

def check_cols(board):
	# for each col
	# check that the col has only one of the possibilities
	for x in board_length:
		p = list(pos)
		for y in board_length:
			val = board[y][x]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False
	return True

def check_square(board, x_range, y_range):
	p = list(pos)
	for x in x_range:
		for y in y_range:
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False

def check_squares(board):
	# top left
	p = list(pos)
	for x in range(0,3):
		for y in range(0,3):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False

	# top mid
	p = list(pos)
	for x in range(0,3):
		for y in range(3,6):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False

	# top right
	p = list(pos)
	for x in range(0,3):
		for y in range(6,9):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False

	# mid left
	p = list(pos)
	for x in range(3,6):
		for y in range(0,3):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False
	
	# mid mid
	p = list(pos)
	for x in range(3,6):
		for y in range(3,6):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False

	# mid right
	p = list(pos)
	for x in range(3,6):
		for y in range(6,9):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False

	# bot left
	p = list(pos)
	for x in range(6,9):
		for y in range(0,3):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False

	# bot mid
	p = list(pos)
	for x in range(6,9):
		for y in range(3,6):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False
	
	# bot right
	p = list(pos)
	for x in range(6,9):
		for y in range(6,9):
			val = board[x][y]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False

	return True

def check_board(board):
	return check_rows(board) and check_cols(board) and check_squares(board)

def is_done(board):
	#check that all board spots are filled with non-zero
	for x in board_length:
		for y in board_length:
			val = board[x][y]
			if val == 0:
				return False
	return True

def play(board):
	global boards
	good = check_board(board)
	if not good:
		return
	elif is_done(board):
		print("Done!")
		print("Boards: " + str(boards))
		print_board(board)
		sys.exit()
	for x in board_length:
		for y in board_length:
			if board[x][y] != 0:
				continue
			else:
				b = copy.deepcopy(board)
				for p in pos:
					b[x][y] = p
					boards += 1
					play(b)
				return

def print_board(board):
	print("|----------------------|")
	for x in board_length:
		print("|", end="")

		for y in board_length:
			print(str(board[x][y]) + " ", end="")
			if (y + 1) % 3 == 0:
				print("| ", end="")
		if (x + 1) % 3 == 0:
			print()
			print("|----------------------|")
		else:
			print()
play(m_board)
#print(check_board(m_board))
