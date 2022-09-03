from functools import reduce
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    BFS, get numbers by level
    Time Complexity: O(2^n)
    Space Complexity: O(2^n) = 9/2 * 2^n + 9/4 * 2^n
    """

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        numbers = [[i] for i in range(1, 10) if (i - k >= 0) or i + k < 10]
        while n > 1:
            new_numbers = []
            for i in numbers:
                if i[-1] + k < 10:
                    new_numbers.append(i + [i[-1] + k])
                if k > 0 and i[-1] - k >= 0:
                    new_numbers.append(i + [i[-1] - k])
            numbers = new_numbers
            n -= 1
        return [reduce(lambda total, d: 10 * total + d, i, 0) for i in numbers]


class Solution2:
    """
    DFS, get numbers one by one in recursion
    Time Complexity: O(2^n)
    Space Complexity: O(2^n) = 9/2 * 2^n + n
    """

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def get_next_digits(valid_numbers, remain_digits):
            if remain_digits > 0:
                if valid_numbers[-1] + k < 10:
                    get_next_digits(
                        valid_numbers + [valid_numbers[-1] + k], remain_digits - 1
                    )
                if valid_numbers[-1] - k >= 0:
                    get_next_digits(
                        valid_numbers + [valid_numbers[-1] - k], remain_digits - 1
                    )
            else:
                ans.append(valid_numbers)

        if k > 0:
            ans = []
            numbers = [[i] for i in range(1, 10) if (i - k >= 0) or i + k < 10]
            for i in numbers:
                get_next_digits(i, n - 1)
            return [reduce(lambda total, d: 10 * total + d, i, 0) for i in ans]
        else:
            base = int("1" * n)
            return [i * base for i in range(1, 10)]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "numsSameConsecDiff",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert sorted(solution(n=3, k=7)) == [181, 292, 707, 818, 929]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert sorted(solution(n=2, k=1)) == [
        10,
        12,
        21,
        23,
        32,
        34,
        43,
        45,
        54,
        56,
        65,
        67,
        76,
        78,
        87,
        89,
        98,
    ]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert sorted(solution(n=2, k=0)) == [11, 22, 33, 44, 55, 66, 77, 88, 99]
