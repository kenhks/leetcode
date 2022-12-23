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

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: TreeNode):
            nonlocal ans
            if not node.left and not node.right:
                ans += node.val
            else:
                if node.left:
                    node.left.val += node.val << 1
                    dfs(node.left)
                if node.right:
                    node.right.val += node.val << 1
                    dfs(node.right)

        if root:
            dfs(root)
        return ans


class Solution2:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = deque([root]) if root else []
        while stack:
            for _ in range(len(stack)):
                node = stack.popleft()
                if not node.left and not node.right:
                    ans += node.val
                else:
                    if node.left:
                        node.left.val += node.val << 1
                        stack.append(node.left)
                    if node.right:
                        node.right.val += node.val << 1
                        stack.append(node.right)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "sumRootToLeaf",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 0, 1, 0, 1, 0, 1])
    assert solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([0])
    assert solution(root) == 0
