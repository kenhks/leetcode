from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use hashmap to check exchange pair exists
    Time Complexity: O(m+n)
    Space Complexity: O(m+n)
    m = len(aliceSizes)
    n = len(bobSizes)
    """

    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        answer = []
        alice_box_set = set()
        bob_box_set = set()
        alice_sum = bob_sum = 0
        for a_size in aliceSizes:
            alice_box_set.add(a_size)
            alice_sum += a_size
        for b_size in bobSizes:
            bob_box_set.add(b_size)
            bob_sum += b_size
        half = (alice_sum - bob_sum) // 2
        for i in alice_box_set:
            expected_b_size = i - half
            if expected_b_size in bob_box_set:
                answer = [i, expected_b_size]
                break
        return answer


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "fairCandySwap",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    aliceSizes = [1, 1]
    bobSizes = [2, 2]
    assert solution(aliceSizes, bobSizes) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    aliceSizes = [1, 2]
    bobSizes = [2, 3]
    assert solution(aliceSizes, bobSizes) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    aliceSizes = [2]
    bobSizes = [1, 3]
    assert solution(aliceSizes, bobSizes) == [2, 3]
