from typing import Optional

import pytest

from data_structures import ListNode
from utils import create_LinkedList, parametrize_solution_cls


class Solution:
    """
    Convert linked list to array, check with two pointer
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution2:
    """
    Reverse second half of linked list, check with two pointer
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            prev_slow, slow = slow, slow.next
        prev_slow.next = None
        mid_node = slow
        while slow:
            next_node = slow.next
            slow.next = prev_slow
            prev_slow = slow
            slow = next_node
        mid_node.next = None
        end = prev_slow
        while head and end:
            if head.val != end.val:
                return False
            head, end = head.next, end.next
        return True


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "isPalindrome",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head_node = create_LinkedList([1, 2, 2, 1])
    assert solution(head_node)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head_node = create_LinkedList([1, 2])
    assert not solution(head_node)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    head_node = create_LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
    assert solution(head_node)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    head_node = create_LinkedList([1])
    assert solution(head_node)
