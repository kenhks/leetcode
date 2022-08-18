import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Count magazine with hashmap, decrease count by ransomNote
    Time Complexity: O(m + n)
    Space Complexity: O(m)
    m = len(magazine), n = len(ransomNote)
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_count = {}
        for m_char in magazine:
            if m_char in m_count:
                m_count[m_char] += 1
            else:
                m_count[m_char] = 1
        for r_char in ransomNote:
            if r_char in m_count:
                m_count[r_char] -= 1
                if m_count[r_char] < 0:
                    return False
            else:
                return False
        return True


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "canConstruct",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert not solution("a", "b")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution("aa", "ab")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("aa", "aab")
