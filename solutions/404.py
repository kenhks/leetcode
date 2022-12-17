from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    BFS
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_sum = 0
        nodes = [root] if root and root.left else []
        while nodes:
            next_nodes = []
            for i in nodes:
                if i.left:
                    if i.left.left is None and i.left.right is None:
                        left_sum += i.left.val
                    next_nodes.append(i.left)
                if i.right:
                    next_nodes.append(i.right)
            nodes = next_nodes
        return left_sum


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "sumOfLeftLeaves",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([3, 9, 20, None, None, 15, 7])
    assert solution(root) == 24


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2, 3])
    assert solution(root) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root) == 0
