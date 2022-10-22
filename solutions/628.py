from functools import reduce
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time complexity: O(n^3)
    Space Complexity: O(1)
    """

    def maximumProduct(self, nums: List[int]) -> int:
        ans = nums[0] * nums[1] * nums[2]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    ans = max(ans, nums[i] * nums[j] * nums[k])
        return ans


class Solution2:
    """
    Sort by desecnding
    Time Complexity: O(nlog(2,n))
    Space Complexity: O(log(2, n))
    """

    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) > 3:
            nums.sort(reverse=True)
            return max(
                reduce(lambda x, y: x * y, nums[:3]),
                reduce(lambda x, y: x * y, [nums[0], nums[-1], nums[-2]]),
            )
        return reduce(lambda x, y: x * y, nums)


class Solution3:
    """
    Scan with min, max
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maximumProduct(self, nums: List[int]) -> int:
        a = b = c = -1001  # Max 3
        d = e = 1001  # Min 2
        for i in nums:
            if i >= a:
                a, b, c = i, a, b
            elif i >= b:
                b, c = i, b
            elif i >= c:
                c = i
            if i <= e:
                e, d = i, e
            elif i <= d:
                d = i
        max_value = a * b * c
        if d < 0 and e < 0:
            max_value = max(max_value, a * d * e)
        return max_value


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "maximumProduct",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 3]) == 6


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 2, 3, 4]) == 24


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[-1, -2, -3]) == -6
