import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i, c in enumerate(s):
            if c in freq:
                freq[c] = -1
            else:
                freq[c] = i
        return next((freq[j] for j in freq if freq[j] >= 0), -1)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "firstUniqChar",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("leetcode") == 0


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("loveleetcode") == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("aabb") == -1
