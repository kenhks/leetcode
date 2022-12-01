import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force, start from longest
    Time Complexity: O(n^2) = n * (n - 1) / 2
    Space Complexity: O(1) = 1
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        size = 1
        for sub_size in range(len(s), 1, -1):
            for i in range(len(s) - sub_size + 1):
                substring = s[i : i + sub_size]
                if len(set(substring)) == len(substring):
                    return len(substring)
        return size


class Solution2:
    """
    Scan with hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        size = 0
        left = -1
        c_map = {}
        for i, c in enumerate(s):
            if c in c_map:
                left = max(c_map[c], left)
            c_map[c] = i
            size = max(i - left, size)
        return size


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "lengthOfLongestSubstring",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abcabcbb") == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("bbbbb") == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("pwwkew") == 3


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution("") == 0


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution("b") == 1


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution("abcdefg") == 7


@pytest.mark.parametrize("solution", solutions)
def test_7(solution):
    assert solution("dvdf") == 3


@pytest.mark.parametrize("solution", solutions)
def test_8(solution):
    assert solution("abba") == 2
