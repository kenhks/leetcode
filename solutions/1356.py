from collections import defaultdict
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + 32
    Space Complexity: O(n) = 2n
    """

    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_counter = defaultdict(list)
        for i in arr:
            bit_counter[bin(i).count("1")].append(i)
        ans = []
        for bit in sorted(bit_counter.keys()):
            ans.extend(sorted(bit_counter[bit]))
        return ans


class Solution2:
    """
    Hashmap
    Time Complexity: O(nlog(2, n))
    Space Complexity: O(1)
    """

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "sortByBits",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert solution(arr) == [0, 1, 2, 4, 8, 3, 5, 6, 7]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    assert solution(arr) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
