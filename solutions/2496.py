from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(m)
    Space Complexity: O(1)
    m = length of total characters
    """

    def maximumValue(self, strs: List[str]) -> int:
        ans = -1
        for s in strs:
            if s.isnumeric():
                ans = max(int(s), ans)
            else:
                ans = max(len(s), ans)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maximumValue",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(strs=["alic3", "bob", "3", "4", "00000"]) == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(strs=["1", "01", "001", "0001"]) == 1
