import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with stack
    Time Complexity: O(n)
    Space Complexity: O(1) = 2
    """

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append((s1[i], s2[i]))
                if len(diff) >= 3:
                    break
        return not diff or (len(diff) == 2 and diff[0][::-1] == diff[1])


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "areAlmostEqual",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("bank", "kanb")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution("attack", "defend")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("kelb", "kelb")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution("batkn", "kanbt")


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert not solution("qweabcd", "qefabcd")


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert not solution("aa", "ac")
