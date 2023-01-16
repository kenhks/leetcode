from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Direct
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for i in range(len(row)):
                row[i] ^= 1
            row.reverse()
        return image


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "flipAndInvertImage",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert solution(image) == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    expected = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    assert solution(image) == expected
