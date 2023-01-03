from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Swap in-place twice, two pointer
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == 0:
                left += 1
            elif nums[right] == 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -= 1
            else:
                right -= 1
        right = len(nums) - 1
        while left <= right:
            if nums[left] == 1:
                left += 1
            elif nums[right] == 1:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -= 1
            else:
                right -= 1


class Solution2:
    """
    Swap in-place, three pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = left = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                if i > left:
                    nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "sortColors",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [2, 0, 2, 1, 1, 0]
    expected = [0, 0, 1, 1, 2, 2]
    solution(nums)
    assert nums == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [2, 0, 1]
    expected = [0, 1, 2]
    solution(nums)
    assert nums == expected


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [1, 0, 0]
    expected = [0, 0, 1]
    solution(nums)
    assert nums == expected
