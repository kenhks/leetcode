from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan from left and right
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def maxDistance(self, colors: List[int]) -> int:
        right = len(colors) - 1
        while colors[0] == colors[right]:
            right -= 1
        left = 0
        while colors[left] == colors[-1]:
            left += 1
        return max(right, len(colors) - 1 - left)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxDistance",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    colors = [1, 1, 1, 6, 1, 1, 1]
    assert solution(colors) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    colors = [1, 8, 3, 8, 3]
    assert solution(colors) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    colors = [0, 1]
    assert solution(colors) == 1
