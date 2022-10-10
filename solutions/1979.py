from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n) = n + log(2, a)
    Space Complexity: O(1)
    a = minimum value of nums
    """

    def findGCD(self, nums: List[int]) -> int:
        min_num = 1001
        max_num = 0
        for n in nums:
            min_num = min(n, min_num)
            max_num = max(n, max_num)

        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b > 0:
                a, b = b, a % b
            return a

        return gcd(min_num, max_num)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findGCD",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[2, 5, 6, 9, 10]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[7, 5, 6, 8, 3]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[3, 3]) == 3
