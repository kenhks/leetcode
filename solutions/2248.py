from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashset
    Time Complexity: O(S)
    Space Complexity: O(S)
    S = total element of nested array
    """

    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])
        for arr in nums[1:]:
            common &= set(arr)
        return sorted(common)


class Solution2:
    """
    Hashset
    Time Complexity: O(S)
    Space Complexity: O(S)
    S = total element of nested array
    """

    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = Counter()
        for arr in nums:
            counter.update(Counter(arr))
        return sorted(i for i, j in counter.items() if j == len(nums))


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "intersection",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    assert solution(nums) == [3, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [[1, 2, 3], [4, 5, 6]]
    assert solution(nums) == []
