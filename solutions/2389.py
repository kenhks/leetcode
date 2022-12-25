from bisect import bisect_right
from itertools import accumulate
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Binary Search on Accumulated num, with cache
    Time Complexity: O(mlog(2, m) + n) = mlog(2, m) + m + n
    Space Complexity: O(m + n)
    m = len(nums)
    n = len(queries)
    """

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        prefix = list(accumulate(nums))
        q_cache = {}
        for q in queries:
            if q in q_cache:
                ans.append(q_cache[q])
            else:
                q_cache[q] = bisect_right(prefix, q)
                ans.append(q_cache[q])
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "answerQueries",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    assert solution(nums, queries) == [2, 3, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [2, 3, 4, 5]
    queries = [1]
    assert solution(nums, queries) == [0]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [469781, 45635, 628818, 324948, 343772, 713803, 452081]
    queries = [816646, 929491]
    assert solution(nums, queries) == [3, 3]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    nums = [1, 2, 3, 4, 5, 6]
    queries = [1, 2, 3, 4, 5, 21]
    assert solution(nums, queries) == [1, 1, 2, 2, 2, 6]


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    nums = [1, 10, 100, 1000, 10000, 100000]
    queries = [1, 11, 111, 1111, 11111, 111111]
    assert solution(nums, queries) == [1, 2, 3, 4, 5, 6]
