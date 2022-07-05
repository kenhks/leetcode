from typing import List

from data_structures import ListNode


def create_LinkedList(nums: List) -> ListNode:
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


def create_function(cls, func_name):
    return getattr(cls(), func_name)


def parametrize_solution_cls(sol_cls_list: List, sol_func_name):
    return [
        lambda *args, **kwargs: (
            create_function(sol_cls, sol_func_name)(*args, **kwargs)
        )
        for sol_cls in sol_cls_list
    ]
