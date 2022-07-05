from functools import reduce
from typing import List

import pytest

from utils import create_function


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        unique = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
                unique.add(i)
            else:
                unique.remove(i)
        return next(i for i in unique)


solution_func_name = "singleNumber"
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
    assert solution([2, 2, 1]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([4, 1, 2, 1, 2]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1]) == 1
