from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Horizontal scanning
    Time Complexity: O(S)
    Space Complexity: O(1)
    S = the total number of all characters in the array
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for w in strs[1:]:
            if not prefix or not w:
                prefix = ""
                break
            for i in range(min(len(w), len(prefix))):
                if w[i] != prefix[i]:
                    break
                i += 1
            prefix = w[:i]
        return prefix


class Solution2:
    """
    Vertical scanning
    Time Complexity: O(S)
    Space Complexity: O(1)
    S = the total number of all characters in the array
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for w in strs[1:]:
            if not prefix or not w:
                prefix = ""
                break
            for i in range(min(len(w), len(prefix))):
                if w[i] != prefix[i]:
                    break
                i += 1
            prefix = w[:i]
        return prefix


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "longestCommonPrefix",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(["flower", "flow", "flight"]) == "fl"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(["dog", "racecar", "car"]) == ""


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(["ab", "a"]) == "a"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(["dog", "racecar", "car"]) == ""
