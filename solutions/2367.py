from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^3) = (n)(n - 1)(n - 2)
    Space Complexity: O(1)
    """

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[j] - nums[i]) == (nums[k] - nums[j]) == diff:
                        count += 1
        return count


class Solution2:
    """
    Hashset
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        count = 0
        for n in nums:
            if n - diff in seen and (n - 2 * diff) in seen:
                count += 1
            seen.add(n)
        return count


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "arithmeticTriplets",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[0, 1, 4, 6, 7, 10], diff=3) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[4, 5, 6, 7, 8, 9], diff=2) == 2
