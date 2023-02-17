from collections import Counter

from typing import List
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for frequency count
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [i for i, j in Counter(nums).items() if j == 2]


class Solution2:
    """
    Flip array value
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            n = abs(nums[i])
            index = n - 1
            if nums[index] < 0:
                ans.append(n)
            else:
                nums[index] *= -1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "findDuplicates",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    assert set(solution(nums)) == set([2, 3])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [1, 1, 2]
    assert set(solution(nums)) == set([1])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [1]
    assert set(solution(nums)) == set([])
