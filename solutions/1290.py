import pytest

from data_structures import ListNode
from utils import create_LinkedList, parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        while head:
            value = value * 2 + head.val
            head = head.next
        return value


class Solution2:
    """
    Bitwise Operation
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        while head:
            value = (value << 1) | head.val
            head = head.next
        return value


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "getDecimalValue",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head = create_LinkedList([1, 0, 1])
    assert solution(head) == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    head = create_LinkedList([0])
    assert solution(head) == 0
