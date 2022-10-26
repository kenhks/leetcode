from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = len(nums)
        ans = False
        while s > 1 and not ans:
            for i in range(len(nums) - s + 1):
                if sum(nums[i : i + s]) % k == 0:
                    ans = True
                    break
            s -= 1
        return ans


class Solution2:
    """
    Cumulative sum
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        i = 0
        ans = False
        while i < (len(nums) - 1) and (not ans):
            i_sum = nums[i]
            for j in range(i + 1, len(nums)):
                i_sum += nums[j]
                if i_sum % k == 0:
                    ans = True
                    break
            i += 1
        return ans


class Solution3:
    """
    Hashmap of remainder position
    Time Complexity: O(n)
    Space Complexity: O(min(n, k))
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        ans = False
        remainder_map = {0: -1}
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder_map:
                remainder_map[r] = i + 1
            elif remainder_map[r] < i:
                ans = True
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "checkSubarraySum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[23, 2, 4, 6, 7], k=6)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[23, 2, 6, 4, 7], k=6)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(nums=[23, 2, 6, 4, 7], k=13)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution(nums=[0], k=1)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(nums=[5, 0, 0, 0], k=3)


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution(nums=[23, 6, 9], k=3)


@pytest.mark.parametrize("solution", solutions)
def test_7(solution):
    assert not solution(nums=[23, 6, 9], k=6)
