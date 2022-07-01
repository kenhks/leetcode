from typing import List

import pytest

from utils import create_function


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, x in enumerate(nums):
            if (target - x) in hmap:
                return [i, hmap[target - x]]
            hmap[x] = i


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i + 1:]):
                if x + y == target:
                    return [i, i + j + 1]


solution_func_name = "twoSum"
solution_class = [
    Solution,
    Solution2,
]


solutions = [
    lambda *args, **kwargs: (
        create_function(sol_cls, solution_func_name)(*args, **kwargs)
    )
    for sol_cls in solution_class
]


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([2, 7, 11, 15], 9) == [0, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([3, 2, 4], 6) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([3, 3], 6) == [0, 1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([-3, 3, 10, 8], 5) == [0, 3]
