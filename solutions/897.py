import pytest

from data_structures import TreeNode
from utils import create_Tree, get_Tree_values, parametrize_solution_cls


class Solution:
    """
    DFS, Inorder Traversal
    Time Complexity: O(n) = 2n
    Space Complexity: O(n) = n + h
    h = height of tree ~= log(2, n)
    """

    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)
            nodes.append(node)
            if node.right:
                dfs(node.right)
            node.left = None
            node.right = None

        if root:
            dfs(root)
            root = node = nodes[0]
            for next_node in nodes[1:]:
                node.right = next_node
                node = next_node
        return root


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "increasingBST",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
    assert get_Tree_values(solution(root)) == [
        1,
        None,
        2,
        None,
        3,
        None,
        4,
        None,
        5,
        None,
        6,
        None,
        7,
        None,
        8,
        None,
        9,
    ]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([5, 1, 7])
    assert get_Tree_values(solution(root)) == [1, None, 5, None, 7]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert get_Tree_values(solution(root)) == [1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    root = create_Tree([2, 1, 4, None, None, 3])
    assert get_Tree_values(solution(root)) == [1, None, 2, None, 3, None, 4]
