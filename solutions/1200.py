from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2) = n^2 + nlog(2, n)
    Space Complexity: O(n)
    """

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        min_diff = float("inf")
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                diff = abs(arr[i] - arr[j])
                if diff < min_diff:
                    min_diff = diff
                    ans.clear()
                    ans.append([min(arr[i], arr[j]), max(arr[i], arr[j])])
                elif diff == min_diff:
                    ans.append([min(arr[i], arr[j]), max(arr[i], arr[j])])
        ans.sort(key=lambda x: x[0])
        return ans


class Solution2:
    """
    Sort and Scan
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(n)
    """

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                ans.clear()
                ans.append([arr[i - 1], arr[i]])
                min_diff = diff
            elif diff == min_diff:
                ans.append([arr[i - 1], arr[i]])
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minimumAbsDifference",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    expecetd = [[1, 2], [2, 3], [3, 4]]
    assert solution([4, 2, 1, 3]) == expecetd


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    expected = [[1, 3]]
    assert solution([1, 3, 6, 10, 15]) == expected


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    expected = [[-14, -10], [19, 23], [23, 27]]
    assert solution([3, 8, -10, 23, 19, -4, -14, 27]) == expected
