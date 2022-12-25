import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        ans = True

        def check_validrome(left, right):
            ans = True
            while left < right:
                if s[left] != s[right]:
                    ans = False
                    break
                left += 1
                right -= 1
            return ans

        while left < right:
            if s[left] != s[right]:
                ans = check_validrome(left + 1, right) or check_validrome(left, right - 1)
                break
            else:
                left += 1
                right -= 1
        return ans


class Solution2:
    """
    Recurisve
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def validPalindrome(self, s: str) -> bool:
        def check_parlindrome(sub_s: str, delete: bool) -> bool:
            if len(sub_s) <= 1:
                return True
            elif sub_s[0] == sub_s[-1]:
                return check_parlindrome(sub_s[1:-1], delete)
            elif not delete:
                return check_parlindrome(sub_s[:-1], True) or check_parlindrome(sub_s[1:], True)
            else:
                return False

        return check_parlindrome(s, delete=False)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "validPalindrome",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("aba")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("abca")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution("abc")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution("razysdieftupaukuvjqmjblwulrexmsmrzdfjvwovxxxehqhrx")


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert not solution(
        "ognfjhgbjhzkqhzadmgqbwqsktzqwjexqvzjsopolnmvnymbbzoofzbbmynvmnloposjzvqxejwqztksqwbqgmdazhqkzhjbghjfno"
    )


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution(
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    )
