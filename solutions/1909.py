from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2) = n * (n - 1)
    Space Complexity: O(1)
    """

    def canBeIncreasing(self, nums: List[int]) -> bool:
        can = False
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i + 1 :]
            for j in range(1, len(new_nums)):
                if new_nums[j - 1] >= new_nums[j]:
                    break
            else:
                can = True
            if can:
                break
        return can


class Solution2:
    """
    Iterative scan with count
    Time Complexity: O(n) = n
    Space Complexity: O(1)
    """

    def canBeIncreasing(self, nums: List[int]) -> bool:
        dec_count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                dec_count += 1
                if dec_count == 2:
                    return False
                else:
                    to_remove = i
        if dec_count == 1:
            if (to_remove >= 2 and nums[to_remove - 2] >= nums[to_remove]) and (
                to_remove < (len(nums) - 1)
                and nums[to_remove - 1] >= nums[to_remove + 1]
            ):
                return False
        return dec_count <= 1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "canBeIncreasing",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 10, 5, 7])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution([2, 3, 1, 2])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution([1, 1, 1])


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([105, 924, 32, 968])
