from itertools import accumulate
from typing import List

import pytest


class NumArray:
    """
    Prefix Sum
    """
    def __init__(self, nums: List[int]):
        self.prefix_sum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - (self.prefix_sum[left - 1] if left > 0 else 0)


solutions = [
    NumArray,
]


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    ops = ["NumArray", "sumRange", "sumRange", "sumRange"]
    args = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    expected_outputs = [None, 1, -1, -3]
    obj = solution(*args[0])
    actual_outputs = [None]
    for op, arg in zip(ops[1:], args[1:]):
        actual_outputs.append(getattr(obj, op)(*arg))
    assert actual_outputs == expected_outputs
