from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashset size
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


class Solution2:
    """
    Hashset, early break
    Time Complexity: O(n) = n
    Space Complexity: O(n)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = False
        seen = set()
        for n in nums:
            if n in seen:
                ans = True
                break
            seen.add(n)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "containsDuplicate",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 3, 1])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution([1, 2, 3, 4])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
