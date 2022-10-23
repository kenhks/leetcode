from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Check number frequency
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = [0, 0]
        for i in range(1, len(nums) + 1):
            if i not in cnt:
                ans[1] = i
            elif cnt[i] == 2:
                ans[0] = i
        return ans


class Solution2:
    """
    Sort
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(log(2, n))
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0, 1]
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                ans[0] = nums[i]
            elif nums[i + 1] > (nums[i] + 1):
                ans[1] = nums[i] + 1
        if nums[-1] != len(nums):
            ans[1] = len(nums)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "findErrorNums",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 2, 4]) == [2, 3]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 1]) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([2, 2]) == [2, 1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([3, 2, 3, 4, 6, 5]) == [3, 1]
