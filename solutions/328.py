from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Store linked list as list
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_node, even_node = head, head.next if head else None
        nodes = [[odd_node], [even_node]]
        while even_node and even_node.next:
            odd_node = even_node.next
            even_node = odd_node.next
            nodes[0].append(odd_node)
            nodes[1].append(even_node)
        for i in range(1, len(nodes[0])):
            nodes[0][i - 1].next = nodes[0][i]
        for i in range(1, len(nodes[1])):
            nodes[1][i - 1].next = nodes[1][i]
        if head:
            nodes[0][-1].next = nodes[1][0]
        return head


class Solution2:
    """
    4 Pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_node = head
        even_head_node = even_node = head.next if head else None
        while even_node and even_node.next:
            next_odd_node, next_even_node = even_node.next, even_node.next.next
            odd_node.next = next_odd_node
            even_node.next = next_even_node
            odd_node = odd_node.next
            even_node = even_node.next
        if head:
            odd_node.next = even_head_node
        return head


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "oddEvenList",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head = create_LinkedList([1, 2, 3, 4, 5])
    solution(head)
    assert get_LinkedList_values(head) == [1, 3, 5, 2, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head = create_LinkedList([2, 1, 3, 5, 6, 4, 7])
    solution(head)
    assert get_LinkedList_values(head) == [2, 3, 6, 7, 1, 5, 4]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head = create_LinkedList([1, 2])
    solution(head)
    assert get_LinkedList_values(head) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    head = create_LinkedList([1])
    solution(head)
    assert get_LinkedList_values(head) == [1]


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    head = create_LinkedList([])
    solution(head)
    assert get_LinkedList_values(head) == []
