from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Directly Iterative
    m = len(l1), n = len(l2)
    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n)) = max(m,n) + 1
    """

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        head = curr = ListNode(0)
        while l1 or l2 or carry:
            node_value = carry
            if l1:
                node_value += l1.val
                l1 = l1.next
            if l2:
                node_value += l2.val
                l2 = l2.next
            if node_value >= 10:
                carry = 1
                node_value -= 10
            else:
                carry = 0
            curr.next = ListNode(node_value)
            curr = curr.next
        return head.next


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "addTwoNumbers",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    node1 = create_LinkedList([2, 4, 3])
    node2 = create_LinkedList([5, 6, 4])
    assert get_LinkedList_values(solution(node1, node2)) == [7, 0, 8]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    node1 = create_LinkedList([0])
    node2 = create_LinkedList([0])
    assert get_LinkedList_values(solution(node1, node2)) == [0]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    node1 = create_LinkedList([9, 9, 9, 9, 9, 9, 9])
    node2 = create_LinkedList([9, 9, 9, 9])
    assert get_LinkedList_values(solution(node1, node2)) == [8, 9, 9, 9, 0, 0, 0, 1]
