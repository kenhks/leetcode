from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Backtracking
    Time Complexity: O(2^n * n^2)
    Space Complexity: O(1)
    """

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for n in nums:
            new_ans = [[n]]
            for prev_seq in ans:
                new_seq = prev_seq.copy()
                if new_seq[-1] <= n:
                    new_seq.append(n)
                    new_ans.append(new_seq)
            ans.extend(new_ans)
        return list(set(tuple(i) for i in ans if len(i) >= 2))


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findSubsequences",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [4, 6, 7, 7]
    expected = [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
    assert set(tuple(i) for i in solution(nums)) == set(tuple(i) for i in expected)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [4, 4, 3, 2, 1]
    expected = [[4, 4]]
    assert set(tuple(i) for i in solution(nums)) == set(tuple(i) for i in expected)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [1, 2, 3, 4, 5]
    expected = [
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 5],
        [1, 2, 4],
        [1, 2, 4, 5],
        [1, 2, 5],
        [1, 3],
        [1, 3, 4],
        [1, 3, 4, 5],
        [1, 3, 5],
        [1, 4],
        [1, 4, 5],
        [1, 5],
        [2, 3],
        [2, 3, 4],
        [2, 3, 4, 5],
        [2, 3, 5],
        [2, 4],
        [2, 4, 5],
        [2, 5],
        [3, 4],
        [3, 4, 5],
        [3, 5],
        [4, 5],
    ]
    assert set(tuple(i) for i in solution(nums)) == set(tuple(i) for i in expected)
