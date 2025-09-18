from checkmate import checkmate


def main():
    """
    Defines sample chessboards and tests the checkmate function.
    """
    # Example 1
    board = """\
R...
.K..
..P.
....\
"""
    print("Example 1:")
    checkmate(board)

    print()
    # Example 2
    board = """\
..
.K\
"""
    print("Example 2:")
    checkmate(board)


if __name__ == "__main__":
    main()
