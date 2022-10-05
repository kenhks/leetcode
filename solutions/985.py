from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(qn)
    Space Complexity: O(n)
    q = len(queries)
    """

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for val, index in queries:
            nums[index] += val
            res.append(sum(i for i in nums if i % 2 == 0))
        return res


class Solution2:
    """
    Calculate running even_sum
    Time Complexity: O(n + q)
    Space Complexity: O(n)
    q = len(queries)
    """

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(i for i in nums if i % 2 == 0)
        res = []
        for val, index in queries:
            if nums[index] % 2 == 0:
                if val % 2 == 0:
                    even_sum += val
                else:
                    even_sum -= nums[index]
            elif val % 2 == 1:
                even_sum += nums[index] + val
            nums[index] += val
            res.append(even_sum)
        return res


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "sumEvenAfterQueries",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    assert solution(nums, queries) == [8, 6, 2, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [1]
    queries = [[4, 0]]
    assert solution(nums, queries) == [0]
