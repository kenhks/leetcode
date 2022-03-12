from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        row = []
        new_mat = []
        for i in range(m):
            for j in range(n):
                if len(row) < c:
                    print("append")
                    row.append(mat[i][j])
                if len(row) == c:
                    new_mat.append(row)
                    row = []
        return new_mat


def test_1():
    mat = [
        [1, 2],
        [3, 4],
    ]
    assert Solution().matrixReshape(mat, r=1, c=4) == [[1, 2, 3, 4]]


def test_2():
    mat = [
        [1, 2],
        [3, 4],
    ]
    assert Solution().matrixReshape(mat, r=2, c=4) == [[1, 2], [3, 4]]
