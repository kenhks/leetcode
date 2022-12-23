from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False

        def search(node: TreeNode):
            nonlocal ans
            if not ans:
                if node.val == subRoot.val:
                    ans = check_equal(node, subRoot)
                if node.left:
                    search(node.left)
                if node.right:
                    search(node.right)

        def check_equal(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            elif node1 and node2:
                return (
                    node1.val == node2.val
                    and check_equal(node1.left, node2.left)
                    and check_equal(node1.right, node2.right)
                )
            else:
                return False

        search(root)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isSubtree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([3, 4, 5, 1, 2])
    subRoot = create_Tree([4, 1, 2])
    assert solution(root, subRoot)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = create_Tree([4, 1, 2])
    assert not solution(root, subRoot)
