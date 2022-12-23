from collections import deque
from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, get_Tree_values, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            new = TreeNode(root1.val + root2.val)
            new.left = self.mergeTrees(root1.left, root2.left)
            new.right = self.mergeTrees(root1.right, root2.right)
            return new
        else:
            return root1 or root2


class Solution2:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root1.val += root2.val
            stack = deque([(root1, root2)])
            while stack:
                for _ in range(len(stack)):
                    node1, node2 = stack.popleft()
                    if node1 or node2:
                        if node1.left and node2.left:
                            stack.append((node1.left, node2.left))
                            node1.left.val += node2.left.val
                        elif node2.left:
                            node1.left = node2.left
                        if node1.right and node2.right:
                            stack.append((node1.right, node2.right))
                            node1.right.val += node2.right.val
                        elif node2.right:
                            node1.right = node2.right
        return root1 or root2


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "mergeTrees",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root1 = create_Tree([1, 3, 2, 5])
    root2 = create_Tree([2, 1, 3, None, 4, None, 7])
    assert get_Tree_values(solution(root1, root2)) == [3, 4, 5, 5, 4, None, 7]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root1 = create_Tree([1])
    root2 = create_Tree([1, 2])
    assert get_Tree_values(solution(root1, root2)) == [2, 2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root1 = create_Tree([])
    root2 = create_Tree([1])
    assert get_Tree_values(solution(root1, root2)) == [1]
