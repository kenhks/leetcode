from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Merge and Sort
    Time Complexity: O((m + n)log(2, m + n)) = (m + n)log(2, m + n) + m + n
    Space Complexity: O(1)
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n > 0:
            for j in nums2:
                nums1[m] = j
                m += 1
            nums1.sort()


class Solution2:
    """
    Two pointer, merge from end
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n > 0:
            m -= 1
            n -= 1
            for i in range(len(nums1) - 1, -1, -1):
                if m >= 0 and n >= 0:
                    if nums1[m] >= nums2[n]:
                        nums1[i] = nums1[m]
                        m -= 1
                    else:
                        nums1[i] = nums2[n]
                        n -= 1
                elif n >= 0:
                    nums1[i] = nums2[n]
                    n -= 1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "merge",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums1, m = [1, 2, 3, 0, 0, 0], 3
    nums2, n = [2, 5, 6], 3
    solution(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums1, m = [1], 1
    nums2, n = [], 0
    solution(nums1, m, nums2, n)
    assert nums1 == [1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums1, m = [0], 0
    nums2, n = [1], 1
    solution(nums1, m, nums2, n)
    assert nums1 == [1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    nums1, m = [1, 3, 5, 7, 0, 0, 0, 0], 4
    nums2, n = [2, 4, 6, 8], 4
    solution(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    nums1, m = [5, 6, 7, 8, 0, 0, 0, 0], 4
    nums2, n = [1, 2, 3, 4], 4
    solution(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 6, 7, 8]
