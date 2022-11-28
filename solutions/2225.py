from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for loss count
    Time Complexity: O(nlog(2, n))
    Space Complexity: O(n)
    """

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        for winner, loser in matches:
            if winner not in loss_count:
                loss_count[winner] = 0
            loss_count[loser] = loss_count.get(loser, 0) + 1
        ans1, ans2 = [], []
        for i, j in loss_count.items():
            if j == 0:
                ans1.append(i)
            elif j == 1:
                ans2.append(i)
        ans1.sort()
        ans2.sort()
        return [ans1, ans2]


class Solution2:
    """
    Counting Loss with array
    Time Complexity: O(n + k)
    Space Complexity: O(k)
    """

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = [-1] * 100001
        for winner, loser in matches:
            if loss_count[winner] == -1:
                loss_count[winner] == 0
            if loss_count[loser] == -1:
                loss_count[loser] = 1
            else:
                loss_count[loser] += 1
        ans1, ans2 = [], []
        for i in range(1, 100001):
            if loss_count[i] == 0:
                ans1.append(i)
            elif loss_count[i] == 1:
                ans2.append(i)
        return [ans1, ans2]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findWinners",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    expected = [[1, 2, 10], [4, 5, 7, 8]]
    assert solution(matches) == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
    expected = [[1, 2, 5, 6], []]
    assert solution(matches) == expected
