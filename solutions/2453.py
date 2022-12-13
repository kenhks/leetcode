from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Modulo Ring
    Time Complexity: O(n + k)
    Space Complexity: O(k)
    """

    def destroyTargets(self, nums: List[int], space: int) -> int:
        ring = {}
        for n in nums:
            ring_key = n % space
            if ring_key not in ring:
                ring[ring_key] = [1, n]
            else:
                ring[ring_key][0] += 1
                ring[ring_key][1] = min(n, ring[ring_key][1])
        return sorted(ring.values(), key=lambda x: (-x[0], x[1]))[0][1]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "destroyTargets",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[3, 7, 8, 1, 1, 5], space=2) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 3, 5, 2, 4, 6], space=2) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[6, 2, 5], space=100) == 2
