import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use set
    Time Complexity: O(n)
    Space Complexity: O(1) = 26
    """

    def checkIfPangram(self, sentence: str) -> bool:
        pangram_set = set()
        is_pangram: bool = False
        for c in sentence:
            pangram_set.add(c)
            if len(pangram_set) == 26:
                is_pangram = True
                break
        return is_pangram


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "checkIfPangram",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(sentence="thequickbrownfoxjumpsoverthelazydog")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(sentence="leetcode")
