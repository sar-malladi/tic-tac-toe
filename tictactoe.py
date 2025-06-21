import random
import time
import sys 
        
board = []
winner = ""
nextMover = "player"

def setWinner():
    global board
    #check rows using set, which sees if all the elements of a list are the same
    for row in board:
        if len(set(row)) <= 1:
            if row[0] == " X ":
                return "player"
            elif row[0] == " O ": #matching squares could just be blanks
                return "computer"

    #check columns
    transposedBoard = [list(row) for row in zip(*board)]
    for transposedBoardRow in transposedBoard:
        if len(set(transposedBoardRow)) <= 1:
            if transposedBoardRow[0] == " X ":
                return "player"
            elif transposedBoardRow[0] == " O ": #matching squares could just be blanks
                return "computer"

    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == " X ":
            return "player"
        elif board[1][1] == " O ": #matching squares could just be blanks
            return "computer"
    
    return ""
            
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

def computerMove(): 
    global board
    randomEmptySquare = random.choice(generateEmptySquaresList())
    chosenRow = int(randomEmptySquare[0])
    chosenCol = int(randomEmptySquare[1])
    board[chosenRow][chosenCol] = " O "
    visualizeBoard(board)

def playerMove():
    import sys  # Needed for sys.exit()

def playerMove():
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
            playerMove()
        elif isEmpty(moveRow, moveCol):
            board[moveRow][moveCol] = " X "
            visualizeBoard(board)
        else:
            print("Try again — you may only select an empty square.")
            playerMove()
    except:
        print("Try again — your selected row and column must be a number.")
        playerMove()

def visualizeBoard (b):
    for rownum in range(len(b)):
        for colnum in range(len(b[rownum])):
            print (b[rownum][colnum], end = "")
            if colnum % 3 == 0 or colnum % 3 == 1:
                #if on the 1st or 2nd column
                print ("|", end = "")
        if rownum % 3 == 0 or rownum % 3 == 1: 
            #if on the 1st or 2nd row
            print("\n --+---+--")
            
def playGame():
    global board, winner, nextMover
    board = [["   ", "   ", "   ",] , ["   ", "   ", "   "] , ["   ", "   ", "   "]]
    
    #reset nextMover and winner in case they are replaying the game
    nextMover = "player"
    winner = ""
    
    print("Let's play Tic Tac Toe!")

    while (winner == "" and len(generateEmptySquaresList()) != 0):
        if nextMover == "player":
            print("\nYour turn!")
            playerMove()
            winner = setWinner()
            nextMover = "computer"
        elif nextMover == "computer":
            print("\nMy turn! Selecting a move...")
            time.sleep(2)
            computerMove()
            winner = setWinner()
            nextMover = "player"

    if (winner == "player"):
        print ("You won the game! Final board:")
    elif (winner == "computer"):
        print ("You lost the game. Final board:")
    else:
        print ("It's a tie! Final board:")
    visualizeBoard(board)

playGame()

while input("\nPlay again? (y/n): ").lower() == "y":
    playGame()

print("Thanks for playing!")
sys.exit()

#at the end: try to use webscraping to scrape online tic-tac-toe games and user can watch?
#            add a probability of player's chance of winning? go back and do #check columns the proper way instead of using zip, and maybe same for rows