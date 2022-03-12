from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mat_sum = 0 if n % 2 == 0 else -mat[n // 2][n // 2]
        for y in range(n):
            mat_sum += mat[y][y] + mat[y][n - 1 - y]
        return mat_sum


def test_1():
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert Solution().diagonalSum(mat) == 25


def test_2():
    mat = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]
    assert Solution().diagonalSum(mat) == 8
