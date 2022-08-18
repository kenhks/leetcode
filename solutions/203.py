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

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy_head = ListNode(-1)
        dummy_head.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next


class Solution2:
    """
    Iterative with dummy node, two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = dummy_head = ListNode(-1)
        dummy_head.next = head
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy_head.next


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "removeElements",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head_node = create_LinkedList([1, 2, 6, 3, 4, 5, 6])
    result_node = solution(head_node, 6)
    assert get_LinkedList_values(result_node) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head_node = create_LinkedList([])
    result_node = solution(head_node, 1)
    assert get_LinkedList_values(result_node) == []


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head_node = create_LinkedList([7, 7, 7, 7])
    result_node = solution(head_node, 7)
    assert get_LinkedList_values(result_node) == []
