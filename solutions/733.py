from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    DFS
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    m = len(image)
    n = len(image[0])
    """

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        changed = set()

        def flood(x, y, original_color):
            if (x, y) in changed or x < 0 or y < 0 or x >= len(image[0]) or y >= len(image):
                pass
            else:
                changed.add((x, y))
                if image[y][x] == original_color:
                    image[y][x] = color
                    flood(x, y + 1, original_color)
                    flood(x, y - 1, original_color)
                    flood(x - 1, y, original_color)
                    flood(x + 1, y, original_color)

        if image[sr][sc] != color:
            flood(sc, sr, image[sr][sc])
        return image


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "floodFill",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    result = [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]
    assert solution(image, sr=1, sc=1, color=2) == result


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    image = [
        [0, 0, 0],
        [0, 0, 0],
    ]
    result = [
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert solution(image, sr=0, sc=0, color=0) == result
