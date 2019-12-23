from a4q2Lib import *
    
def displayTable (tab):
    '''
    (list) -> None
    Display the game table
    Preconditions: tab is a reference to an n x n array that contains '-', 'X' or 'O'
    The format is: 
        0 1 2
      0 - - O
      1 - X -
      2 - - X
    '''
    print("   ", end="")
    col = 0
    while col < len(tab): 
      print(col, end="  ")
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
    Plays a step of the game
    Preconditions: tab is a reference to the n x n tab containing '-', 'X' and 'O'
    The player is X or O
    tab is modified (an elementis changed)
    '''               
    
    valid = False
                 
    while not valid:   
        place = [-1,-1] # create a table with two elements
        while not((0 <= place[0] < len(tab)) and (0 <= place[1] < len(tab))):
          print ("Player ",player, end="")
          print(", Please provide the row and the columm from 0 to", (len(tab)-1), ": ")
          place[0] = int(input("Row: ")) # 
          place[1] = int(input("Column: "))
        #find a position that is not busy that contains '-‘             
        if tab[place[0]][place[1]] != '-':
          print("The position", place[0], place[1], "is occupied");
          valid = False
        else:
          valid = True             
          # put the player in the array 
          tab[place[0]][place[1]] = player 
    # no result
  

# Create the game table 
table = [['-','-','-'],['-','-','-'],['-','-','-']] # The only array used in the program.
    
response = input("Start a game (O or N): ");    
while response == 'o' or response == 'O': 
      eraseTable(table)  # prepares the game table
      winner = False  # initializes the variable winner 
      while not winner: 
        displayTable(table) # display the game table
        play(table,'X')  # ask player X to play
        winner = verifyWin(table)  # Did he win?
        if not winner: 
          # no winner, the other player can play
          displayTable(table) # display the game table
          play(table,'O')  # ask player O to play
          winner = verifyWin(table)  # Did he win?
          
      displayTable(table) # display the game table
      response = input("Start a game (O or N): ") # new game?
