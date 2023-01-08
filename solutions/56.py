from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(n)
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for a, b in intervals:
            if a <= ans[-1][-1]:
                ans[-1][-1] = max(b, ans[-1][-1])
            else:
                ans.append([a, b])
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "merge",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    assert solution(intervals) == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    intervals = [[1, 4], [4, 5]]
    expected = [[1, 5]]
    assert solution(intervals) == expected
