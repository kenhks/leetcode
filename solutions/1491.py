from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary, max_salary = 10 ** 6, 1000
        total = 0
        for i in salary:
            if i < min_salary:
                min_salary = i
            if i > max_salary:
                max_salary = i
            total += i
        return (total - min_salary - max_salary) / (len(salary) - 2)


def test_1():
    assert Solution().average([4000, 3000, 1000, 2000]) == 2500


def test_2():
    assert Solution().average([1000, 2000, 3000]) == 2000

def test_3():
    assert Solution().average([1000, 1000, 3000]) == 1000