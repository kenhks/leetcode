from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Iterative with two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "removeNthFromEnd",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head_node = create_LinkedList([1, 2, 3, 4, 5])
    result_node = solution(head_node, 2)
    assert get_LinkedList_values(result_node) == [1, 2, 3, 5]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head_node = create_LinkedList([1, 2])
    result_node = solution(head_node, 1)
    assert get_LinkedList_values(result_node) == [1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head_node = create_LinkedList([1])
    result_node = solution(head_node, 1)
    assert get_LinkedList_values(result_node) == []
