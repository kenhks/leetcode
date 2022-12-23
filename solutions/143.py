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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_stack = []
        node = head
        while node:
            node_stack.append(node)
            node = node.next
        prev = node_stack[0]
        i, j = 0, len(node_stack) - 1
        while i < j:
            prev.next = node_stack[j]
            node_stack[j].next = node_stack[i + 1]
            prev = node_stack[i + 1]
            i += 1
            j -= 1
        prev.next = None


class Solution2:
    """
    Reverse Linked List from middle
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        pre, slow.next, slow = None, None, slow.next
        while slow:
            slow.next, pre, slow = pre, slow, slow.next
        while head and pre:
            head.next, head, pre.next, pre = pre, head.next, head.next, pre.next


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "reorderList",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head = create_LinkedList([1, 2, 3, 4])
    solution(head)
    assert get_LinkedList_values(head) == [1, 4, 2, 3]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head = create_LinkedList([1, 2, 3, 4, 5])
    solution(head)
    assert get_LinkedList_values(head) == [1, 5, 2, 4, 3]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head = create_LinkedList([1])
    solution(head)
    assert get_LinkedList_values(head) == [1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    head = create_LinkedList([1, 2])
    solution(head)
    assert get_LinkedList_values(head) == [1, 2]
