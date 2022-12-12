import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalpha():
                left += 1
                continue
            if not s[right].isalpha():
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "reverseOnlyLetters",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="ab-cd") == "dc-ba"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
