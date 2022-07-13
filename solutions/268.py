from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap
    Time Complexity: O(2n)
    Space Complexity: O(n)
    """

    def missingNumber(self, nums: List[int]) -> int:
        num_map = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_map:
                return i


class Solution2:
    """
    Bitwise XOR to find unique number
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def missingNumber(self, nums: List[int]) -> int:
        unique = len(nums)
        for i, x in enumerate(nums):
            unique = unique ^ i ^ x
        return unique


class Solution3:
    """
    Math
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "missingNumber",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([3, 0, 1]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([0, 1]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
