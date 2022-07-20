from collections import Counter

import pytest

from utils import parametrize_solution_cls


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_counts = [0] * 26
        for s_char, t_char in zip(s, t):
            char_counts[ord(s_char) - 97] += 1
            char_counts[ord(t_char) - 97] -= 1
        for count in char_counts:
            if count != 0:
                return False
        else:
            return True


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "isAnagram",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("anagram", "nagaram")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution("rat", "car")
