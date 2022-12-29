from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(nlog(10, n))
    Space Complexity: O(1)
    """

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if all(int(j) != 0 and i % int(j) == 0 for j in str(i))]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "selfDividingNumbers",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(left=1, right=22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(left=47, right=85) == [48, 55, 66, 77]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(left=1, right=100) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        11,
        12,
        15,
        22,
        24,
        33,
        36,
        44,
        48,
        55,
        66,
        77,
        88,
        99,
    ]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(left=100, right=1000) == [
        111,
        112,
        115,
        122,
        124,
        126,
        128,
        132,
        135,
        144,
        155,
        162,
        168,
        175,
        184,
        212,
        216,
        222,
        224,
        244,
        248,
        264,
        288,
        312,
        315,
        324,
        333,
        336,
        366,
        384,
        396,
        412,
        424,
        432,
        444,
        448,
        488,
        515,
        555,
        612,
        624,
        636,
        648,
        666,
        672,
        728,
        735,
        777,
        784,
        816,
        824,
        848,
        864,
        888,
        936,
        999,
    ]
