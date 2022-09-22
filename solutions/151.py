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
        reversed_s = []
        word_left = word_right = -1
        for i, c in enumerate(s):
            if word_left < 0 and c == " ":
                continue
            if c != " ":
                if word_left == -1:
                    word_left = i
                word_right = i
            else:
                reversed_s.append(s[word_left : word_right + 1])
                word_left = word_right = -1
        if word_left != -1:
            reversed_s.append(s[word_left : word_right + 1])
        res = ""
        for i in range(len(reversed_s) - 1, -1, -1):
            if i == len(reversed_s) - 1:
                res = reversed_s[i]
            else:
                res += f" {reversed_s[i]}"
        return res


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
