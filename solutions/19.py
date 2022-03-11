from typing import Optional

from data_structures import ListNode
from utils import create_LinkedList, get_LinkedList_values


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


def test_1():
    node = create_LinkedList([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(node, 2)
    assert get_LinkedList_values(result) == [1, 2, 3, 5]


def test_2():
    node = create_LinkedList([1, 2])
    result = Solution().removeNthFromEnd(node, 1)
    assert get_LinkedList_values(result) == [1]

def test_3():
    node = create_LinkedList([1, ])
    result = Solution().removeNthFromEnd(node, 1)
    assert get_LinkedList_values(result) == []