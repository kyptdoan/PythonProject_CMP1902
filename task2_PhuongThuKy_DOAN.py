import time, random

class Game():
    """
    Class "Game" manages the flow of the game
    ...
    Attributes:
        board: class
            the board used in the game
        current_turn: int
            player's turn index
        points: list
            a list contains each player's number of special disc
    ...
    Methods:
        is_game_over(): check if the game is over
        calculate_points(game_type, player_id): calculate points for each player 
        use_special_disc(special_disc_row, special_disc_col): delete adjacent cells for a move with special disc
        PopOut_execution(selected_col): pop the bottom disc in the selected column when PopOut is played.
        find_the_winner(): find the winner by comparing their points.
        control(): control the flow of the game
        validate_obstacle_size(): validate the input for obstacle size (row, column)
        validate_game_type(): validate the input for game type
        validate_move_type(): validate the input for move type
    """

    def __init__(self):
        """
        Contructs all the necessary attributes for the game object
        """
        self.board = Board()
        self.current_turn = 1
        self.points = [0, 0]
    
    def is_game_over(self):
        """
        Checks if the game is over by checking if the board is full
        Returns:
            bool: True if the game is over (the board is full), False if not
        """
        # Loop through each row and col of the board
        for row in range (self.board.row_num):
            for col in range (self.board.col_num):
                # If there is an empty cell, the game is not over
                if (self.board.board[row][col] == ' '):
                    return False
        # If there is no empty cell, the game is over
        return True
    
    def calculate_points(self, game_type, player_id):
        """
        Calculate points for each player 

        Args:
            game_type (int): the type of game chosen by players
            player_id (int): player's id used as disc's symbol in the board

        Returns:
            int: the points of a player after their turn
        """
        
        # Intitial point
        temp_points = 0
        
        # Calculate points for Connect 3
        if (game_type == 3):
            
            # Check horizontally
            # Loop through each row
            for row in range (self.board.row_num):
                # In each row, loop through each column to form the cells coordinate
                for col in range (self.board.col_num-2):
                    # Check if there is any 3-connection in a row
                    if (self.board.board[row][col] == player_id and self.board.board[row][col+1] == player_id and self.board.board[row][col+2] == player_id):
                        # If yes, the player scores a point
                        temp_points += 1
        
            # Check vertically
            # Loop through each row in range (0, 4)
            for row in range (self.board.row_num-2):
                # In each row, loop through each column to form the cells coordinate
                for col in range (self.board.col_num):
                    # Check if there is any 3-connection in a column
                    if (self.board.board[row][col] == player_id and self.board.board[row+1][col] == player_id and self.board.board[row+2][col] == player_id):
                        # If yes, the player scores a point
                        temp_points += 1
            
            # Check negative diagonals
            # Loop through each column in range (0, 5)
            for col in range (self.board.col_num-2):
                # In each column, loop through each row in range (2, 6)
                for row in range (2, self.board.row_num):
                    # Check if there is any 3-connection in a negative diagonal
                    if (self.board.board[row][col] == player_id and self.board.board[row-1][col+1] == player_id and self.board.board[row-2][col+2] == player_id):
                        # If yes, the player scores a point
                        temp_points += 1

            # Check positive diagonals
            # Loop through each column in range (0, 5)
            for col in range (self.board.col_num-2):
                # In each column, loop through each row in range (0, 4)
                for row in range (self.board.row_num-2):
                    # Check if there is any 3-connection in a positive diagonal
                    if (self.board.board[row][col] == player_id and self.board.board[row+1][col+1] == player_id and self.board.board[row+2][col+2] == player_id):
                        # If yes, the player scores a point
                        temp_points += 1
   
        # Calculate points for Connect 4
        elif (game_type == 4):
            # Same idea as for Connect 3
            
            # Check horizontally
            for row in range (self.board.row_num):
                for col in range (self.board.col_num-3):
                    # Check if there is any 4-connection in a row
                    if (self.board.board[row][col] == player_id and self.board.board[row][col+1] == player_id and self.board.board[row][col+2] == player_id and self.board.board[row][col+3] == player_id):
                        temp_points += 1

            # Check vertically
            for row in range (self.board.row_num-3):
                for col in range (self.board.col_num):
                    # Check if there is any 4-connection in a column
                    if (self.board.board[row][col] == player_id and self.board.board[row+1][col] == player_id and self.board.board[row+2][col] == player_id and self.board.board[row+3][col] == player_id):
                        temp_points += 1
                        
            # Check negative diagonals
            for col in range (self.board.col_num-3):
                for row in range (3, self.board.row_num):
                    # Check if there is any 4-connection in a negative diagonal
                    if (self.board.board[row][col] == player_id and self.board.board[row-1][col+1] == player_id and self.board.board[row-2][col+2] == player_id and self.board.board[row-3][col+3] == player_id):
                        temp_points += 1
            
            # Check positive diaganols
            for col in range (self.board.col_num-3):
                for row in range (self.board.row_num-3):
                    # Check if there is any 4-connection in a positive diagonal
                    if (self.board.board[row][col] == player_id and self.board.board[row+1][col+1] == player_id and self.board.board[row+2][col+2] == player_id and self.board.board[row+3][col+3] == player_id):
                        temp_points += 1
        
        # Calculate points for Connect 5
        elif (game_type == 5):
            # Same idea as for Connect 3 and Connect 4
            
            # Check horizontally
            for row in range (self.board.row_num):
                for col in range (0,self.board.col_num-4):
                    # Check if there is any 5-connection in a row
                    if (self.board.board[row][col] == player_id and self.board.board[row][col+1] == player_id and self.board.board[row][col+2] == player_id and self.board.board[row][col+3] == player_id and self.board.board[row][col+4] == player_id):
                        temp_points += 1
            
            # Check vertically
            for row in range (self.board.row_num-4):
                for col in range (self.board.col_num):
                    # Check if there is any 5-connection in a column
                    if (self.board.board[row][col] == player_id and self.board.board[row+1][col] == player_id and self.board.board[row+2][col] == player_id and self.board.board[row+3][col] == player_id and self.board.board[row+4][col] == player_id):
                        temp_points += 1
            
            # Check negative diaganols
            for col in range (self.board.col_num-4):
                for row in range (4, self.board.row_num):
                    # Check if there is any 5-connection in a negative diagonal
                    if (self.board.board[row][col] == player_id and self.board.board[row-1][col+1] == player_id and self.board.board[row-2][col+2] == player_id and self.board.board[row-3][col+3] == player_id and self.board.board[row-4][col+4] == player_id):
                        temp_points += 1
            
            # Check positive diaganols
            for col in range (self.board.col_num-4):
                for row in range (self.board.row_num-4):
                    # Check if there is any 5-connection in a positive diagonal
                    if (self.board.board[row][col] == player_id and self.board.board[row+1][col+1] == player_id and self.board.board[row+2][col+2] == player_id and self.board.board[row+3][col+3] == player_id and self.board.board[row+4][col+4] == player_id):
                        temp_points += 1
        
        # Save the points corresponding to the player into the points list
        self.points[player_id-1] = temp_points
    
        return self.points[player_id-1]
    
    def use_special_disc(self, special_disc_row, special_disc_col):
        """
        Delete adjacent discs of a special disc when it is placed

        Args:
            special_disc_row (int): the row of special disc in the board
            special_disc_col (int): the column special disc in the board

        Returns:
            list: the state of the board after deleting adjacent discs and the special disc itself
        """
        
        # a list contain operations for left, right, down, upleft, upright, downleft, downright
        direction = [(0,-1), (0,1), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
        
        # Loop through each direction
        for row, col in direction:
            # Calculate the coordinates of the adjacent cell
            deleted_row = special_disc_row + row
            deleted_col = special_disc_col + col
            
            # Check if the row and column of the adjacent cell exceed the board size
            if (deleted_row >= 0 and deleted_row <= 5):
                if (deleted_col >= 0 and deleted_col <= 6):
                    # Check if the adjacent cell is an obstacle
                    if (self.board.board[deleted_row][deleted_col] != 'o'):
                        self.board.board[deleted_row][deleted_col] = ' '

        # Remove the special disc
        self.board.board[special_disc_row][special_disc_col] = ' '
        
        return self.board.board
    
    def PopOut_execution(self, selected_col):
        """
        Pop the bottom disc in the selected column when PopOut is played.
        Validation for the player's disc is done in method "Control".
        Args:
            selected_col (int): the selected column
        """
        self.board.board[5][selected_col] = ' '

    def find_the_winner(self):
        """
        Find the winner by comparing their points.
        """
        # Compare 2 player's points and announce the winner.
        if (self.points[0] > self.points[1]):
            print("Player 1 wins.")
        elif (self.points[0] < self.points[1]):
            print("Player 2 wins.")
        else:
            print("Tie.")            
    
    def control(self):
        """
        Control the flow of the game including:
            Take player's input for game type/obstacle size/move type/column
            Manage the turn index, calculate time for each turn
            Update the board, points
            Announce winner
        """
        
        # Initial turn index in the beginning
        current_turn = 1
        
        # A list contains each player's number of special disc in the beginning
        number_of_special_disc = [1, 1]
        
        # Keep prompting players until they input a valid game type
        while (True):
            # Erroneous input handling when the input for game type is not an integer
            while (True):
                try:
                    game_type = int(input("Choose game type. Press 3 for Connect 3, 4 for Connect 4, 5 for Connect 5: "))
                    break
                except ValueError:
                    print("Please input an integer (3 for Connect 3 / 4 for Connect 4 / 5 for Connect 5")
            
            # Exception handling for game type
            try:
                self.validate_game_type(game_type)
                break
            except InvalidIntegerError as e:
                print(e)

        # Keep prompting players until they input a valid row and a valid column for obstacle
        while (True):
            
            # a list contains the size (row, column) of the obstacle
            obstacle_size = []
            
            # Erroneous input handling when the inputs for obstacle size are not integers
            while (True):
                try:
                    obstacle_row = int(input("Input the number of rows for the obstacle: "))
                    obstacle_col = int(input("Input the number of columns for the obstacle: "))
                    break
                except ValueError:
                    print("Please input integers only for obstacle size.")
            
            # Exception handling when player's chosen obstacle size exceeds the board size        
            try:
                self.validate_obstacle_size(obstacle_row, obstacle_col)
                break
            except InvalidIntegerError as e:
                print(e)
        
        # Save the obstacle size (row, column) into obstacle_size list    
        obstacle_size.append(obstacle_row)
        obstacle_size.append(obstacle_col)
        
        # Print the board with the chosen obstacle inside
        self.board.create_board(obstacle_size)
        
        # Prompting each player to make a move until the game is over
        while (True):
            
            # Update the board after each turn
            self.board.print_board()
            
            # Update the points after each turn
            print("Player 1 points: ", self.calculate_points(game_type, 1))
            print("Player 2 points: ", self.calculate_points(game_type, 2))
            
            # Whenever the game is not over, the player (index by the turn number)
            if (self.is_game_over() != True):
                
                print(f"Player {current_turn}. You have 5 seconds to make a move.")
                
                # Start the timer
                init_time = time.time()
                
                # Prompting the player until they choose a valid move type
                while (True):
                    
                    # Erroneous input handling when the player do not input an integer for move type
                    while (True):
                        try:
                            move_type = int(input(f"Player {current_turn}. Press 1 for standard move, 2 for special disc, 3 for PopOut: "))
                            break
                        except ValueError:
                            print("Please type in an integer (1 for Standard Move/ 2 for Special Disc/ 3 for PopOut)")
                            
                    # Exception handling when player types in an integer but it is not valid for move type
                    try:
                        self.validate_move_type(move_type)
                        break
                    except InvalidIntegerError as e:
                        print(e)
                    
                # Standard Movement is executed when the player press 1
                if (move_type == 1):
                    
                    # Prompting the player until they choose a valid column
                    while (True):
                        # Erroneous inpur handling when the player do not input an integer for column
                        while (True):
                            try:
                                selected_col = int(input(f"Player {current_turn}. Please choose a column (0 to 6) to drop your disc: "))
                                break
                            except ValueError:
                                print("Please input an integer between 0 and 6 to make a move.")
                        
                        # Exception handling when the player input a negative integer
                        if (selected_col < 0):
                            print("Please input an integer between 0 and 6 to make a move.")
                            continue
                        
                        # Exception handling when the player do not input a valid column number
                        try:
                            item = self.board.board[0][selected_col]
                            break
                        except IndexError:
                            print("Please input an integer between 0 and 6 to make a move.")    
                    
                    # Calculate the time they spent for a valid move                            
                    secs_elapsed_1 = time.time() - init_time
                    
                    # Check if they made a valid move in 5 seconds
                    if (secs_elapsed_1 <= 5):
                        
                        # Check if their selected column is available for a new disc
                        if (self.board.is_available_col(selected_col)):
                            # If the column is available, update the board with the new played disc
                            self.board.place_a_disc(selected_col, current_turn)
                            # Switch the turn index
                            current_turn = (current_turn % 2) + 1
                            # Switch to another player's turn
                            continue
                        # If the column is unavailable, announce them 
                        else:
                            print(f"Player {current_turn}. Your chosen columnn is full. You have lost your turn.")
                            current_turn = (current_turn % 2) + 1
                            continue
                    
                    # If they made move in more than 5 seconds, announce them and switch to another player's turn
                    else:
                        print(f"Player {current_turn}. Your time is up. You have lost your turn.")
                        current_turn = (current_turn % 2) + 1
                        continue
                    
                # Special Disc Movement is executed when the player press 2
                if (move_type == 2):
                    
                    # Update the number of their remained special disc
                    print(f"Player {current_turn}. You have {number_of_special_disc[current_turn-1]} special disc.")
                    
                    # If they have not used any special disc (have 1), they can drop it        
                    if (number_of_special_disc[current_turn-1] != 0):
                        
                        # Prompting the player until they make a valid choose for column
                        while (True):
                            # Erroneous input handling when the player do not input an integer to choose a column
                            while (True):
                                try:
                                    special_disc_col = int(input(f"Player {current_turn}. Please choose a column (0 to 6) to drop your special disc: "))
                                    break
                                except ValueError:
                                    print("Please input an integer between 0 and 6 to make a move.")

                            # Exception handling when the player input a negative integer to choose a column
                            if (special_disc_col < 0):
                                print("Please input an integer between 0 and 6 to make a move.")
                                continue
                            
                            # Exception handling when the player do not input a valid column number
                            try:
                                item = self.board.board[0][special_disc_col]
                                break
                            except IndexError:
                                print("Please input an integer between 0 and 6 to make a move.")
                        
                        # Calculate the time the player spent for a valid move
                        secs_elapsed_2 = time.time() - init_time
                        
                        # Check if they made a valid move in 5 seconds
                        if (secs_elapsed_2 <= 5):
                            # Check if the chosen column is available for a new disc
                            if (self.board.is_available_col(special_disc_col)):
                                
                                # Find special disc row using its selected column
                                for row in range (-1, -7, -1):
                                    if (self.board.board[row][special_disc_col] == ' '):
                                        special_disc_row = row + 6
                                        break
                                
                                # Place the special disc into the board
                                self.board.place_a_disc(special_disc_col, current_turn)
                                # Delete the adjacent disc
                                self.use_special_disc(special_disc_row, special_disc_col)
                                # Maintain the gravity in the board
                                self.board.maintain_the_gravity()
                                # Update the number of special disc
                                number_of_special_disc[current_turn-1] = number_of_special_disc[current_turn-1]-1
                                current_turn = (current_turn % 2) + 1
                                continue
                            
                            # If the selected column is full, announce and switch to another player's turn
                            else:
                                print("Player ", current_turn, "Your chosen column is full. You have lost your turn.")
                                current_turn = (current_turn % 2) + 1
                                continue
                        
                        # If the player made a valide move in more than 5 secs, switch to another player's turn
                        else:
                            print("Player ", current_turn, ". Your time is up. You have lost your turn.")
                            current_turn = (current_turn % 2) + 1
                            continue
                    
                    # If the player has used their special disc before, announce and switch to another player's turn
                    else:
                        print("Player ", current_turn,"You have used your special disc before. You have lost your turn.")
                        current_turn = (current_turn % 2) + 1
                        continue
            
                # PopOut Movement is executed when the player press 3
                if (move_type == 3):
                    
                    # Prompting the player until they input a valid integer for column
                    while (True):
                        while (True):
                            try:
                                selected_col = int(input(f"Player {current_turn}. Please choose a column (0 to 6): "))
                                break
                            except ValueError:
                                print("Please input an integer between 0 and 6 to make a move.")
                        
                        if (selected_col < 0):
                            print("Please input an integer between 0 and 6 to make a move.")
                            continue
                        
                        try:
                            item = self.board.board[0][selected_col]
                            break
                        except IndexError:
                            print("Please input an integer between 0 and 6 to make a move.")
                    
                    # Calculate the time they spent to make a valid move
                    secs_elapsed_3 = time.time() - init_time
                    
                    # Check if they made a valid move in 5 secs
                    if (secs_elapsed_3 <= 5):
                        # Check if there is a disc of current player at the bottom row of the selected column
                        if (self.board.board[5][selected_col] != current_turn):
                            print(f"Player {current_turn}. You don't have any disc to remove at this cell. You have lost your turn.")
                            current_turn = (current_turn % 2) + 1
                            continue
                        else:
                            self.PopOut_execution(selected_col)
                            self.board.maintain_the_gravity()
                            current_turn = (current_turn % 2) + 1
                            continue
                    else:
                        print(f"Player {current_turn}. Your time is up. You have lost your turn.")
                        current_turn = (current_turn % 2) + 1
                        continue
                        
            else:
                break
        
        # Find and announce the winner when the game is over
        self.find_the_winner()

    def validate_obstacle_size(self, obstacle_row, obstacle_col):
        """
        Validate the inputs for obstacle size (row, column)

        Args:
            obstacle_row (int): the obstacle's number of row 
            obstacle_col (int): the obsatcle's number of column

        Raises:
            InvalidIntegerError: if the inputs are negative, print the message
            InvalidIntegerError: if the inputs are equal to the board's number of row and column, print the message
            InvalidIntegerError: if the inputs exceed the board size, print the message
        """
        if (obstacle_row < 0 or obstacle_col < 0):
            raise InvalidIntegerError("Obstacle size must not be negative. Please input again.")
        if (obstacle_row == 6 and obstacle_col == 7):
            raise InvalidIntegerError("The board is totally filled with obstacle. Please input again.")
        if (obstacle_row > 6 or obstacle_col > 7):
            raise InvalidIntegerError("The obstacle is bigger than the board. Please input again.")
        
    def validate_game_type(self, game_type):
        """
        Validate the input for game type

        Args:
            game_type (int): player's input to choose favorite game type

        Raises:
            InvalidIntegerError: when the input is not 3/4/5, print the message
        """
        if (game_type not in [3, 4, 5]):
            raise InvalidIntegerError("We only offer Connect 3, Connect 4 and Connect 5.")
    
    def validate_move_type(self, move_type):
        """
        Validate the input for move type
        
        Args:
            move_type (int): player's input to choose move type

        Raises:
            InvalidIntegerError: when the input is not 1/2/3, print the message
        """
        if (move_type not in [1, 2, 3]):
            raise InvalidIntegerError("Please type 1 for Standard Move/ 2 for Special Disc/ 3 for PopOut")
                                                
class Board():
    """
    Class "Board" represents the board in the game
    ...
    Attributes:
        board: list
            an empty board with 6 rows and 7 columns
        row_num: int
            the number of the board's row (which is 6)
        col_num: int
            the number of the board's column (which is 7)
    ...
    Methods:
        create_board(obstacle_size): create the initial board with chosen obstacle
        is_available_col(selected_col): check if the selected column is available for a new disc
        place_a_disc(selected_col, player_id): update the board with a new disc being placed inside
        maintain_the_gravity(): Update the board with no empty cell between any 2 discs in the same column
        print_board(): print the board with required format
    """
    def __init__(self):
        """
        Constructs all the necessary attribute for a board object
        """
        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.row_num = 6
        self.col_num = 7
        
    def create_board(self, obstacle_size):
        """
        Create the board with obstacle

        Args:
            obstacle_size (list): a list contains the number of row and columns of the obstacle

        Returns:
            list: the board with chosen obstacle
        """
        
        # Randomly place the obstacle at the bottom
        temp = random.randint(0, self.col_num-obstacle_size[1])
        obstacle_position = temp

        for obstacle_row in range (self.row_num-obstacle_size[0], self.row_num):
            for obstacle_col in range (obstacle_position, obstacle_position + obstacle_size[1]):
                self.board[obstacle_row][obstacle_col] = 'o'
        return self.board
    
    def is_available_col(self, selected_col):
        """
        Check if the selected column is still available for a new disc to be dropped in

        Args:
            selected_col (int): the player's selected column

        Returns:
            bool: True if the selected column is still available, False if not
        """
        for row in self.board:
            if (row[selected_col] == ' '):
                return True
        return False
    
    def place_a_disc(self, selected_col, player_id):
        """
        Place a new disc in the most bottom empty row of the selected row

        Args:
            selected_col (int): player's selected column 
            player_id (int): the current player's id is the symbol of the disc
        """
        for row in range (-1, -7, -1):
            if (self.board[row][selected_col] == ' '):
                self.board[row][selected_col] = player_id
                break
                
    def maintain_the_gravity(self):
        """
        Update the board with no empty cell between any 2 discs in the same column

        Returns:
            list: return the board after updating
        """
        # A stack to contain the disc in the column
        disc_container = []
        
        # Loop through each column and row to find discs
        for col in range (self.col_num):
            for row in range (self.row_num):
                # If a disc is found, push it in the stack and delete it out of the board
                if (self.board[row][col] != ' ' and self.board[row][col] != 'o'):
                    disc_container.append(self.board[row][col])
                    self.board[row][col] = ' '
            
            # Save the length of the stack when it contains all the disc in a column
            initial_length = len(disc_container)
            
            # Find the most bottom empty row in a column to be the starting row
            for row in range (-1, -7, -1):
                if (self.board[row][col] != 'o'):
                    starting_row = row
                    break
            
            # Loop through the row down-to-up from the starting row to place the discs back into the column
            for row in range (starting_row, starting_row-initial_length, -1):
                # Pop a disc out the stack
                disc = disc_container.pop()
                # Place a disc back to the board
                self.board[row][col] = disc
        return self.board
        
    def print_board(self):
        """
        Print the board with required format
        """
        for row in self.board:
            print("|", end="")
            for cell in row:
                print(cell, end="|")
            print()
        print("---------------")
        print(" 0 1 2 3 4 5 6 ")

class InvalidIntegerError(Exception):
    """
    Custom exception class for when the player inputs an integer but it is not valid
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

if __name__ == "__main__":
    game = Game()
    game.control()
            

