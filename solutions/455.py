from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two Pointer with sort
    Time Complexity: O(mlog(2, m) + nlog(2, n)) = mlog(2, m) + nlog(2, n) + m + n
    Space Complexity: O(m + n)
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
            j += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findContentChildren",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):

    assert solution(g=[1, 2, 3], s=[1, 1]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(g=[1, 2], s=[1, 2, 3]) == 2
