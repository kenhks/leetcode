from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Rolling hashset
    Time Complexity: O(n)
    Space Complexity: O(1)/O(n)
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        k = min(len(nums), k)
        rolling_set = set(nums[:k])
        if len(rolling_set) < k:
            return True
        ans = False
        left, right = 0, k
        while right < len(nums):
            if nums[right] in rolling_set:
                ans = True
                break
            rolling_set.remove(nums[left])
            rolling_set.add(nums[right])
            left += 1
            right += 1
        return ans


class Solution2:
    """
    Hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        ans = False
        d = {}
        for i, x in enumerate(nums):
            if x in d and (i - d[x]) <= k:
                ans = True
                break
            d[x] = i
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "containsNearbyDuplicate",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 3, 1], k=3)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 0, 1, 1], k=1)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(nums=[1, 2, 3, 1, 2, 3], k=2)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(nums=[99, 99], k=2)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert not solution(nums=[1, 2, 1], k=0)


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert not solution(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=20)
