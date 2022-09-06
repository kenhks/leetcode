from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Iterative, merge in place
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    m = len(list1), n = len(list2)
    """

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not (list1 and list2):
            return list1 or list2
        cnode = head = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                cnode.next = list2
                list2 = list2.next
                cnode = cnode.next
            elif list1.val < list2.val:
                cnode.next = list1
                list1 = list1.next
                cnode = cnode.next
            else:
                cnode.next, list1 = list1, list1.next
                cnode.next.next, list2 = list2, list2.next
                cnode = cnode.next.next
        if list1:
            cnode.next = list1
        if list2:
            cnode.next = list2
        return head.next


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "mergeTwoLists",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    node1 = create_LinkedList([1, 2, 4])
    node2 = create_LinkedList([1, 3, 4])
    assert get_LinkedList_values(solution(node1, node2)) == [1, 1, 2, 3, 4, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    node1 = create_LinkedList([])
    node2 = create_LinkedList([])
    assert get_LinkedList_values(solution(node1, node2)) == []


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    node1 = create_LinkedList([])
    node2 = create_LinkedList([0])
    assert get_LinkedList_values(solution(node1, node2)) == [0]
