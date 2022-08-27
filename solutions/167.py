from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            c_target = numbers[left] + numbers[right]
            if c_target < target:
                left += 1
            elif c_target > target:
                right -= 1
            else:
                break
        return [left + 1, right + 1]


class Solution2:
    """
    Scan with hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(numbers, start=1):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                break
        return [h[n], i]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "twoSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([2, 7, 11, 15], 9) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([2, 3, 4], 6) == [1, 3]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([-1, 0], -1) == [1, 2]
