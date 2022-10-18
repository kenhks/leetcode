from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_employee, max_worktime = 0, -1
        last_leave_time = 0
        for i, t in logs:
            c_work_time = t - last_leave_time
            if c_work_time > max_worktime:
                max_employee = i
                max_worktime = c_work_time
            elif c_work_time == max_worktime:
                max_employee = min(i, max_employee)
            last_leave_time = t
        return max_employee


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "hardestWorker",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    n = 10
    logs = [[0, 3], [2, 5], [0, 9], [1, 15]]
    assert solution(n, logs) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    n = 26
    logs = [[1, 1], [3, 7], [2, 12], [7, 17]]
    assert solution(n, logs) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    n = 2
    logs = [[0, 10], [1, 20]]
    assert solution(n, logs) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    n = 70
    logs = [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]
    assert solution(n, logs) == 12
