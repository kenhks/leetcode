from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    String Concatenation
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if not s:
                s += str(i)
            arr.append(s)
        return arr


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "fizzBuzz",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(3) == ["1", "2", "Fizz"]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(5) == ["1", "2", "Fizz", "4", "Buzz"]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
