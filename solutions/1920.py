from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use seperate array
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans


class Solution2:
    """
    Encode orignal and new value
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] += len(nums) * (nums[nums[i]] % len(nums))
        for i in range(len(nums)):
            nums[i] //= len(nums)
        return nums


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "buildArray",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [0, 2, 1, 5, 3, 4]
    assert solution(nums) == [0, 1, 2, 4, 5, 3]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [5, 0, 1, 2, 3, 4]
    assert solution(nums) == [4, 5, 0, 1, 2, 3]
