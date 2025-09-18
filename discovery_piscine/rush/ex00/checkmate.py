def find_king(board):
    """Finds the coordinates of the King 'K' on the board."""
    for r_idx, row in enumerate(board):
        for c_idx, char in enumerate(row):
            if char == "K":
                return (r_idx, c_idx)
    return None


def check_pawn(board, k_pos):
    """Checks for attacks from Pawns ('P')."""
    k_r, k_c = k_pos

    r1, c1 = k_r + 1, k_c - 1
    if 0 <= r1 < len(board) and 0 <= c1 < len(board[r1]) and board[r1][c1] == "P":
        return True

    r2, c2 = k_r + 1, k_c + 1
    if 0 <= r2 < len(board) and 0 <= c2 < len(board[r2]) and board[r2][c2] == "P":
        return True

    return False


def check_line(board, k_pos, direction):
    """
    Checks for attacks from Rooks, Bishops, or Queens in a straight line.
    direction is a tuple (dr, dc) representing the line's direction.
    """
    k_r, k_c = k_pos
    dr, dc = direction

    r, c = k_r + dr, k_c + dc
    while 0 <= r < len(board) and 0 <= c < len(board[r]):
        piece = board[r][c]
        if piece != ".":
            if (dr == 0 or dc == 0) and (piece == "R" or piece == "Q"):
                return True
            if (dr != 0 and dc != 0) and (piece == "B" or piece == "Q"):
                return True
            return False
        r, c = r + dr, c + dc
    return False


def checkmate(board):
    """
    Determines if the King 'K' on the board is in check.
    Prints 'Success' if the King is in check, otherwise prints 'Fail'.
    """
    if isinstance(board, str):
        board = [line for line in board.splitlines() if line]

    if not board or not any("K" in row for row in board):
        print("Fail")
        return

    king_pos = find_king(board)
    if king_pos is None:
        print("Fail")
        return

    if check_pawn(board, king_pos):
        print("Success")
        return

    directions = [
        (-1, 0),  # บน
        (1, 0),  # ล่าง
        (0, -1),  # ซ้าย
        (0, 1),  # ขวา
        (-1, -1),  # บนซ้าย
        (-1, 1),  # บนขวา
        (1, -1),  # ล่างซ้าย
        (1, 1),  # ล่างขวา
    ]

    for dr, dc in directions:
        if check_line(board, king_pos, (dr, dc)):
            print("Success")  # In Check
            return

    # Safe
    print("Fail")
