from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative DP
    Time Complexity: O(n)
    Space Complexity: O(26)
    """

    def maxLength(self, arr: List[str]) -> int:
        unique_arr = []
        for s in arr:
            s_unique = set(s)
            if len(s_unique) == len(s):
                unique_arr.append(s_unique)
        dp = [set()]
        for s in unique_arr:
            for prev_s in dp:
                if not s & prev_s:
                    dp.append(s | prev_s)
        return max(len(i) for i in dp)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxLength",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(["un", "iq", "ue"]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(["cha", "r", "act", "ers"]) == 6


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(["abcdefghijklmnopqrstuvwxyz"]) == 26


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(["a", "b", "c", "d", "e"]) == 5
