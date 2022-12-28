import heapq
from typing import List
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n + klog(2, n))
    Space Complexity: O(n)
    """

    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)
        for _ in range(k):
            curr = -heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))
        return -sum(heap)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minStoneSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(piles=[5, 4, 9], k=2) == 12


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(piles=[4, 3, 6, 7], k=3) == 12
