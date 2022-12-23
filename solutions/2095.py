from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Scan with stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Do not return anything, modify head in-place instead.
        """
        node_stack = []
        node = head
        while node:
            node_stack.append(node)
            node = node.next
        if len(node_stack) > 2:
            mid = len(node_stack) // 2
            node_stack[mid - 1].next = node_stack[mid + 1]
        elif len(node_stack) == 2:
            head.next = None
        else:
            head = None
        return head


class Solution2:
    """
    Three pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_slow = slow = fast = head
        while fast and fast.next:
            prev_slow, slow, fast = slow, slow.next, fast.next.next
        if fast == head:
            head = None
        elif prev_slow.next and prev_slow.next.next:
            prev_slow.next = prev_slow.next.next
        else:
            prev_slow.next = None
        return head


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "deleteMiddle",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head = create_LinkedList([1, 3, 4, 7, 1, 2, 6])
    assert get_LinkedList_values(solution(head)) == [1, 3, 4, 1, 2, 6]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head = create_LinkedList([1, 2, 3, 4])
    assert get_LinkedList_values(solution(head)) == [1, 2, 4]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head = create_LinkedList([2, 1])
    assert get_LinkedList_values(solution(head)) == [2]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    head = create_LinkedList([1])
    assert get_LinkedList_values(solution(head)) == []
