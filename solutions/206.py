from platform import node
from typing import Optional

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node


def test_1():
    head = create_LinkedList([1, 2, 3, 4, 5])
    result = Solution().reverseList(head)
    assert get_LinkedList_values(result) == [5, 4, 3, 2, 1]


def test_2():
    head = create_LinkedList([1, 2])
    result = Solution().reverseList(head)
    assert get_LinkedList_values(result) == [2, 1]


def test_3():
    head = create_LinkedList([])
    result = Solution().reverseList(head)
    assert get_LinkedList_values(result) == []
