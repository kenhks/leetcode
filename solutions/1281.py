from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = [int(i) for i in str(n)]
        return reduce(lambda x, y: x * y, str_n) - sum(str_n)


class Solution2:
    def subtractProductAndSum(self, n: int) -> int:
        product, sum = 1, 0
        while n > 0:
            digit_value = n % 10
            sum += digit_value
            product *= digit_value
            print(n, digit_value, sum, product, n / 10)
            n = n // 10
        return product - sum


def test_1():
    assert Solution2().subtractProductAndSum(234) == 15


def test_2():
    assert Solution2().subtractProductAndSum(4421) == 21
