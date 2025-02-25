import sys

class Tetris:
    def __init__(self, width=10):

        """
        Functon intialization.

        Parameters:
        self.width (int) : The width of the occupancy grid (Default value 10).
        self.height (int) : The maximum height of the occupany grid (10e^7)
        self.col_height (list) : The next available space in each column of the grid.
        self.grid (list) : The occupancy grid space where '0' represents empty space and '1' represents occupied space.
        self.piece_shapes (dict) : The mapping of piece name to its dimensions with respect to row and column (Mentioned in drop_piece funcition).

        """

        self.width = width
        self.height = 10000000 # for visualization of the given examples, use height of 15.
        self.col_heights = [0]*width
        self.grid = [[0] * width for _ in range(self.height)]

        self.piece_shapes = {
            'Q': [(0, 0), (0, 1), (1, 0), (1, 1)],    # Q or Square Shape
            'Z': [(1, 0), (1, 1), (0, 1), (0, 2)],    # Z shape
            'S': [(0, 0), (0, 1), (1, 1), (1, 2)],    # S shape
            'T': [(0, 0), (0, 1), (0, 2), (-1, 1)],   # T shape
            'I': [(0, 0), (0, 1), (0, 2), (0, 3)],    # I shape
            'L': [(0, 0), (1, 0), (2, 0), (0, 1)],    # L shape
            'J': [(0, 0), (0, 1), (1, 1), (2, 1)]     # J shape
        }

    
    def drop_piece(self, piece, column): 
        """
        To fill each piece in the occupancy grid.

        This function drops each piece in the grid. 
        The pieces occupying the grid are represented as ones and the empty spaces are represented as zeroes
        
        Parameters:
        piece (str) : The type of piece, i.e. Q,L,J,Z,S,T or I.
        column (int) : The column along which the piece should fall.
        row (int) : The row at the which the piece can occupy in the grid.

        Returns:
        y_max (int) : The maximum height of occupied space in the overall grid after dropping a single piece.

        Raises:
        ValueError : If is some part of piece is outside the grid

        """

        row = 0 
        y_max = 0

        # Check two column's height
        if piece == 'Q':
            row = max(self.col_heights[column], self.col_heights[column+1])
        elif piece == 'L':
            row = max(self.col_heights[column], self.col_heights[column+1])
        elif piece == 'J':
            row = max(self.col_heights[column], self.col_heights[column+1])

        # Check three column's height
        elif piece == 'Z':
            row = max(self.col_heights[column]-1, self.col_heights[column+1], self.col_heights[column+2])
        elif piece == 'S':
            row = max(self.col_heights[column], self.col_heights[column+1], self.col_heights[column+2]-1)
        elif piece == 'T':
            row = max(self.col_heights[column],  self.col_heights[column+1]+1, self.col_heights[column+2])

        # Check four column's height
        elif piece == 'I':
            row = max(self.col_heights[column], self.col_heights[column+1], self.col_heights[column+2], self.col_heights[column+3])

        
        # Fill each grid with 1 based on the shape of piece and update y_max and self.col_heights
        for dy, dx in self.piece_shapes[piece]:
            x = column + dx
            y = row + dy    

            if x < 0 or x > self.width-1 or y<0 or y>self.height:
                raise ValueError("Piece cannot be added as some part of it is outside the grid.")
            
            self.grid[y][x] = 1
            self.col_heights[x] = max(self.col_heights[x], y+1) 
            y_max = max(y_max,y)

        return y_max
    

    def check_full_rows(self, y_max):
        """
        To delete the row that is completely filled.

        This function checks if any row in the grid is completely occupied and removes it from the grid.
        Additionally the function also updates self.col_heights if any rows are removed from the grid.

        Parameters:
        count (int) : The total number of rows deleted from the grid.

        """
        count = 0

        # Find if any row is completely filled along the width, count the no. of rows removed and then delete the rows.
        for r in range(y_max,-1,-1):
            if sum(self.grid[r]) == self.width:
                # print(f"Removed row {r}")
                count += 1
                del self.grid[r]

        # Update the self.col_heights based on the new grid (update done in column wise fashion).
        if count != 0:
            for i  in range(self.width):
                j = self.col_heights[i] - count 
                
                while self.grid[j][i] == 0 and j >= 0 :
                    j -= 1
                self.col_heights[i] = j + 1  


    def visualize(self, move):
        """
        To Visualize the pieces dropped in the grid.

        This function is OPTIONAL to run and is just to visualize each move in the grid.
        The occupied spaces of the grid is represented by '1' and empty spaces are represented as '0'

        Parameters:
        move (str) : Each instruction in each line (e.g. 'Q4') . 

        """
        self.height = 15 # Subject to change based on test case.

        print(f"move : {move}")
        for row in self.grid:
            print(row)
        print()
        print(self.col_heights)
        print()     


    def process_line(self, line):

        """
        To process each line in the input.txt

        Parameters:
        line (str) : A string which contains comma seperated values in input.txt (e.g. 'Z2,S3,I0,I4').
        moves (list) : A list that contains the moves for each line (e.g. ['Q2','Q4','T5] ). 
        piece (str) : The type of piece, i.e. Q,L,J,Z,S,T or I.
        column (int) : The column along which the piece should fall.

        Returns:
        height : The maximum height of the occuppied space after dropping all pieces.

        Raises:
        ValueError : If piece apart from Q,S,Z,T,L and J are given in input.
        ValueError : If column excedes beyond the width of the grid.
        
        """
        moves = line.strip().split(',')

        for move in moves:
            piece = move[0]
            column = int(move[1])
            # print(f"move {move}")

            if piece not in self.piece_shapes:
                raise ValueError("Piece not avaibale.")
            if column < 0 or column > self.width-1:
                raise ValueError("Input column value is outside the grid.")

            y_max = self.drop_piece(piece, column)
            self.check_full_rows(y_max)
        
    # For Visualizing un-comment the following lines
    # *************************************************
    #         self.visualize(move)
    #     print('*'*30)
    #     print("\n")
    # # *************************************************
            

        height = max(self.col_heights) 

        # Initialize self.col_heights and self.grid to zeroes for processing next line.
        self.col_heights = [0]*self.width
        self.grid = [[0] * self.width for _ in range(self.height)]

        return height 
    
    

def main():
    tetris = Tetris()
    input_file = sys.stdin.read().strip().split('\n')
    results = [str(tetris.process_line(line)) for line in input_file]
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    main()


