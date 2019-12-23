def eraseTable (tab):
   '''
   (list) -> None
   This function prepares the game table (array) 
   by putting '-' in all the elements.
   It does not create a new array
   Preconditions: tab is a reference to an nxn array matrice n x n that contains '-', 'X' or 'O'
   '''
   
    # to complete
    
    # returns nothing

      
def verifyWin(tab):  
    '''(list) ->  bool
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

    # to complete
   
    return False  # to change

 
def testRows(tab):
   ''' (list) ->  str
   * verify if there is a winning row.
   * Look for three 'X' or three 'O' in a row.  
   * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''

   # to complete
  
   return '-' # to be modified so that it returns the winner, or '-' if there is no winner 

  
  
def testCols(tab):
   ''' (list) ->  str
   * verify a winning column.
   * look for three 'X' or three 'O' in a column.  
   * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
    
   # to complete
  
   return '-'   #to be modified so that it returns the winner, or '-' if there is no winner

   
def testDiags(tab):
   ''' (list) ->  str
   * Look for three 'X' or three 'O' in a diagonal.  
   * If it is the case, the character 'X' or 'O' is returned
   * otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''

   # to complete
    
   return '-'   # #to be modified so that it returns the winner, or '-' if there is no winner

  
  
def testDraw(tab):
   ''' (list) ->  bool
   * verify if there is a draw
   * check if all the array elements have X or O, not '-'.  
   * If we do not find find any '-' in the array, return True. 
   * If there is any '-', return false.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
    
   # to complete
  
   return False  # to BE modiffied

