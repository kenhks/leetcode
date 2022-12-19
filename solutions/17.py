from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    BFS, DP
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)
    """

    digit2letter = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        ans = [""] if digits else []
        for d in digits:
            ans = [prev + letter for prev in ans for letter in self.digit2letter[d]]
        return ans


class Solution2:
    """
    DFS, DP
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)
    """

    digit2letter = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)

        def dfs(prev, next):
            if len(prev) == n:
                ans.append(prev)
            else:
                for letter in self.digit2letter[digits[next]]:
                    dfs(prev + letter, next + 1)

        if n:
            dfs("", 0)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "letterCombinations",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(digits="23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(digits="") == []


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(digits="2") == ["a", "b", "c"]
