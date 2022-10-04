from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Dynamic hashmap to check anagram
    Time Complexity: O(n)
    Space Complexity: O(1) = 52
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) <= len(s):
            p_counter = Counter(p)
            s_counter = Counter(s[: len(p)])
            if p_counter == s_counter:
                res.append(0)
            for i in range(len(p), len(s)):
                s_counter[s[i]] = s_counter.get(s[i], 0) + 1
                s_counter[s[i - len(p)]] -= 1
                if s_counter == p_counter:
                    res.append(i - len(p) + 1)
        return res


class Solution2:
    """
    Use hashed sum to check anagram
    Time Complexity: O(n)
    Space Complexity: O(1) = 2
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) <= len(s):
            p_hash = sum(hash(c) for c in p)
            p_len = len(p)
            s_hash = sum(hash(c) for c in s[:p_len])
            if p_hash == s_hash:
                res.append(0)
            for i, c in enumerate(s[p_len:]):
                s_hash += hash(c) - hash(s[i])
                if p_hash == s_hash:
                    res.append(i + 1)
        return res


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "findAnagrams",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="cbaebabacd", p="abc") == [0, 6]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="abab", p="ab") == [0, 1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="abc", p="d") == []


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(s="abc", p="defg") == []
