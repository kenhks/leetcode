from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Two pointer, fast and slow
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "middleNode",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head_node = create_LinkedList([1, 2, 3, 4, 5])
    result_node = solution(head_node)
    assert get_LinkedList_values(result_node) == [3, 4, 5]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head_node = create_LinkedList([1, 2, 3, 4, 5, 6])
    result_node = solution(head_node)
    assert get_LinkedList_values(result_node) == [4, 5, 6]
