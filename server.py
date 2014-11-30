#!/usr/bin/env python
__author__ = 'Loc Le'

import random
import socket

TCP_IP = '192.168.56.1'
TCPPortForClient1 = 5005
TCPPortForClient2 = 15000
BufferSize = 10000
turn = 'N'  # Whose turn it is, X always goes first
turn_num = 0
winner = 'N'  # Who won the game
player1 = 'N'
player2 = 'N'

# Create and initialize the game board
drawGamingBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def check_winner():
    # Moves 1 -> 2 -> 3
    if drawGamingBoard[0] == 'X' and drawGamingBoard[1] == 'X' and drawGamingBoard[2] == 'X':
        the_winner_is = 'X'
    elif drawGamingBoard[0] == 'O' and drawGamingBoard[1] == 'O' and drawGamingBoard[2] == 'O':
        the_winner_is = 'O'
    # Moves 1 -> 4 -> 7
    elif drawGamingBoard[0] == 'X' and drawGamingBoard[3] == 'X' and drawGamingBoard[6] == 'X':
        the_winner_is = 'X'
    elif drawGamingBoard[0] == 'O' and drawGamingBoard[3] == 'O' and drawGamingBoard[6] == 'O':
        the_winner_is = 'O'
    #Moves 7 -> 8 -> 9
    elif drawGamingBoard[6] == 'X' and drawGamingBoard[7] == 'X' and drawGamingBoard[8] == 'X':
        the_winner_is = 'X'
    elif drawGamingBoard[6] == 'O' and drawGamingBoard[7] == 'O' and drawGamingBoard[8] == 'O':
        the_winner_is = 'O'
    #Moves 3 -> 6 -> 9
    elif drawGamingBoard[2] == 'X' and drawGamingBoard[5] == 'X' and drawGamingBoard[8] == 'X':
        the_winner_is = 'X'
    elif drawGamingBoard[2] == 'O' and drawGamingBoard[5] == 'O' and drawGamingBoard[8] == 'O':
        the_winner_is = 'O'
    #Moves 4 -> 5 -> 6
    elif drawGamingBoard[3] == 'X' and drawGamingBoard[4] == 'X' and drawGamingBoard[5] == 'X':
        the_winner_is = 'X'
    elif drawGamingBoard[3] == 'O' and drawGamingBoard[4] == 'O' and drawGamingBoard[5] == 'O':
        the_winner_is = 'O'
    #Moves 2 -> 5 -> 8
    elif drawGamingBoard[1] == 'X' and drawGamingBoard[4] == 'X' and drawGamingBoard[7] == 'X':
        the_winner_is = 'X'
    elif drawGamingBoard[1] == 'O' and drawGamingBoard[4] == 'O' and drawGamingBoard[7] == 'O':
        the_winner_is = 'O'
    #Moves 3 -> 5 -> 7
    elif drawGamingBoard[2] == 'X' and drawGamingBoard[4] == 'X' and drawGamingBoard[6] == 'X':
        the_winner_is = 'X'
    elif drawGamingBoard[2] == 'X' and drawGamingBoard[4] == 'X' and drawGamingBoard[6] == 'X':
        the_winner_is = 'O'
    #Moves 1 -> 5 -> 9
    elif drawGamingBoard[0] == 'X' and drawGamingBoard[4] == 'X' and drawGamingBoard[8] == 'X':
        the_winner_is = 'X'
        # return winner
    elif drawGamingBoard[0] == 'O' and drawGamingBoard[4] == 'O' and drawGamingBoard[8] == 'O':
        the_winner_is = 'O'
    #Winner hasn't been found yet
    else:
        the_winner_is = 'N'
    return the_winner_is


def switch_player(turn):
    # Initialized to False to use for while loop
    player_finish_move = False
    if 'player1' == turn:
        conn.send("\nTake your turn, for help type --help")
        data = conn.recv(BufferSize)
        print "recieved data: ", data
        # Take input from the user and add it into the game board
        while not player_finish_move:
            #Split the data and turn it to all uppercase to compare
            data_split = data.upper().split()
            if data_split[0] == "--HELP":
                #Call the function to print help and show the valid commands
                print_help()
                data = conn.recv(BufferSize)
                print "received data: ", data
                data_split = data.upper().split()
            if len(data_split) == 2 and data_split[0] == 'PICK':
                #Check to see if the spot on the board is taken
                spot = data_split[1]
                #It's spot-1 because the index of the array starts at 0, not 1.
                if drawGamingBoard[int(spot) - 1] == " ":
                    #Put the move into the game board
                    drawGamingBoard[int(spot) - 1] = player1
                    #turn = 'player2' #Change turns
                    player_finish_move = True
                    #Spot already taken
                else:
                    conn.send("\nThe spot you want to take is already taken. Please try again.")
                    data = conn.recv(BufferSize)
                    print "received data: ", data
            #The player command is invalid
            else:
                conn.send("\nThe command you entered is invalid, type --help to see valid commands. Please try again.")
                data = conn.recv(BufferSize)
                print "received data: ", data
    else:
        conn2.send("\nTake your turn, for help type --help")
        data = conn2.recv(BufferSize)
        print "received data: ", data
        # Take input from the user and add it into the game board
        while not player_finish_move:
            #Split the data and turn it to all uppercase to compare
            data_split = data.upper().split()
            if data_split[0] == "--HELP":
                #Call the function to print help and show the valid commands
                print_help()
                data = conn2.recv(BufferSize)
                print "received data: ", data
                data_split = data.upper().split()
            if len(data_split) == 2 and data_split[0] == 'PICK':
                #Check to see if the spot on the board is taken
                spot = data_split[1]
                #It's spot-1 because the index of the array starts at 0, not 1.
                if drawGamingBoard[int(spot) - 1] == " ":
                    #Put the move into the game board
                    drawGamingBoard[int(spot) - 1] = player2
                    #turn = 'player1' #Change turns
                    player_finish_move = True
                    #Spot already taken
                else:
                    conn2.send("\nThe spot you want to take is already taken. Please try again.")
                    data = conn2.recv(BufferSize)
                    print "received data: ", data
            #The player command is invalid
            else:
                conn2.send("\nThe command you entered is invalid, type --help to see valid commands. Please try again.")
                data = conn2.recv(BufferSize)
                print "received data: ", data


