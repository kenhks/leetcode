from typing import List
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Swap in-place
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()
        for i, n in enumerate(nums):
            if n not in seen:
                seen.add(n)
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return k


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "removeDuplicates",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [1, 1, 2]
    first_k_slot = solution(nums)
    assert nums[:first_k_slot] == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    first_k_slot = solution(nums)
    assert nums[:first_k_slot] == [0, 1, 2, 3, 4]
