import pytest

from utils import create_LinkedList, get_LinkedList_values, parametrize_solution_cls


class Solution:
    """
    Delete the next node of target node
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def deleteNode(self, node):
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        del next_node


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "deleteNode",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    head = create_LinkedList([4, 5, 1, 9])
    solution(head)
    assert get_LinkedList_values(head) == [5, 1, 9]
