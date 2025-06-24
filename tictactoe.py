import random
import time
import sys 
        
board = []
winner = ""
nextMover = "human"

def setWinner():
    global board
    for row in board:
        if len(set(row)) <= 1:
            if row[0] == " X ":
                return "computer"
            elif row[0] == " O ": #matching squares could just be blanks
                return "human"

    #check columns
    transposedBoard = [list(row) for row in zip(*board)]
    for transposedBoardRow in transposedBoard:
        if len(set(transposedBoardRow)) <= 1:
            if transposedBoardRow[0] == " X ":
                return "computer"
            elif transposedBoardRow[0] == " O ": #matching squares could just be blanks
                return "human"

    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == " X ":
            return "computer"
        elif board[1][1] == " O ": #matching squares could just be blanks
            return "human"
    
    return ""

def getBestMove():
       bestScore = -1000000000000000000
       bestMove = ""

       for square in generateEmptySquaresList():
           #place X in that square
            chosenRow = int(square[0])
            chosenCol = int(square[1])
            board[chosenRow][chosenCol] = " X "

           #Recursively call minimax with the next depth and the minimizing player
            score = minimax(0, "human")
           #Reset the move
            board[chosenRow][chosenCol] = "   "

           # Update the best score
            if score > bestScore:
               bestScore = score
               bestMove = square

       return bestMove

def minimax(depth, player):
   global board
   # Base case: Check if the game is over
   if setWinner() == "computer":
       return 1
   if setWinner() == "human":
       return -1
   if len(generateEmptySquaresList()) == 0 and setWinner() == "":
       return 0

   # If it's the computer's turn (maximizing)
   if player == "computer":
       bestScore = -1000000000000000000
       for square in generateEmptySquaresList():
           #place X in that square
           chosenRow = int(square[0])
           chosenCol = int(square[1])
           board[chosenRow][chosenCol] = " X "

           #calculate the associated score for that move
           score = minimax(depth + 1, "human")
           
           #undo the move
           board[chosenRow][chosenCol] = "   "
           if int(score) > int(bestScore):
               bestScore = score
       return bestScore

   # If it's the human's turn (goal is to find minimum score- assuming human will play optimally)
   if player == "human":
       bestScore = 1000000000000000000
       for square in generateEmptySquaresList():
           #place O in that square
           chosenRow = int(square[0])
           chosenCol = int(square[1])
           board[chosenRow][chosenCol] = " O "

           #calculate the associated score for that move
           score = minimax(depth + 1, "computer")

           #undo the move
           board[chosenRow][chosenCol] = "   "
           if int(score) < int(bestScore):
               bestScore = score
       return bestScore
            
def isEmpty(r, c):
    global board
    if board[r][c] == "   ":
        return True

def generateEmptySquaresList():
    emptySquaresList = []
    for rowNum in range(3):
        for colNum in range(3):
            if isEmpty(rowNum, colNum):
                emptySquaresList.append(str(str(rowNum) + str(colNum)))
    return emptySquaresList

import sys

def computerMove():
    global board
    moveRow = int(getBestMove()[0])
    moveCol = int(getBestMove()[1])
    board[moveRow][moveCol] = " X "
    visualizeBoard(board)

def humanMove():
    global board
    moveRow = input("Enter the row number (1-3) of your move, or 'q' to quit: ").strip()
    if moveRow.lower() == "q":
        print("Thanks for playing!\nExiting the game...")
        sys.exit()
    
    moveCol = input("Enter the column number (1-3) of your move, or 'q' to quit: ").strip()
    if moveCol.lower() == "q":
        print("Thanks for playing!\nExiting the game...")
        sys.exit()

    try:
        moveRow = int(moveRow) - 1
        moveCol = int(moveCol) - 1
        if moveRow < 0 or moveRow > 2 or moveCol < 0 or moveCol > 2:
            print("Try again — you must select 1, 2, or 3.")
            humanMove()
        elif isEmpty(moveRow, moveCol):
            board[moveRow][moveCol] = " O "
            visualizeBoard(board)
        else:
            print("Try again — you may only select an empty square.")
            humanMove()
    except:
        print("Try again — your selected row and column must be a number.")
        humanMove()

def visualizeBoard (b):
    for rownum in range(len(b)):
        for colnum in range(len(b[rownum])):
            print (b[rownum][colnum], end = "")
            if colnum % 3 == 0 or colnum % 3 == 1:
                print ("|", end = "")
        if rownum % 3 == 0 or rownum % 3 == 1: 
            #if on the 1st or 2nd row
            print("\n --+---+--")
            
def playGame():
    global board, winner, nextMover
    board = [["   ", "   ", "   ",] , ["   ", "   ", "   "] , ["   ", "   ", "   "]]
    
    #reset nextMover and winner in case they are replaying the game
    nextMover = "human"
    winner = ""
    
    print("\nLet's play Tic Tac Toe!")
    visualizeBoard(board)

    while (winner == "" and len(generateEmptySquaresList()) != 0):
        if nextMover == "human":
            print("\nYour turn!")
            humanMove()
            winner = setWinner()
            nextMover = "computer"
        elif nextMover == "computer":
            print("\nMy turn! Selecting a move...")
            time.sleep(2)
            computerMove()
            winner = setWinner()
            nextMover = "human"

    if (winner == "human"):
        print ("You won the game! Final board:")
    elif (winner == "computer"):
        print ("You lost the game. Final board:")
    else:
        print ("It's a tie! Final board:")
    visualizeBoard(board)

playGame()

while input("\nPlay again? (y/n): ").lower() == "y":
    playGame()

print("Thanks for playing!\nExiting the game...")
sys.exit()

#at the end: try to use webscraping to scrape online tic-tac-toe games and user can watch?
#            add a probability of human's chance of winning? go back and do #check columns the proper way instead of using zip, and maybe same for rows