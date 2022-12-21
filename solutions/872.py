from collections import deque
from itertools import zip_longest
from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, recursive with leaf stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaves = []
        root2_leaves = []

        def dfs(node: TreeNode, stack):
            if not node.left and not node.right:
                stack.append(node.val)
            if node.left:
                dfs(node.left, stack)
            if node.right:
                dfs(node.right, stack)

        dfs(root1, root1_leaves)
        dfs(root2, root2_leaves)
        return root1_leaves == root2_leaves


class Solution2:
    """
    DFS, Iterative with leave stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_values(root: TreeNode) -> List[int]:
            nodes = deque([root])
            while any(isinstance(i, TreeNode) for i in nodes):
                for _ in range(len(nodes)):
                    node = nodes.popleft()
                    if isinstance(node, TreeNode):
                        if not node.left and not node.right:
                            nodes.append(node.val)
                        if node.left:
                            nodes.append(node.left)
                        if node.right:
                            nodes.append(node.right)
                    else:
                        nodes.append(node)
            return nodes
        return get_leaf_values(root1) == get_leaf_values(root2)


class Solution3:
    """
    DFS, Recursive with generator
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from dfs(node.left)
            if node.right:
                yield from dfs(node.right)

        return all(a == b for a, b in zip_longest(dfs(root1), dfs(root2)))


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "leafSimilar",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root1 = create_Tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
    root2 = create_Tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    assert solution(root1, root2)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root1 = create_Tree([1, 2, 3])
    root2 = create_Tree([1, 3, 2])
    assert not solution(root1, root2)
