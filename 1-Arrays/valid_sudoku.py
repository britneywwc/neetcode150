import collections


def isValidSudoku(board) -> bool:
    """
    Sudoku board: 9x9
    Checking if an entry is valid:
    - Dict for rows (each row is key, value: 1-9 with no duplicates)
    - Dict for cols (each col is key, value: 1-9 with no duplicates)
    - Dict for boxes (key: box coord in tuple, value: 1-9 with no duplicates)
        > 9 total boxes, divide them up by boxes and add to boxes if already present
        > Row//3 and Col//3 to get the box key (0, 0) to (2, 2)
    """
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    boxes = collections.defaultdict(set)

    for i in range(9):
        for j in range(9):
            cell = board[i][j]

            if cell == ".":
                continue

            if (cell in rows[i] or
                cell in cols[j] or
                cell in boxes[i // 3, j // 3]):
                return False

            cols[j].add(board[i][j])
            rows[i].add(board[i][j])
            boxes[(i//3, j//3)].add(board[i][j])

            print("Rows", rows)
            print("Cols", cols)
            print("Boxes", boxes, '\n')
    return True


board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
