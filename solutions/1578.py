from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Group color
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        color_left = color_right = 0

        def group_cost(left, right):
            sub_cost_total = 0
            max_cost = 1
            for i in neededTime[left : right + 1]:
                sub_cost_total += i
                max_cost = max(max_cost, i)
            return sub_cost_total - max_cost

        for i in range(1, len(colors)):
            prev, cur = colors[i - 1], colors[i]
            if prev != cur:
                if color_right > color_left:
                    cost += group_cost(color_left, color_right)
                color_left = color_right = i
            else:
                color_right = i
        return cost + (group_cost(color_left, color_right) if color_right > color_left else 0)


class Solution2:
    """
    Two Pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left, ans = 0, 0
        for right in range(1, len(colors)):
            if colors[left] == colors[right]:
                if neededTime[left] < neededTime[right]:
                    ans += neededTime[left]
                else:
                    ans += neededTime[right]
                    continue
            left = right
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minCost",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abaac", neededTime=[1, 2, 3, 4, 5]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("abc", neededTime=[1, 2, 3]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("aabaa", neededTime=[1, 2, 3, 4, 1]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution("aaaaabaa", neededTime=[1, 6, 3, 10, 1, 3, 4, 1]) == 12


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution("a", neededTime=[1]) == 0
