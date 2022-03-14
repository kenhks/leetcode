from data_structures import ListNode
from utils import create_LinkedList


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        while head:
            value = value * 2 + head.val
            head = head.next
        return value


class Solution2:
    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        while head:
            value = (value << 1) | head.val
            head = head.next
        return value


def test_1():
    head = create_LinkedList([1, 0, 1])
    assert Solution().getDecimalValue(head) == 5


def test_2():
    head = create_LinkedList([0])
    assert Solution().getDecimalValue(head) == 0


def test_3():
    head = create_LinkedList([1, 0, 1])
    assert Solution2().getDecimalValue(head) == 5


def test_4():
    head = create_LinkedList([0])
    assert Solution2().getDecimalValue(head) == 0
