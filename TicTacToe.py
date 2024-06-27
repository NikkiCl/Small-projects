import copy


def rowChecker(board : list):
    for row in board:
        if row in CheckList:
            return True
    return False


def transpose(board: list):
    copyList = copy.deepcopy(board)
    tempList = []
    for row in range(len(board)):
        for col in range(len(board)):
            tempList.append(copyList[col][row])
    tempList = [tempList[i:i+3] for i in range(0, len(tempList), 3)]
    return tempList
        

def colChecker(tempList : list):
    for row in tempList:
        if row in CheckList:
            return True
    return False

    

def diagChecker1(board : list):
    diagChecker1List = []
    for row in range(len(board)):
            diagChecker1List.append(board[row][row])
    if diagChecker1List in CheckList:
        return True
    return False
        

def diagChecker2(board : list):
    diagChecker2List = []
    num = 0
    for row in range(2,-1,-1):
        diagChecker2List.append(board[num][row])
        num += 1
    if diagChecker2List in CheckList:
        return True
    return False


def playTurn(board : list,x : int,y: int,playerTurn : int,playerSymbols : list):
    ListLength = [0,1,2]
    if x not in ListLength or y not in ListLength or board[x][y] != "":
        return False
    board[x][y] = playerSymbols[playerTurn-1]
    for i in range(len(board)):
        print(board[i])

def winCondition(board : list):
    if rowChecker(board) or colChecker(transpose(board)) or diagChecker1(board) or diagChecker2(board):
        return True
    return False


def TicTacToe(WinningCount : list, playerSymbols : list):
    playerTurn = 1
    board = [["","",""],
             ["","","",],
             ["","",""]]
    while winCondition(board) == False:
        x,y = input(f"Player {playerTurn}, which row and column would you like to place an {playerSymbols[playerTurn-1]} on?").split(" ")
        if x.isdigit() == False or y.isdigit() == False:
            print("Please enter a number.")
            continue
        x = int(x)
        y = int(y)
        if playTurn(board,x,y,playerTurn,playerSymbols) == False:
            print("Please enter a value between 0-2 or a value on a square that isn't taken.")
            continue
        if winCondition(board):
            break
        if playerTurn == 1:
            playerTurn = 2
        else:
            playerTurn = 1
    print(f"Player {playerTurn} has won! \n")
    WinningCount[playerTurn-1] += 1
    return WinningCount
    

if __name__ == "__main__":
    playerSymbols = ["X","O"]
    CheckList = []
    for e in range(2):
        CheckInARow = [playerSymbols[e] for x in range(3)]
        CheckList.append(copy.deepcopy(CheckInARow))
        CheckInARow.clear()
    WinningCount = [0,0]
    scoreBoardName = ["Current","Final"]
    it = 0
    NumOfGames = int(input("How many games would you like to play?"))
    for i in range(NumOfGames):
        TicTacToe(WinningCount,playerSymbols)
        if i == NumOfGames-1:
            it += 1
        if NumOfGames > 1:
            print(f"""{scoreBoardName[it]} Scoreboard:
Player 1: {WinningCount[0]} wins
Player 2: {WinningCount[1]} wins\n""")
#To do list:
#Add better visuals (game is starting.., better formatting, etc)
#Check for bugs