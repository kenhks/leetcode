from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^3) = ((n + 1) // 2) * (n - ((n + 1) // 2))) * ((n + 1) // 2))
    Space Complexity: O(1)
    """

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_size = len(arr)
        arr_sum = sum(arr)
        for sub_arr_size in range(3, arr_size + 1, 2):
            arr_sum += sum(
                sum(arr[i : i + sub_arr_size])
                for i in range(arr_size)
                if i + sub_arr_size <= arr_size
            )
            sub_arr_size -= 2
        return arr_sum


class Solution2:
    """
    Sum subarray by moving sum
    Time Complexity: O(n^2) = ((n + 1) // 2) * (n - ((n + 1) // 2)))
    Space Complexity: O(1)
    """

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_sum = sum(arr)
        for sub_arr_size in range(3, len(arr) + 1, 2):
            sub_arr_sum = sum(arr[:sub_arr_size])
            arr_sum += sub_arr_sum
            for i in range(sub_arr_size, len(arr)):
                sub_arr_sum += arr[i] - arr[i - sub_arr_size]
                arr_sum += sub_arr_sum
        return arr_sum


class Solution3:
    """
    Math, sum by freq formula
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i, x in enumerate(arr):
            ans += x * ((i + 1) * (n - i) + 1) // 2
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "sumOddLengthSubarrays",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 4, 2, 5, 3]) == 58


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 2]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([10, 11, 12]) == 66


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    arr = list(range(1, 13))  # 1 - 12
    assert solution(arr) == 1183
