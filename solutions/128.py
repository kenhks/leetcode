from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force with set
    Time Complexity: O(n^3)
    Space Complexity: O(n)
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_size = 0

        for x in nums_set:
            x_size = 1
            while x + 1 in nums_set:
                x += 1
                x_size += 1
            max_size = max(x_size, max_size)
        return max_size


class Solution2:
    """
    Sort and count with hashmap
    Time Complexity: O(nlog(n))
    Space Complexity: O(s), where s is the number of consective subarray
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        groups = {}
        for x in nums:
            if x in groups:
                continue
            elif (x - 1) in groups:
                groups[x] = groups.pop(x - 1) + 1
            else:
                groups[x] = 1
        return max(groups.values(), default=0)


class Solution3:
    """
    Scan with set
    Time Complexity: O(n) = n + s, where s is the number of consective subarray
    Space Complexity: O(n)
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_size = 0
        for x in nums_set:
            if (x - 1) not in nums_set:
                x_size = 1
                while x + 1 in nums_set:
                    x += 1
                    x_size += 1
            max_size = max(x_size, max_size)
        return max_size


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "longestConsecutive",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([100, 4, 200, 1, 3, 2]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([1, 2, 0, 1]) == 3
