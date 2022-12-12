from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    BruteForce with hashmap
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """

    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0

        def hammingdistance(x, y):
            xor_result = x ^ y
            distance = 0
            while xor_result:
                distance += xor_result & 1
                xor_result = xor_result >> 1
            return distance

        if len(nums) > 1:
            seen = {}
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] != nums[j]:
                        key = (min(nums[i], nums[j]), max(nums[i], nums[j]))
                        if key not in seen:
                            seen[key] = hammingdistance(nums[i], nums[j])
                        total += seen[key]
        return total


class Solution2:
    """
    Count 1 and 0 at each bit
    Time Complexity: O(n) = 33n
    Space Complexity: O(1)
    """

    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        max_n = max(nums)
        for bit in range(32):
            one_count = 0
            mask = 1 << bit
            if mask > max_n:
                break
            for i in nums:
                one_count += i & mask > 0
            total += one_count * (n - one_count)
        return total


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "totalHammingDistance",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([4, 14, 2]) == 6


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([4, 14, 4]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([0]) == 0
