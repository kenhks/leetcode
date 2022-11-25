import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Count uppercase letter
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def detectCapitalUse(self, word: str) -> bool:
        ans = False
        upper_count = 0
        for i, c in enumerate(word):
            if c.isupper():
                if upper_count != i:
                    upper_count = -1
                    break
                upper_count += 1
        if upper_count == 0 or (upper_count == 1 and word[0].isupper()) or upper_count == len(word):
            ans = True
        return ans


class Solution2:
    """
    Python built-in
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper() and word[1:].islower():
            return True
        if word[0:].isupper():
            return True
        if word[0:].islower():
            return True
        return False


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "detectCapitalUse",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution()


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution()


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution()
