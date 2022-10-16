from collections import defaultdict
from typing import Dict, List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^4)
    Space Complexity: O(1)
    """

    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        if (nums[a] + nums[b] + nums[c]) == nums[d]:
                            count += 1
        return count


class Solution2:
    """
    Hashmap for frequency count
    Time Complexity: O(n^3)
    Space Complexity: O(n)
    """

    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        freq: Dict[int, int] = {}

        for c in range(len(nums) - 1, 1, -1):
            for b in range(c - 1, 0, -1):
                for a in range(b - 1, -1, -1):
                    target_sum = nums[a] + nums[b] + nums[c]
                    if target_sum in freq:
                        count += freq[target_sum]
            freq[nums[c]] = freq.get(nums[c], 0) + 1
        return count


class Solution3:
    """
    Hashmap for frequency count
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        freq: Dict[int, int] = defaultdict(int)
        freq[nums[0] + nums[1]] += 1
        for i in range(2, len(nums) - 1):
            c = i
            for d in range(c + 1, len(nums)):
                count += freq[nums[d] - nums[c]]
            a = i
            for b in range(a):
                freq[nums[a] + nums[b]] += 1
        return count


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "countQuadruplets",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 3, 6]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[3, 3, 6, 4, 5]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[1, 1, 1, 3, 5]) == 4
