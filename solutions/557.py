import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in, split and reverse
    Time Complexity: O(n) = 3n
    Space Complexity: O(n)
    """

    def reverseWords(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split()])


class Solution2:
    """
    Two pointer
    Time Complexity: O(n) = 3n
    Space Complexity: O(n)
    """

    def reverseWords(self, s: str) -> str:
        s_arr = list(s)
        left, right = 0, len(s) - 1
        for i in range(len(s)):
            if s_arr[i] == " " or i == len(s) - 1:
                if i == len(s) - 1:
                    right = len(s) - 1
                else:
                    right = i - 1
                while left < right:
                    s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                    left += 1
                    right -= 1
                left = i + 1
        return "".join(s_arr)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "reverseWords",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("God Ding") == "doG gniD"
