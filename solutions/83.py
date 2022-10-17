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

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head.next
        while fast is not None:
            if fast.val == slow.val:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return head


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "deleteDuplicates",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head_node = create_LinkedList([1, 1, 2])
    result_node = solution(head_node)
    assert get_LinkedList_values(result_node) == [1, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head_node = create_LinkedList([1, 1, 2, 3, 3])
    result_node = solution(head_node)
    assert get_LinkedList_values(result_node) == [1, 2, 3]
