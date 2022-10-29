from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def minDeletion(self, nums: List[int]) -> int:
        fast, slow = 1, 0
        count = 0
        while fast < len(nums):
            while fast < len(nums) and nums[slow] == nums[fast]:
                count += 1
                fast += 1
            else:
                slow = fast + 1
                fast += 2
        if (len(nums) - count) & 1 == 1:
            count += 1
        return count


class Solution2:
    """
    Check Last num
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def minDeletion(self, nums: List[int]) -> int:
        count = 0
        previous = -1

        for num in nums:
            if num == previous:
                count += 1
            else:
                previous = num if previous < 0 else -1
        return count + (previous >= 0)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minDeletion",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 1, 2, 3, 5]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 1, 2, 2, 3, 3]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([0, 6, 6, 1, 8, 7]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([1]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    nums = [7, 1, 2, 2, 1, 7, 5, 8, 0, 2, 0, 7, 4, 1, 4, 3, 6, 9, 4]
    assert solution(nums) == 1
