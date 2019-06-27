#import colors
# Copy your logic functions from part A belo
# This file contains the core functions needed to validate moves in the Tic Tac Toe game
# Implement each function and choose "Run Tests" from the drop down menu to see how you did.
# Once you pass all the tests, you can move on to the next part of the project (user interaction).

# For all functions, "board" is assumed to be a nested list representing your Tic Tac Toe board.
# The board should be 3x3 and each spot should have an "X", "O" or " " (single space).



# N - is_board_full
# P - Checks if there are any open spaces on the board
# I - board: a 3x3 representation of the board as a nested list
# R - True if the board is full, False if there is at least one open space
def is_board_full(board):
	for lists in board:
		for item in lists:
			if item == " ":
				return False
	return True

# N - is_valid_move
# P - Checks if a mark can be placed at the location on the board
# I - board: a 3x3 representation of the board as a nested list
#		 location: an int (1-9) indicating where the user wants to place a mark
# R - True if the location is open on the board, False if it is already taken.

def is_valid_move(board, location):
	# Check if location is in range
	if location not in range (1,10):
		return False
	
	row = (location - 1) // len(board)
	col = (location - 1) % len(board[row])
	
	if board[row][col] == ' ':
		return True
	else: 
		return False

# N - winning_move
# P - Checks if the previous move resulted in the user winning the game
# I - board: a 3x3 representation of the board as a nested list
# R - True if the user now has 3 marks in a row, False if the user does not

def winning_move(board):
	# Check for horizontals
	for row in range(0,3):
		if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ":
			return True
			
	# Check for verticals
	for col in range(0,3):
		if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] != " ":
			return True
			
	# Check for diagonals
	#Diagonal top left to bottom right
	if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != " ":
			return True
	
	#Diagonal top right to bottom left
	if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != " ":
			return True
		
	return False
		
# Extra Credit: uncomment the following line and implement the function
# N - winning_move_possible
# P - Determines if the game is an inevitable tie or if someone can still win
# I - board: a 3x3 representation of the board as a nested list
# R - True if there's at least one combination of moves that would let a player win, False if the game must tie
# def winning_move_possible(board):
		


# Write your test code here:
'''
def winning_move_possible():
	#still working on it (temporarily moved on to part B)
'''

# END logic functions
def convert_to_board_index(board, choose_spot):
		if choose_spot in range(1,4):
			row = 0
		elif choose_spot in range(4,7):
			row = 1
		elif choose_spot in range(7,10):
			row = 2
			
		if choose_spot == 1 or choose_spot == 4 or choose_spot == 7:
			col = 0
		elif choose_spot == 2 or choose_spot == 5 or choose_spot == 8:
			col = 1
		elif choose_spot == 3 or choose_spot == 6 or choose_spot == 9:
			col = 2
			
		if current_player == player1:
			board[row][col] = 'X'
		elif current_player == player2:
			board[row][col] = 'O'

# N - print_board
# P - print the board with the current state of X, O, and blanks
# I - board: the 3x3 gameboard with the current state
# R - None
board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def print_board(board):
	print("\n {} | {} | {}\n---|---|---\n {} | {} | {}\n---|---|---\n {} | {} | {}".format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]))

welcome_message = """Welcome to Tic Tac Toe!

This game supports two players.
Each player will alternate placing an X or O on the 3x3 grid until one player gets 3 of their mark in a row, column, or diagonal.
If the board fills up without anyone getting 3 in a row, the players will tie.

You will tell the computer where to put your mark by using the numbering system below:

		 1 | 2 | 3 
		---|---|---
		 4 | 5 | 6 
		---|---|---
		 7 | 8 | 9

Good luck!
"""
			
print(welcome_message)

# Main game loop
player1 = input("Player 1, please enter your name: ")
player2 = input("Player 2, please enter your name: ")
current_player = player1
game_over = False
			
# The board starts empty
while not game_over:
	# 1. Ask the user (by name) to select a position on the board
	# print('board before choose: ',board)
	location = int(input("\n{}, please choose a location to place your X: ".format(current_player)))
	# 2. Check if the position is valid (not already marked) and update the board.
	#		If it's not valid, ask the user again until they give you a valid position.
	
	while not is_valid_move(board, location):
		print('Not a valid move')
		location = int(input("\n{}, please choose a location to place your X: ".format(current_player)))
	convert_to_board_index(board, location)
		# print('board after choose: ',board)
	# 3. Print the current board
	# print(board)
	print_board(board)

	# 4. Check if the player won the game
	#				Print which player won
	if winning_move(board) == True:
		print(current_player + " has won!")

	# 5. Check if the game is a tie
	#				Print that it is a tie
	#				For extra credit, check if there are no more possible moves to win the game and print that the game is ending early if so.
	if is_board_full(board) == True and winning_move(board) == False:
		print("Its a tie.")
	
	# 6. If there's a winner or tie
	#				End the game
	#				Ask if the user wants to play again
	#						If yes, clear the board
	#						If no, game_over = True
	if winning_move(board) == True:
		play_again = input("Would you like to play again?")
		if play_again == 'yes' or play_again == 'y':
			board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
		else:
			game_over = True
	
	# 7. Switch the players
	if current_player == player1:
			current_player = player2
	else:
			current_player = player1

# END main while loop
print("Thanks for playing!")