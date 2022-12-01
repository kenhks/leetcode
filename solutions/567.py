from collections import Counter
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force with sorting
    Time Complexity: O(m(n - m)log(2, m)) = m(n - m)log(2, m) + mlog(2, m)
    Space Complexity: O(m(n - m)log(2, m)) = m(n - m)log(2, m)
    m = len(s1), n = len(s2)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = False
        if len(s2) >= len(s1):
            s1_sorted = sorted(s1)
            for i in range(len(s2)):
                sub_s2 = sorted(s2[i : i + len(s1)])
                if s1_sorted == sub_s2:
                    ans = True
                    break
        return ans


class Solution2:
    """
    Scan with Counter
    Time Complexity: O((n-m) + m) = 26(n-m) + m
    Space Complexity: O(1) = 52
    m = len(s1), n = len(s2)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = False
        if len(s2) >= len(s1):
            s1_counter = Counter(s1)
            sub_s2_counter = Counter(s2[: len(s1) - 1])
            left, right = 0, len(s1) - 1
            while right < len(s2):
                sub_s2_counter[s2[right]] = sub_s2_counter.get(s2[right], 0) + 1
                if s1_counter == sub_s2_counter:
                    ans = True
                    break
                sub_s2_counter[s2[left]] -= 1
                if sub_s2_counter[s2[left]] == 0:
                    sub_s2_counter.pop(s2[left])
                left += 1
                right += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "checkInclusion",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s1="ab", s2="eidbaooo")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(s1="ab", s2="eidboaoo")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(s1="abcde", s2="ab")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(s1="ab", s2="ba")
