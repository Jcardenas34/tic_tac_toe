#!/usr/bin/ python3

'''
Description:
---------------
Defines a tic tac toe class, where the 

'''


# Diagonal  win x
board_1 = [["o","o","x"], 
           ["x","x","o"], 
           ["x","o","o"]]

# Row win x
board_2 = [["o","x","o"],
           ["x","x","x"], 
           ["o","o","x"]]

# Column win o
board_3 = [["o","x","o"], 
           ["o","o","x"], 
           ["o","x","o"]]

# Draw
board_4 = [["x","x","o"], 
           ["o","o","x"], 
           ["x","x","o"]]


# Ongoing game
board_5 = [["o","x","o"], 
           [None, None, None], 
           ["o","x","o"]]



# Defining an array of games to loop over for testing           
games = [board_1]
# games = [board_1, board_2, board_3, board_4, board_5]


class State:
    """State of the tic-tac-toe board."""

    def __init__(self, board):
        # You can define the structure for the board however you like
        self.board = board

        pass



    def score(self) -> int | None:
        """Return the result of the state.
        If the game is not over, return None. Otherwise, return 1 for a victory
        for the 'x' player, -1 for a victory for the 'o' player, and 0 for a
        draw.
        """
        board = self.board

        # Defining cases where x and o can wim
        o_win = ["o","o","o"]
        x_win = ["x","x","x"]
        

        # Row win
        for row in board:
            if row == x_win:
                return (1,"Row win")
            if row == o_win:
                return (-1,"Row win")


        # Column win
        for column in range(3):

            tracker = []   
            for row in board: # (Bug fix)
            # for row[column] in board: # (Original code, problem: here 'row[column]' is weird syntax to  it recursively 
                print(row[column])
                tracker.append(row[column])

            if tracker == o_win:
                return (-1, "Column win")
            if tracker == x_win:
                return (1, "Column win")


        # Counter diagonal elements 
        diag_1_elements = [board[0][2], board[1][1], board[2][0]]   

        # Diagonal elements (matching indicies)
        diag_2_elements = [board[0][0], board[1][1], board[2][2]]  
        
            
        # if either diagonal is all o
        if diag_1_elements == o_win or diag_2_elements == o_win:
            return (-1,"Diagonal win")


        # if either diagonal is all x
        if diag_1_elements == x_win or diag_2_elements == x_win:
            return (1,"Diagonal win")


        # Draw can take place if all spaces have an x or an o but no one has won
        for row in board:
            for col in row:
                if col == None:
                    return (None, "Game In progress")


        # Have exhausted all possibilities, game is a draw
        return (0,"Draw")




# Testing the games
for game in games:
    match_1 = State(game)


    if match_1.score()[0] == 1:
        print("x win: {}".format(match_1.score()[1]))
    elif match_1.score()[0] == -1:
        print("o win: {}".format(match_1.score()[1]))
    elif match_1.score()[0] == 0:
        print("Draw!")
    else:
        print("Game in progress")

