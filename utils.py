from typing import List, Optional

from data_structures import ListNode, TreeNode


def create_LinkedList(nums: List) -> Optional[ListNode]:
    if not nums:
        return None
    prev_node = head = ListNode(nums[0])
    for i in nums[1:]:
        prev_node.next = ListNode(i)
        prev_node = prev_node.next
    return head


def get_LinkedList_values(node: ListNode) -> List:
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def create_Tree(nums: List) -> Optional[TreeNode]:
    if not nums:
        return None
    nodes = [TreeNode(i) if i is not None else None for i in nums]
    for i, node in enumerate(nodes):
        if not node:
            continue
        left_index = 2 * i + 1
        if left_index < len(nodes):
            node.left = nodes[left_index]
        left_index = 2 * i + 1
        right_index = left_index + 1
        if right_index < len(nodes):
            node.right = nodes[right_index]
    return nodes[0]


def get_Tree_values(root: TreeNode) -> List:
    level_nodes = [root]
    values = []
    while any(i is not None for i in level_nodes):
        values.extend([i.val if i is not None else None for i in level_nodes])
        new_level_nodes = []
        for n in level_nodes:
            if n:
                new_level_nodes.append(n.left)
                new_level_nodes.append(n.right)
            else:
                new_level_nodes.append(None)
                new_level_nodes.append(None)
        level_nodes = new_level_nodes
    return values


def create_function(cls, func_name):
    def _func(*args, **kwargs):
        return getattr(cls(), func_name)(*args, **kwargs)

    _func.__name__ = cls.__name__
    return _func


def parametrize_solution_cls(sol_cls_list: List, sol_func_name):
    return [create_function(sol_cls, sol_func_name) for sol_cls in sol_cls_list]
