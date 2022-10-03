from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2) = n^2 + n
    Space Complexity: O(n)
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        exists = set(nums)
        missing = []
        for i in range(1, len(nums) + 1):
            if i not in exists:
                missing.append(i)
        return missing


class Solution2:
    """
    Set difference
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        total_set = set(range(1, len(nums) + 1))
        return list(total_set - set(nums))


class Solution3:
    """
    Set difference
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            temp = abs(i) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        missing = []
        for i, n in enumerate(nums, start=1):
            if n > 0:
                missing.append(i)
        return missing


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "findDisappearedNumbers",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 1]) == [2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1]) == []
