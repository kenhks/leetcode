import pytest

from utils import parametrize_solution_cls


class Solution:

    """
    Recursive
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    domino_cache = {0: 1, 1: 1, 2: 2}
    tromino_cache = {0: 1, 1: 0, 2: 1}

    def numTilings(self, n: int) -> int:
        return self.domino(n) % (10**9 + 7)

    def domino(self, n):
        if n in self.domino_cache:
            return self.domino_cache[n]
        else:
            self.domino_cache[n] = self.domino(n - 1) + self.domino(n - 2) + self.tromino(n - 1) * 2
            return self.domino_cache[n]

    def tromino(self, n):
        if n in self.tromino_cache:
            return self.tromino_cache[n]
        else:
            self.tromino_cache[n] = self.domino(n - 2) + self.tromino(n - 1)
            return self.tromino_cache[n]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "numTilings",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(1) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(2) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(3) == 5


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(4) == 11


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(5) == 24
