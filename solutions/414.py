from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort and scan
    Time Complexity: O(nlog(2,n)) = nlog(2,n) + n
    Space Complexity: O(n)
    """

    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        distinct, last = 1, nums[0]
        for i in nums[1:]:
            if i != last:
                distinct += 1
            last = i
            if distinct == 3:
                break
        else:
            last = nums[0]
        return last


class Solution2:
    """
    Sort the nums set
    Time Complexity: O(nlog(2,n)) = nlog(2,n) + 2n
    Space Complexity: O(n)
    """

    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "thirdMax",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([3, 2, 1]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 2]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([2, 2, 3, 1]) == 1
