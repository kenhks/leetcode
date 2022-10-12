from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        if nums[-1] <= 0:
            squares = [i**2 for i in nums[::-1]]
        elif nums[0] >= 0:
            squares = [i**2 for i in nums]
        else:
            squares = []
            while left <= right:
                if abs(nums[left]) >= abs(nums[right]):
                    squares.insert(0, nums[left] ** 2)
                    left += 1
                else:
                    squares.insert(0, nums[right] ** 2)
                    right -= 1
        return squares


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "sortedSquares",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([0]) == [0]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([-4, -1, 0]) == [0, 1, 16]
