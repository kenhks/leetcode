import itertools
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Check row, col, grid
    n = len(board)
    Time Complexity: O(3n)
    Space Complexity: O(3n^2)
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_group(arrays):
            checked = set()
            for x in arrays:
                if x == ".":
                    continue
                elif x in checked:
                    return False
                else:
                    checked.add(x)
            return True

        for row in board:
            if not check_group(row):
                return False
        for col in zip(*board):
            if not check_group(col):
                return False
        for y in range(0, 9, 3):
            rows = board[y : y + 3]
            for x in range(0, 9, 3):
                grid = itertools.chain(*[i[x : x + 3] for i in rows])
                if not check_group(grid):
                    return False
        return True


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isValidSudoku",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solution(board)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert not solution(board)
