# Tetris Game Engine

## Description

Tetris class in tetris.py contains following functions: 

- `drop_piece`: To fill each piece in the occupancy grid.
- `check_full_rows`: To delete the row that is completely filled.
- `visualize`: (optional) To Visualize the pieces dropped in the grid.
- `process_line`: To process each line in the input.txt .

Each function and the respective parameters are explained under the function defination in tetris.py .

## Instruction

1. Create a conda environment (shell script):
    conda create --name tetris python=3.9

2. Activate the environment (shell script):
    conda activate tetris

3. Create an input.txt:
    create an input.txt with the pattern for block to be drop chronologically

4. Run the tetris.py file (shell script):
    cd your-repo
    python tetris.py < input.txt > output.txt

5. Visualize the grid (optional):
    comment out line 180 to 182 in tetris.py and see the grid in output.txt
   
Note : 
- The grid structure used in the code is not as same as the conventional tetris game.
- The grid used in the code is flipped (about x or horizontal axis) version of the original one.
          
    
