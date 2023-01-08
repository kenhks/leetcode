import collections
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort two list and search with two Pointer
    Time Complexity: O(mlog(2, m) + nlog(2, n)) = mlog(2, m) + nlog(2, n) + m + n
    Space Complexity: O(m + n)
    m = len(nums1), n = len(nums2)
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


class Solution2:
    """
    Counter
    Time Complexity: O(m + n)
    Space Complexity: O(m)
    m = len(nums1), n = len(nums2)
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_count = {}
        for i in nums1:
            if i in nums1_count:
                nums1_count[i] += 1
            else:
                nums1_count[i] = 1
        for j in nums2:
            if j in nums1_count:
                if nums1_count[j] > 0:
                    result.append(j)
                    nums1_count[j] -= 1
        return result


class Solution3:
    """
    Python Built-in
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    m = len(nums1), n = len(nums2)
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "intersect",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert solution(nums1, nums2) == [2, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert sorted(solution(nums1, nums2)) == [4, 9]
