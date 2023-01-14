from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    ans += 1
                if i == k and tickets[i] == 0:
                    break
        return ans


class Solution2:
    """
    Math
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(len(tickets)):
            ans += min(tickets[i], tickets[k] - (i > k))
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "timeRequiredToBuy",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    tickets = [2, 3, 2]
    k = 2
    assert solution(tickets, k) == 6


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    tickets = [5, 1, 1, 1]
    k = 0
    assert solution(tickets, k) == 8
