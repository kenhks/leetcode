import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS with recursion
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def goodNodes(self, root: TreeNode) -> int:
        good_count = 1

        def get_good_count(node: TreeNode, path_max: int) -> int:
            c = 1 if node.val >= path_max else 0
            if node.left:
                c += get_good_count(node.left, max(node.val, path_max))
            if node.right:
                c += get_good_count(node.right, max(node.val, path_max))
            return c

        if root.left:
            good_count += get_good_count(root.left, root.val)
        if root.right:
            good_count += get_good_count(root.right, root.val)
        return good_count


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "goodNodes",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([3, 1, 4, 3, None, 1, 5])
    assert solution(root) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([3, 3, None, 4, 2])
    assert solution(root) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root) == 1
