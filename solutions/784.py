from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(2^n)
    n = len(s)
    """

    def letterCasePermutation(self, s: str) -> List[str]:
        def possible_chars(char):
            if char.isdigit():
                return [char]
            elif char.isalpha():
                return [char.lower(), char.upper()]

        result: List[List[str]] = [[]]
        for char in s:
            chars = possible_chars(char)
            if len(chars) == 1:
                result = [i + chars for i in result]
            elif len(chars) == 2:
                result = [i + chars[:1] for i in result] + [i + chars[1:] for i in result]
        return ["".join(i) for i in result]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "letterCasePermutation",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    expected = [
        "a1b2",
        "a1B2",
        "A1b2",
        "A1B2",
    ]
    assert sorted(solution("a1b2")) == sorted(expected)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    expected = [
        "3z4",
        "3Z4",
    ]
    assert sorted(solution("3z4")) == sorted(expected)
