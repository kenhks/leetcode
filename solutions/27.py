from typing import List
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Swap in-place
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, n in enumerate(nums):
            if n != val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return k


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "removeElement",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [3, 2, 2, 3]
    first_k_slot = solution(nums, 3)
    assert nums[:first_k_slot] == [2, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    first_k_slot = solution(nums, 2)
    assert nums[:first_k_slot] == [0, 1, 3, 0, 4]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [3, 3, 3, 3]
    first_k_slot = solution(nums, 3)
    assert nums[:first_k_slot] == []


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    nums = [3, 3, 3, 2, 3]
    first_k_slot = solution(nums, 3)
    assert nums[:first_k_slot] == [2]
