from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2) = n * (n + 1) / 2
    Space Complexity: O(1)
    """

    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i, x in enumerate(height):
            for j, y in enumerate(height[i + 1 :], start=i + 1):
                res = max(res, min(x, y) * (j - i))
        return res


class Solution2:
    """
    Two Pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "maxArea",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 1]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([4, 3, 2, 1, 4]) == 16


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([1, 2, 4, 3]) == 4
