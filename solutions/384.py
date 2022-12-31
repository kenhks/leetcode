import random

import pytest


class Solution:
    """
    Fisher-Yates Algorithm
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


solutions = [
    Solution,
]


@pytest.mark.skip(reason="randomness")
@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    ops = ["Solution", "shuffle", "reset", "shuffle"]
    args = [[[1, 2, 3]], [], [], []]
    expected_outputs = [None, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
    obj = solution(*args[0])
    actual_outputs = [None]
    for op, arg in zip(ops[1:], args[1:]):
        actual_outputs.append(getattr(obj, op)(*arg))
    assert actual_outputs == expected_outputs
