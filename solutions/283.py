from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Pop and append
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, count = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                count += 1
                nums.pop(i)
            else:
                i += 1
        nums += [0] * count


class Solution2:
    """
    Swap in place
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_nonzero = 0
        for cur, i in enumerate(nums):
            if i != 0:
                nums[next_nonzero], nums[cur] = nums[cur], nums[next_nonzero]
                next_nonzero += 1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "moveZeroes",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [0, 1, 0, 3, 12]
    solution(nums)
    assert nums == [1, 3, 12, 0, 0]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [0, 1, 0, 3, 12]
    Solution2().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]
