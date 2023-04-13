def solve(puzzle, coloums, rows, boxes):
    """Solves a Sudoku puzzle.

    Args:
        puzzle (list): A list of lists representing the puzzle.
        coloums (set): A set of tuples representing the coloums.
        rows (set): A set of tuples representing the rows.
        boxes (set): A set of tuples representing the boxes.

    Returns:
        list: A list of lists representing the solved puzzle.
    """
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for k in range(1, 10):
                    if (j, k) not in coloums and (i, k) not in rows and (i//3, j//3, k) not in boxes:
                        puzzle[i][j] = k
                        coloums.add((j, k))
                        rows.add((i, k))
                        boxes.add((i//3, j//3, k))
                        if solve(puzzle, coloums, rows, boxes):
                            return puzzle
                        else:
                            puzzle[i][j] = 0
                            coloums.remove((j, k))
                            rows.remove((i, k))
                            boxes.remove((i//3, j//3, k))
                return False
    return puzzle

def sudoku_solver(puzzle):
    """Solves a Sudoku puzzle.

    Args:
        puzzle (list): A list of lists representing the puzzle.

    Returns:
        list: A list of lists representing the solved puzzle.
    """
    coloums = set()
    rows = set()
    boxes = set()
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                coloums.add((j, puzzle[i][j]))
                rows.add((i, puzzle[i][j]))
                boxes.add((i//3, j//3, puzzle[i][j]))
    return solve(puzzle, coloums, rows, boxes)


puzzle = [[ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
          [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
          [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
          [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
          [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
          [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
          [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
          [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
          [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ] 
]

print(sudoku_solver(puzzle))
