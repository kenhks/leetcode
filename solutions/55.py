from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for i, n in enumerate(nums):
            if i == max_pos and n == 0:
                break
            max_pos = max(i + n, max_pos)
            if max_pos >= (len(nums) - 1):
                break
        return max_pos >= (len(nums) - 1)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "canJump",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[2, 3, 1, 1, 4])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution([3, 2, 1, 0, 4])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([0])


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([1, 2])


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0])
