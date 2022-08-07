import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Count with size
    """

    def countVowelPermutation(self, n: int) -> int:
        modulo = 10**9 + 7
        vowels = set(["a", "e", "i", "o", "u"])
        count = {(1, v): 1 for v in vowels}
        for i in range(2, n + 1):
            count[i, "a"] = (
                count[i - 1, "e"] + count[i - 1, "i"] + count[i - 1, "u"]
            ) % modulo
            count[i, "e"] = (count[i - 1, "a"] + count[i - 1, "i"]) % modulo
            count[i, "i"] = (count[i - 1, "e"] + count[i - 1, "o"]) % modulo
            count[i, "o"] = count[i - 1, "i"]
            count[i, "u"] = (count[i - 1, "i"] + count[i - 1, "o"]) % modulo
        return sum(count[n, v] for v in vowels) % modulo


class Solution2:
    """
    Count without size n
    """

    def countVowelPermutation(self, n: int) -> int:
        modulo = 10**9 + 7
        vowels = set(["a", "e", "i", "o", "u"])
        count = {v: 1 for v in vowels}
        for _ in range(1, n):
            count["a"], count["e"], count["i"], count["o"], count["u"] = (
                (count["e"] + count["i"] + count["u"]) % modulo,
                (count["a"] + count["i"]) % modulo,
                (count["e"] + count["o"]) % modulo,
                count["i"],
                (count["i"] + count["o"]) % modulo,
            )
        return sum(count.values()) % modulo


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "countVowelPermutation",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(1) == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(2) == 10


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(5) == 68


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(107871933390123834060683597780808227512929) == 18208803
