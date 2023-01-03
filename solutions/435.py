from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort by start and end
    Time Complexity: O(nlog(2, n)) = nlog(2, n)) + n
    Space Complexity: O(1) = 1
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prev_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < prev_end:
                ans += 1
                prev_end = min(interval[1], prev_end)
            else:
                prev_end = interval[1]
        return ans


class Solution2:
    """
    Sort by end only
    Time Complexity: O(nlog(2, n)) = nlog(2, n)) + n
    Space Complexity: O(1) = 1
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        cur = intervals[0]
        for i in intervals[1:]:
            if i[0] >= cur[1]:
                cur = i
            else:
                ans += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "eraseOverlapIntervals",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    assert solution(intervals) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    intervals = [[1, 2], [1, 2], [1, 2]]
    assert solution(intervals) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    intervals = [[1, 2], [2, 3]]
    assert solution(intervals) == 0
