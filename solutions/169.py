from itertools import groupby
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use frequency hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def majorityElement(self, nums: List[int]) -> int:
        cutoff = len(nums) / 2
        freq = {}
        result = None
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
            if freq[n] >= cutoff:
                result = n
                break
        return result


class Solution2:
    """
    Boyer-Moore Majority vote algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        res, times = 0, 0
        for i in nums:
            if times == 0:
                res = i
            if i == res:
                times += 1
            else:
                times -= 1
        return res


class Solution3:
    """
    Sort and group
    Time Complexity: O(nlog(2,n))
    Space Complexity: O(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majority = len(nums) // 2
        for num, group in groupby(nums):
            if len(list(group)) > majority:
                return num


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "majorityElement",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [3, 2, 3]
    assert solution(nums) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [2, 2, 1, 1, 1, 2, 2]
    assert solution(nums) == 2
