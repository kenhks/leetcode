from typing import Optional

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


def test_1():
    head = create_LinkedList([1, 2, 3, 4, 5])
    result = Solution().middleNode(head)
    assert get_LinkedList_values(result) == [3, 4, 5]


def test_2():
    head = create_LinkedList([1, 2, 3, 4, 5, 6])
    result = Solution().middleNode(head)
    assert get_LinkedList_values(result) == [4, 5, 6]
