from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, create_LinkedListCycle, parametrize_solution_cls


class Solution:
    """
    Two Pointer: fast and slow
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "hasCycle",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head_node = create_LinkedListCycle([3, 2, 0, -4], (-1, 1))
    assert solution(head_node)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head_node = create_LinkedListCycle([1, 2], (-1, 0))
    assert solution(head_node)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head_node = create_LinkedList([1])
    assert not solution(head_node)
