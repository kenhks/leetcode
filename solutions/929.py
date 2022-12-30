from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashset
    Time Complexity: O(s)
    Space Complexity: O(n)
    s = the total nubmer of characters
    """

    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for i in emails:
            local_name, domain_name = i.split("@")
            real_local_name = f"{domain_name}@"
            for c in local_name:
                if c == "+":
                    break
                elif c != ".":
                    real_local_name += c
            email_set.add(real_local_name)
        return len(email_set)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "numUniqueEmails",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    assert solution(emails) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    assert solution(emails) == 3
