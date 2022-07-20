from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = {}
        for i in nums:
            if i in nums_set:
                return True
            else:
                nums_set[i] = True
        return False


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "containsDuplicate",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 3, 1])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution([1, 2, 3, 4])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
