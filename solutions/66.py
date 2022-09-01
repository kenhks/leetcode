from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Inplace
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry and 0 <= i:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                carry = 0
        if carry:
            digits = [1] + digits
        return digits


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "plusOne",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 3]) == [1, 2, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([4, 3, 2, 1]) == [4, 3, 2, 2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([9]) == [1, 0]
