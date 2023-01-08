from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort by descending and search
    Time Complexity: O(n^2) = n^2 + nlog(2,n)
    Space Complexity: O(n)
    """

    def specialArray(self, nums: List[int]) -> int:
        special = -1
        nums.sort(reverse=True)
        for i in range(min(nums[0], len(nums)), 0, -1):
            greater_count = 1
            for j in nums[1:]:
                if j >= i:
                    greater_count += 1
                else:
                    break
            if greater_count == i:
                special = i
                break
        return special


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "specialArray",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([3, 5]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([0, 4, 3, 0, 4]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([5, 5, 5, 5, 5]) == 5
