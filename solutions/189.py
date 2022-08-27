from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        k = k % len(nums)
        if k == 0:
            return
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]


class Solution2:
    """
    Python built-in
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "rotate",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [-1, -100, 3, 99]
    solution(nums, 2)
    assert nums == [3, 99, -1, -100]
