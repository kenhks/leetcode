from itertools import accumulate
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(prod):
                if i != j:
                    prod[j] = y * x
        return prod


class Solution2:
    """
    Use two array of cumulative sum
    Time Complexity: O(n) = 3n
    Space Complexity: O(n) = 3n
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_cum_prod = [1] + list(accumulate(nums, lambda a, b: a * b))
        right_cum_prod = [1] + list(accumulate(nums[::-1], lambda a, b: a * b))
        prod = []
        for i in range(len(nums)):
            prod.append(left_cum_prod[i] * right_cum_prod[-2 - i])
        return prod


class Solution3:
    """
    Use two pointer of cumulative sum
    Time Complexity: O(n) = 2n
    Space Complexity: O(n) = n + 2
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prod = [1] * size
        left_product = right_product = 1
        for i, x in enumerate(nums):
            if i > 0:
                prod[i] = left_product
            left_product *= x
        for j, y in enumerate(nums[::-1]):
            if j > 0:
                prod[size - j - 1] *= right_product
            right_product *= y
        return prod


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "productExceptSelf",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 3, 4]) == [24, 12, 8, 6]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
