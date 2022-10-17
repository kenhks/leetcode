from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, parametrize_solution_cls


class Solution:
    """
    Use hashmap to store object id
    Time Complexity: O(m + n)
    Space Complexity: O(n)
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ans = None
        seen_ids = set()
        while headA is not None:
            seen_ids.add(id(headA))
            headA = headA.next
        while headB is not None:
            if id(headB) in seen_ids:
                ans = headB
                break
            headB = headB.next
        return ans


class Solution2:
    """
    Chain the list together
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "getIntersectionNode",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    skipA, skipB = 2, 3  # noqa
    intersection_head = create_LinkedList(listA[skipA:])
    headA, tailA = create_LinkedList(listA, return_tail=True)
    headB, tailB = create_LinkedList(listB, return_tail=True)
    tailA.next = tailB.next = intersection_head
    result_node = solution(headA, headB)
    assert result_node == intersection_head


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    listA = [1, 9, 1, 2, 4]
    listB = [3, 2, 4]
    skipA, skipB = 3, 1  # noqa
    intersection_head = create_LinkedList(listA[skipA:])
    headA, tailA = create_LinkedList(listA, return_tail=True)
    headB, tailB = create_LinkedList(listB, return_tail=True)
    tailA.next = tailB.next = intersection_head
    result_node = solution(headA, headB)
    assert result_node == intersection_head


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    listA = [2, 6, 4]
    listB = [1, 5]
    skipA, skipB = 3, 2  # noqa
    intersection_head = create_LinkedList(listA[skipA:])
    headA, tailA = create_LinkedList(listA, return_tail=True)
    headB, tailB = create_LinkedList(listB, return_tail=True)
    tailA.next = tailB.next = intersection_head
    result_node = solution(headA, headB)
    assert result_node == intersection_head
