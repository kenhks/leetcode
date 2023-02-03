import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Direct
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        cur_row = 0
        diff = 1
        for c in s:
            rows[cur_row].append(c)
            if cur_row == numRows - 1:
                diff = -1
            elif cur_row == 0:
                diff = 1
            cur_row += diff
        return "".join(["".join(row) for row in rows])


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "convert",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="PAYPALISHIRING", numRows=3) == "PAHNAPLSIIGYIR"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="PAYPALISHIRING", numRows=4) == "PINALSIGYAHRPI"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="A", numRows=1) == "A"
