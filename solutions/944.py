from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(mn)
    Space Complexity: O(1)
    """

    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            prev = col[0]
            sort = True
            for x in col[1:]:
                if ord(x) < ord(prev):
                    sort = False
                    break
                prev = x
            if not sort:
                ans += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minDeletionSize",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(strs=["cba", "daf", "ghi"]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(strs=["a", "b"]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(strs=["zyx", "wvu", "tsr"]) == 3
