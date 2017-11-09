import copy
import sys
import re

board_length = 9
m_board = [0] * board_length
for i in range(board_length):
	m_board[i] = [0] * board_length

boards = 0
pos = [x+1 for x in range(board_length)]
board_range = range(board_length)

def check_rows(board):
	# for each row
	#	check that the row has only one of the possibilities
	for x in board_range:
		p = list(pos)
		for y in board_range:
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
	# 	check that the col has only one of the possibilities
	for x in board_range:
		p = list(pos)
		for y in board_range:
			val = board[y][x]
			if val == 0:
				continue
			elif val in p:
				p.remove(val)
			else:
				return False
	return True

def check_square(board, x_range, y_range):
	# check to make sure that this square has only one of the possibilties
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
	return True

def check_squares(board):
	# check all mini squares
	ranges = [range(0,3), range(3,6), range(6,9)]

	for x in ranges:
		for y in ranges:
			if not check_square(board,x,y):
				return False

	return True

def is_good(board):
	# check to make sure the board complies with Sudoku rules
	return check_rows(board) and check_cols(board) and check_squares(board)

def is_done(board):
	# check that all board spots are filled with non-zero
	for x in board_range:
		for y in board_range:
			val = board[x][y]
			if val == 0:
				return False
	return True

def play(board):
	global boards

	if not is_good(board):
		return

	elif is_done(board):
		print("Boards: " + str(boards))
		print_board(board)
		return

	for x in board_range:
		for y in board_range:
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
	for x in board_range:
		print("|", end="")

		for y in board_range:
			print(str(board[x][y]) + " ", end="")
			if (y + 1) % 3 == 0:
				print("| ", end="")
		if (x + 1) % 3 == 0:
			print()
			print("|----------------------|")
		else:
			print()
def show_help():
	print("usage:")
	print("sudoku.py file file_name")
	print("sudoku.py string input_string")
	sys.exit()

def into_board(string, board):

	pattern = re.compile("\D")
	m_string = pattern.sub("", string)

	expected = board_length * board_length;
	actual = len(m_string)

	if(expected != actual):
		print("incorrect number of lines")
		print("expected: " + str(expected));
		print("actual: " + str(actual));
		sys.exit()

	for row in board_range:
		for col in board_range:
			board[row][col] = int(m_string[board_length * row + col])

if(len(sys.argv) != 3):
	show_help()

input_type=sys.argv[1]
input_string=sys.argv[2]
all_lines = ""

if(input_type == "file"):
	try:
		with open(input_string, 'r') as input_file:
			all_lines = input_file.read()
	except Exception as exception:
		print("failed to read file")
		print(exception)
		sys.exit()

elif(input_type == "string"):
	all_lines = input_string
else:
	show_help()

into_board(all_lines, m_board)

print_board(m_board)
play(m_board)
