from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort then scan
    Time Complexity: O(nlog(2, n))
    Space Complexity: O(n)
    """

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i + 1] != diff:
                return False
        else:
            return True


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "canMakeArithmeticProgression",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([3, 5, 1])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution([1, 2, 4])