# Function to print the game board
def print_gaming_board():
    if turn == 'player1':
        conn.send("\n" + drawGamingBoard[6] + "  |    " + drawGamingBoard[7] + "  |     " + drawGamingBoard[8])
        conn.send("\n --------------------------------------------")
        conn.send("\n" + drawGamingBoard[3] + "  |    " + drawGamingBoard[4] + "  |     " + drawGamingBoard[5])
        conn.send("\n --------------------------------------------")
        conn.send("\n" + drawGamingBoard[0] + "  |    " + drawGamingBoard[1] + "  |     " + drawGamingBoard[2])
    else:
        conn2.send("\n" + drawGamingBoard[6] + "  |    " + drawGamingBoard[7] + "  |     " + drawGamingBoard[8])
        conn2.send("\n --------------------------------------------")
        conn2.send("\n" + drawGamingBoard[3] + "  |    " + drawGamingBoard[4] + "  |     " + drawGamingBoard[5])
        conn2.send("\n --------------------------------------------")
        conn2.send("\n" + drawGamingBoard[0] + "  |    " + drawGamingBoard[1] + "  |     " + drawGamingBoard[2])


# Function to print the commands(--help)
def print_help():
    if turn == 'player1':
        conn.send(
            "\nTo make a move, type: MAKE MOVE #, where # is the number on the grid. "
            "For example, MAKE MOVE 5 marks your symbol in spot 5 if it isn't taken yet.")
        conn.send("\nYou will not be able to make a move in a spot that is already taken.")
    else:
        conn2.send(
            "\nTo make a move, type: MAKE MOVE #, where # is the number on the grid. "
            "For example, MAKE MOVE 5 marks your symbol in spot 5 if it isn't taken yet.")
        conn2.send("\nYou will not be able to make a move in a spot that is already taken.")


#Set up server and listen for the first client
#Set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind the socket, assigns IP and port to the socket
s.bind((TCP_IP, TCPPortForClient1))
#Listens for clients
s.listen(1)

#First client trying to connect
conn, addr = s.accept()
print "Connection Address: ", addr
conn.send("\nWelcome to the Tic-Tac-Toe server.")
conn.send("\nPlease wait while we try to find you an opponent.")


#Listen for the second player to connect
#Set up the socket
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind the socket, assigns IP and port to the socket
s2.bind((TCP_IP, TCPPortForClient2))
#Listens for clients
s2.listen(1)

#Second client trying to connect
conn2, addr2 = s2.accept()
print "Connection Address: ", addr2
conn2.send("\n Welcome to the Tic-Tac-Toe server.")
conn2.send("\nPlease wait while we try to find you an opponent.")


#player1 == conn, player2 == conn2
#Set the turn to who gets to get first (Whoever X is)
rand = random.randint(1, 2)
if rand == 1:
    player1 = 'X'
    player2 = 'O'
    turn = 'player1'
else:
    player1 = 'O'
    player2 = 'X'
    turn = 'player2'

#Tell the players what symbol they are.
conn.send("\nYour symbol has been randomly chosen, you are: " + player1 + ". X goes first.")
conn2.send("\nYour symbol has been randomly chosen, you are: " + player2 + ". X goes first.")


#Start the game, don't end the game until a winner is found
while winner == 'N':
    #Prints out to show what the other player played
    print_gaming_board()
    #Client takes their turn
    switch_player(turn)
    #Prints out the move they just made on the new updated board
    print_gaming_board()
    #Check to see if thee is a winner
    winner = check_winner()
    turn_num += 1

    #This changes the turns for the players
    if turn == 'player1':
        turn = 'player2'
    else:
        turn = 'player1'

    #This checks for winners/ties in the game
    if winner == 'X':
        #This will print out the completed game board to the losing player
        conn.send("\nWinner is X")
        conn2.send("\nWinner is X")
        print_gaming_board()

        break
    if winner == 'O':
        #This will print out the completed game board to the losing player
        conn.send("\nWinner is O")
        conn2.send("\nWinner is O")
        print_gaming_board()

        break
    #The board will be filled at this point
    if turn_num == 9:
        #This will print out the completed game board to the other player
        conn.send("\nThis game is a tie")
        conn2.send("\nThis game is a tie")
        print_gaming_board()

        break

#Close the connections to the 2 other clients after a winner is found
conn.close()
conn2.close()