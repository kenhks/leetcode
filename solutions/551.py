import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with two count
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def checkRecord(self, s: str) -> bool:
        L_count, late = 0, False
        A_count = 0
        for r in s:
            if r != "L":
                if r == "A":
                    A_count += 1
                L_count = 0
            else:
                L_count += 1
                if L_count == 3:
                    late = True
                    break
        if A_count < 2 and not late:
            return True
        else:
            return False


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "checkRecord",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="PPALLP")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(s="PPALLL")
