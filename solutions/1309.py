import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Check next 2 character
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def freqAlphabets(self, s: str) -> str:
        decrpyted_s = ""
        a_ord_offset = ord("a") - 1
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                decrpyted_s += chr(int(s[i : i + 2]) + a_ord_offset)
                i += 3
            else:
                decrpyted_s += chr(int(s[i]) + a_ord_offset)
                i += 1
        return decrpyted_s


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "freqAlphabets",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("10#11#12") == "jkab"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("1326#") == "acz"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#") == "abcdefghijklmnopqrstuvwxyz"
