from typing import Dict, List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2) = n * (n - 1)
    Space Complexity: O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i + 1 :]):
                if x + y == target:
                    return [i, i + j + 1]


class Solution2:
    """
    Scan with hashmap
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap: Dict[int, int] = {}
        for i, x in enumerate(nums):
            if (target - x) in hmap:
                return [i, hmap[target - x]]
            hmap[x] = i


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "twoSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert sorted(solution([2, 7, 11, 15], 9)) == [0, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert sorted(solution([3, 2, 4], 6)) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert sorted(solution([3, 3], 6)) == [0, 1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert sorted(solution([-3, 3, 10, 8], 5)) == [0, 3]
