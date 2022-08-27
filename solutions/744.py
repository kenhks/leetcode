from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Linear Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]


class Solution2:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "nextGreatestLetter",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(["c", "f", "j"], "a") == "c"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(["c", "f", "j"], "c") == "f"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(["c", "f", "j"], "d") == "f"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(["c", "f", "j"], "x") == "c"


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(["a", "b", "c", "d", "e", "f", "g"], "d") == "e"


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution(["a", "b", "c"], "z") == "a"
