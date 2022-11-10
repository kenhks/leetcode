import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c != "-":
                size += 1
        first_groupsize = size % k if size > k else 0
        first_group, ans = "", ""
        group_count = 0
        for c in s:
            if c != "-":
                c = c.upper()
                if len(first_group) < first_groupsize:
                    first_group += c
                elif group_count < k:
                    ans += c
                    group_count += 1
                elif group_count == k:
                    ans += f"-{c}"
                    group_count = 1
        return f"{first_group}-{ans}" if first_groupsize > 0 else ans


class Solution2:
    """
    Reverse Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ""
        group_count = 0
        for c in s[::-1]:
            if c != "-":
                c = c.upper()
                if group_count < k:
                    ans = c + ans
                    group_count += 1
                elif group_count == k:
                    ans = f"{c}-{ans}"
                    group_count = 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "licenseKeyFormatting",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="5F3Z-2e-9-w", k=4) == "5F3Z-2E9W"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="2-5g-3-J", k=2) == "2-5G-3J"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="a", k=1) == "A"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(s="a", k=2) == "A"


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(s="---", k=3) == ""
