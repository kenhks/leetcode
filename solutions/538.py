from typing import Optional, Tuple

import pytest

from data_structures import TreeNode
from utils import create_Tree, get_Tree_values, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree
    """

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode, greater_sum) -> Tuple[int, int]:
            left_sum = right_sum = 0
            tmp = node.val
            if node.right:
                right_sum = dfs(node.right, greater_sum)
            node.val += right_sum + greater_sum
            if node.left:
                left_sum = dfs(node.left, node.val)
            return tmp + left_sum + right_sum

        if root:
            dfs(root, 0)
        return root


class Solution2:
    """
    DFS, Recursive rightmost traversal
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree
    """

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        c_sum = 0

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            nonlocal c_sum
            dfs(node.right)
            tmp = node.val
            node.val += c_sum
            c_sum += tmp
            dfs(node.left)

        dfs(root)
        return root


class Solution3:
    """
    DFS, Iterative rightmost traversal
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        c_sum = 0
        nodes = [root] if root else []
        while nodes:
            node = nodes.pop()
            while node.right:
                nodes.append(node)
                node = node.right
            while not node.left and nodes:
                node.val += c_sum
                c_sum = node.val
                node = nodes.pop()
            node.val += c_sum
            c_sum = node.val
            if node.left:
                nodes.append(node.left)
        return root


solutions = parametrize_solution_cls(
    [
        # Solution,
        # Solution2,
        Solution3,
    ],
    "convertBST",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    actual = solution(root)
    assert get_Tree_values(actual) == [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([0, None, 1])
    actual = solution(root)
    assert get_Tree_values(actual) == [1, None, 1]
