from collections import Counter
from functools import reduce
from math import gcd
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2 log(2, log(2, n)))
    Space Complexity: O(n)
    """

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        ans = False
        for i in range(2, len(deck) + 1):
            if len(deck) % i == 0:
                if all(v % i == 0 for v in counter.values()):
                    ans = True
                    break
        return ans


class Solution2:
    """
    Math, calculate GCD
    Time Complexity: O(nlog(2, log(2, n)))
    Space Complexity: O(n)
    """

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values()) >= 2


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "hasGroupsSizeX",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    deck = [1, 2, 3, 4, 4, 3, 2, 1]
    assert solution(deck)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    deck = [1, 1, 1, 2, 2, 2, 3, 3]
    assert not solution(deck)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    deck = [1]
    assert not solution(deck)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    deck = [1, 1]
    assert solution(deck)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    deck = [1, 1, 2, 2, 2, 2]
    assert solution(deck)
