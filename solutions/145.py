from collections import deque
from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = the height of tree
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            ans.append(node.val)

        if root:
            dfs(root)
        return ans


class Solution2:
    """
    DFS, Iterative with stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = deque([(0, root)]) if root else []
        while stack:
            checked, node = stack.pop()
            if not checked:
                stack.append((1, node))
                if node.right:
                    stack.append((0, node.right))
                if node.left:
                    stack.append((0, node.left))
            else:
                ans.append(node.val)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "postorderTraversal",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, None, 2, 3])
    assert solution(root) == [3, 2, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([])
    assert solution(root) == []


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root) == [1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    root = create_Tree([2, 4, 5, 9, None, 6, 7])
    assert solution(root) == [9, 4, 6, 7, 5, 2]
