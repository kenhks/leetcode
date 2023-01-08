import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Array Counter for lowercase letter
    Time Complexity: O(m + n) = m + n + 26 + 2log(2, 26) + 26
    Space Complexity: O(1) = 104
    """

    def closeStrings(self, word1: str, word2: str) -> bool:
        ans = False
        if len(word1) == len(word2):
            counter1 = [0] * 26
            counter2 = [0] * 26
            for c in word1:
                counter1[ord(c) - 97] += 1
            for c in word2:
                counter2[ord(c) - 97] += 1
            for i in range(26):
                if counter1[i] != counter2[i] and (counter1[i] == 0 or counter2[i] == 0):
                    break
            else:
                counter1.sort()
                counter2.sort()
                ans = counter1 == counter2
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "closeStrings",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(word1="abc", word2="bca")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(word1="a", word2="aa")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(word1="cabbba", word2="abbccc")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution(word1="uau", word2="ssx")


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert not solution(word1="aaabbbbccddeeeeefffff", word2="aaaaabbcccdddeeeeffff")
