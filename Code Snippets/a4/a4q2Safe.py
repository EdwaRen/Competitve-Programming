#Exercise2
    
def eraseTable(tab):
   '''
   (list) -> None
   This function prepares the game table (array)
   by putting '-' in all the elements.
   It does not create a new array
   Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   # Iterating over rows
   for i in range(3):
       for j in range(3):
           tab[i][j] = '-'
  
def verifyWin(tab):
    '''(list) -> bool
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    * Verify if there is a winner.
    * Look for 3 X's and O's in a row, column, and diagonal.
    * If we find one, we display the winner (the message "Player X has won"
    * or "Player O has won!") and returns True.
    * If there is a draw (verify it with the function testdraw),
    * display "It is a draw" and returns True.
    * If the game is not over, returns False.
    * The function call the functions testrows, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Those functions returns the winner 'X' or 'O', or '-' if there is no winner.
    '''
    # Checking for draw
    if testRows(tab)=='X' or testCols(tab)=='X' or testDiags(tab)=='X':
        print("Player X has won!")
    elif testRows(tab)=='O' or testCols(tab)=='O' or testDiags(tab)=='O':
        print("Player O has won!")
    else:
        print("It is a draw")
        return False
    return True


def testRows(tab):
    ''' (list) -> str
    * verify if there is a winning row.
    * Look for three 'X' or three 'O' in a row.
    * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''
    # Iterating over rows
    for lst in tab:
        if ''.join(lst) == 'XXX':
            return 'X'
            
    # Iterating over rows
    for lst in tab:
        if ''.join(lst) == 'OOO':
            return 'O'
            
    return '-'
  
  
def testCols(tab):
    ''' (list) -> str
    * verify a winning column.
    * look for three 'X' or three 'O' in a column.
    * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''
    # Iterating over columns
    for i in range(3):
        c = 0
        for j in range(3):
            if tab[j][i] == 'X':
                c = c+1
        if c==3:
            return 'X'
            
    # Iterating over columns
    for i in range(3):
        c = 0
        for j in range(3):
            if tab[j][i] == 'O':
                c = c+1
        if c==3:
            return 'O'
    
    return '-' 
  
def testDiags(tab):
    ''' (list) -> str
    * Look for three 'X' or three 'O' in a diagonal.
    * If it is the case, the character 'X' or 'O' is returned
    * otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''
    diag1 = ''.join([str(tab[i][i]) for i in range(3)])
    diag2 = ''.join([str(tab[2-i][i]) for i in range(3)])
    if diag1 == 'XXX' or diag2 == 'XXX':
        return 'X'
    elif diag1 == 'OOO' or diag2 == 'OOO':
        return 'O'
    
    return '-'
  
  
def testDraw(tab):
   ''' (list) -> bool
   * verify if there is a draw
   * check if all the array elements have X or O, not '-'.
   * If we do not find find any '-' in the array, return True.
   * If there is any '-', return false.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   # Iterating over rows
   for lst in tab:
       for ch in lst:
           # Check for -
           if ch == '-':
               return False
   return True


def displayTable (tab):
   '''
       (list) -> None
       display the table of the game
       Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
       The format is:
         0 1 2
       0 - - O
       1 - X -
       2 - - X
   '''
   print("   ", end="")
   col = 0
   while col < len(tab):
       print(col, end=" ")
       col += 1
   print()
   row = 0
   while row < len(tab):
       print(row, end="")
       col = 0
       while col < len(tab[row]):
           print(" ",tab[row][col], end="")
           col += 1
       print()
       row += 1

def play(tab, player):
    '''
    (list, str) -> None
    Play a step of the game
    Preconditions: tab is a reference to the n x n tab containing '-', 'X' and 'O'
    The player is either X or O
    tab is modified (an element has changed)
    '''
    
    valid = False
    while not valid:
        # Get the new place
        place = [-1,-1]
        print ("player ",player, end="")
        print(", Provide the row and column from 0 to", (len(tab)-1), ": ")
        place[0] = int(input("Row: "))
        place[1] = int(input("Column: "))

        # Get new location if invalid
        if ((0 <= place[0] < len(tab)) and (0 <= place[1] < len(tab))):

            # Set location if valid
            valid = tab[place[0]][place[1]] != '-'
            if valid:
                print("the position", place[0], place[1], "is busy")
                valid = False
            else:
                valid = True
                tab[place[0]][place[1]] = player
      
def main():
    # Create the game table
    table = [['-','-','-'],['-','-','-'],['-','-','-']]
    
    response = input("Start a game (O or N): ")
    while response == 'o' or response == 'O':
        eraseTable(table)
        winner = False
        currentPlayer = 'X'
        while not winner:
            displayTable(table)
            play(table,currentPlayer)
            winner = verifyWin(table)
            currentPlayer = 'O' if currentPlayer == 'X' else 'X'
            
        displayTable(table) 
        response = input("Start a game (O or N): ") 

main()