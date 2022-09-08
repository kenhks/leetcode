from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def tree2str(self, root: Optional[TreeNode]) -> str:
        def append_nodes(node: TreeNode):
            if not (node.left or node.right):
                return f"({node.val})"
            if node.left:
                left_str = append_nodes(node.left)
            else:
                left_str = "()"
            if node.right:
                right_str = append_nodes(node.right)
            else:
                right_str = ""
            return f"({node.val}{left_str}{right_str})"

        return append_nodes(root)[1:-1]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "tree2str",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 3, 4])
    assert solution(root) == "1(2(4))(3)"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2, 3, None, 4])
    assert solution(root) == "1(2()(4))(3)"
