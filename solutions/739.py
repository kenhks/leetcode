from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > t:
                    ans[i] = j - i
                    break
        return ans


class Solution2:
    """
    Hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        temp_map = {}
        for i, t in enumerate(temperatures):
            cooler_temperatures = [prev_t for prev_t in temp_map if prev_t < t]
            for prev_t in cooler_temperatures:
                for prev_t_index in temp_map.pop(prev_t):
                    ans[prev_t_index] = i - prev_t_index
            if t not in temp_map:
                temp_map[t] = [i]
            else:
                temp_map[t].append(i)
        return ans


class Solution3:
    """
    Scan from right
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        max_temp = 0
        for i in range(len(temperatures) - 1, -1, -1):
            if temperatures[i] >= max_temp:
                max_temp = temperatures[i]
                continue
            days = 1
            while temperatures[i + days] <= temperatures[i]:
                days += ans[i + days]
            ans[i] = days
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "dailyTemperatures",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    assert solution(temperatures) == [1, 1, 4, 2, 1, 1, 0, 0]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    temperatures = [30, 40, 50, 60]
    assert solution(temperatures) == [1, 1, 1, 0]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    temperatures = [30, 60, 90]
    assert solution(temperatures) == [1, 1, 0]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    temperatures = [30]
    assert solution(temperatures) == [0]
