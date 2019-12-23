

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
   for i in range(0, 3):
       for j in range(0, 3):
           tab[i][j] = '-'
  
def verifyWinner(tab):
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
   if testDraw(tab):
       print("It is a draw")
       return True
   elif testRows(tab)=='X' or testCols(tab)=='X' or testDiags(tab)=='X':
       print("Player X has won!")
       return True
   elif testRows(tab)=='O' or testCols(tab)=='O' or testDiags(tab)=='O':
       print("Player O has won!")
       return True
      
   return False # to change


def testRows(tab):
   ''' (list) -> str
   * verify if there is a winning row.
   * Look for three 'X' or three 'O' in a row.
   * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   # Iterating over rows
   for lst in tab:
       c = 0
       # Iterating over columns
       for ch in lst:
           if ch == 'X':
               c = c+1
       # Checking for 3 X
       if c==3:
           return 'X'
          
   # Iterating over rows
   for lst in tab:
       c = 0
       # Iterating over columns
       for ch in lst:
           if ch == 'O':
               c = c+1
       # Checking for 3 O
       if c==3:
           return 'O'
          
   return '-' # to be modified so that it returns the winner, or '-' if there is no winner
  
  
def testCols(tab):
   ''' (list) -> str
   * verify a winning column.
   * look for three 'X' or three 'O' in a column.
   * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   # Iterating over columns
   for i in range(0, 3):
       c = 0
       # Iterating over rows
       for j in range(0, 3):
           if tab[j][i] == 'X':
               c = c+1
       # Checking for 3 X
       if c==3:
           return 'X'
          
   # Iterating over columns
   for i in range(0, 3):
       c = 0
       # Iterating over rows
       for j in range(0, 3):
           if tab[j][i] == 'O':
               c = c+1
       # Checking for 3 O
       if c==3:
           return 'O'
  
   return '-' #to be modified so that it returns the winner, or '-' if there is no winner
  
def testDiags(tab):
   ''' (list) -> str
   * Look for three 'X' or three 'O' in a diagonal.
   * If it is the case, the character 'X' or 'O' is returned
   * otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   if (tab[0][0]=='X' and tab[1][1]=='X' and tab[2][2]=='X') or (tab[0][2]=='X' and tab[1][1]=='X' and tab[2][0]=='X'):
       return 'X'
   elif (tab[0][0]=='O' and tab[1][1]=='O' and tab[2][2]=='O') or (tab[0][2]=='O' and tab[1][1]=='O' and tab[2][0]=='O'):
       return 'O'
  
   return '-' # #to be modified so that it returns the winner, or '-' if there is no winner
  
  
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
       # Iterating over columns
       for ch in lst:
           # Checking for -
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
   print(" ", end="")
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

def play (tab, player):
   '''
   (list, str) -> None
   Play a step of the game
   Preconditions: tab is a reference to the n x n tab containing '-', 'X' and 'O'
   The player is either X or O
   tab is modified (an element has changed)
   '''
  
   valid = False
   while not valid:
       place = [-1,-1] # create a table with two elements
       while not((0 <= place[0] < len(tab)) and (0 <= place[1] < len(tab))):
           print ("player ",player, end="")
           print(", Provide the row and column from 0 to", (len(tab)-1), ": ")
           place[0] = int(input("Row: ")) #
           place[1] = int(input("Column: "))
           #find a position that is not busy and contains '-‘
           if tab[place[0]][place[1]] != '-':
               print("the position", place[0], place[1], "is busy")
               valid = False
           else:
               valid = True
               # put the player in the array
               tab[place[0]][place[1]] = player
      
      
# Create the game table
table = [['-','-','-'],['-','-','-'],['-','-','-']] # the only array used in the program.
  
response = input("Start a game (O or N): ");
while response == 'o' or response == 'O':
   eraseTable(table) # prepare the game table
   winner = False # initialize winner variable
   while not winner:
       displayTable(table) # display the game table
       play(table,'X') # ask the player X to play
       winner = verifyWinner(table) # did he win?
       if not winner:
           # no winner, the other player can play
           displayTable(table) # dplay the game table
           play(table,'O') # ask the player O to play
           winner = verifyWinner(table) # did he win?
      
   displayTable(table) # display the game table
   response = input("Start a game (O or N): ") # new game?


