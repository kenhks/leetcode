from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)
        ans = []
        for c in s:
            if c == "I":
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        ans.append(left)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "diStringMatch",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="IDID") == [0, 4, 1, 3, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="III") == [0, 1, 2, 3]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="DDI") == [3, 2, 0, 1]
