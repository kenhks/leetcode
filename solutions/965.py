from collections import deque
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

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(node: TreeNode):
            nonlocal ans
            if ans:
                if node.val == root.val:
                    if node.left:
                        dfs(node.left)
                    if node.right:
                        dfs(node.right)
                else:
                    ans = False

        if root:
            dfs(root)
        return ans


class Solution2:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        ans = True
        stack = deque([root]) if root else []
        while stack and ans:
            for _ in range(len(stack)):
                node = stack.popleft()
                if node.val != root.val:
                    ans = False
                    break
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "isUnivalTree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 1, 1, 1, 1, None, 1])
    assert solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([2, 2, 2, 5, 2])
    assert not solution(root)
