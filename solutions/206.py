from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Reverse Linked List
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        while head:
            head.next, prev_node, head = prev_node, head, head.next
        return prev_node


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "reverseList",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head = create_LinkedList([1, 2, 3, 4, 5])
    result = solution(head)
    assert get_LinkedList_values(result) == [5, 4, 3, 2, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head = create_LinkedList([1, 2])
    result = solution(head)
    assert get_LinkedList_values(result) == [2, 1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head = create_LinkedList([])
    result = solution(head)
    assert get_LinkedList_values(result) == []
