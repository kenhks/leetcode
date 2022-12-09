import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution2:
    """
    Implement str.split and str.join
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def reverseWords(self, s: str) -> str:
        ans = ""
        prev_isspace = True
        word_start_index = -1
        for i, c in enumerate(s):
            if c.isspace():
                if not prev_isspace:
                    ans = f"{s[word_start_index : i]} {ans}"
                    print(f"{ans = }")
                prev_isspace = True
            else:
                if prev_isspace:
                    word_start_index = i
                prev_isspace = False
        if not prev_isspace:
            ans = f"{s[word_start_index : ]} {ans}"
        return ans[:-1]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "reverseWords",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("the sky is blue") == "blue is sky the"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("  hello world  ") == "world hello"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("a good   example") == "example good a"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution("a b c d e") == "e d c b a"
