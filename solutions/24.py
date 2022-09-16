from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Iterative with dummy node
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(-1, head)
        while head and head.next:
            prev.next = head.next
            head.next = head.next.next
            prev.next.next = head
            prev, head = head, head.next
        return dummy.next


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "swapPairs",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head_node = create_LinkedList([1, 2, 3, 4])
    result_node = solution(head_node)
    assert get_LinkedList_values(result_node) == [2, 1, 4, 3]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head_node = create_LinkedList([])
    result_node = solution(head_node)
    assert get_LinkedList_values(result_node) == []


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head_node = create_LinkedList([1])
    result_node = solution(head_node)
    assert get_LinkedList_values(result_node) == [1]
