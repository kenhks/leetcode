import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with hashmap and hashset
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        used_chars = set()
        ans = True
        for i, j in zip(s, t):
            if i in char_map:
                if j != char_map[i]:
                    ans = False
                    break
            elif j in used_chars:
                ans = False
                break
            else:
                char_map[i] = j
                used_chars.add(j)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isIsomorphic",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("egg", "add")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution("foo", "bar")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("paper", "title")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution("bbbaaaba", "aaabbbba")


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert not solution("badc", "baba")
