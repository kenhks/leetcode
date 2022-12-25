from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Array for tile count, swap count
    Time Complexity: O(n) = 2n + 12
    Space Complexity: O(1) = 28
    """

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        domino_faces = 6
        top_count = [0] * (domino_faces + 1)
        top_swap_count = top_count.copy()
        bottom_count = top_count.copy()
        bottom_swap_count = top_count.copy()
        for v1, v2 in zip(tops, bottoms):
            top_count[v1] += 1
            bottom_count[v2] += 1
            if v1 != v2:
                top_swap_count[v2] += 1
                bottom_swap_count[v1] += 1
        ans = len(tops) + 1
        for v in range(1, 7):
            min_top_swap = len(tops) - top_count[v]
            if top_swap_count[v] >= min_top_swap:
                ans = min(ans, min_top_swap)
            min_bottom_swap = len(tops) - bottom_count[v]
            if bottom_swap_count[v] >= min_bottom_swap:
                ans = min(ans, min_bottom_swap)
        return ans if ans <= len(tops) else -1


class Solution2:
    """
    Array for tile count, swap count and extra same count
    Time Complexity: O(n) = 2n + 12
    Space Complexity: O(1) = 14
    """

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        domino_faces = 6
        top_count = [0] * (domino_faces + 1)
        bottom_count = top_count.copy()
        same_count = 0
        for v1, v2 in zip(tops, bottoms):
            top_count[v1] += 1
            bottom_count[v2] += 1
            if v1 == v2:
                same_count += 1
        ans = -1
        for v in range(1, 7):
            if (top_count[v] + bottom_count[v] - same_count) == len(tops):
                ans = len(tops) - max(top_count[v], bottom_count[v])
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minDominoRotations",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    tops = [2, 1, 2, 4, 2, 2]
    bottoms = [5, 2, 6, 2, 3, 2]
    assert solution(tops, bottoms) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    tops = [3, 5, 1, 2, 3]
    bottoms = [3, 6, 3, 3, 4]
    assert solution(tops, bottoms) == -1
