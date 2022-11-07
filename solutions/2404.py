from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use hashmap with optimization
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def mostFrequentEven(self, nums: List[int]) -> int:
        ans = -1
        counter = {}
        threshold = len(nums) / 2
        for n in nums:
            if n in counter:
                counter[n] += 1
                if counter[n] > threshold:
                    ans = n
                    break
            elif n % 2 == 0:
                counter[n] = 1
        if ans == -1:
            ans = max(counter.items(), key=lambda x: (x[1], -x[0]), default=(-1, 0))[0]
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "mostFrequentEven",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([0, 1, 2, 2, 4, 4, 1]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([4, 4, 4, 9, 2, 4]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([29, 47, 21, 41, 13, 37, 25, 7]) == -1
