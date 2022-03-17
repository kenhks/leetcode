from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def possible_chars(char):
            if char.isdigit():
                return [char]
            elif char.isalpha():
                return [char.lower(), char.upper()]

        result = [[]]
        for char in s:
            chars = possible_chars(char)
            if len(chars) == 1:
                result = [i + chars for i in result]
            elif len(chars) == 2:
                result = [i + chars[:1] for i in result] + [
                    i + chars[1:] for i in result
                ]
        result = ["".join(i) for i in result]
        return result


def test_1():
    expected = [
        "a1b2",
        "a1B2",
        "A1b2",
        "A1B2",
    ]
    assert sorted(Solution().letterCasePermutation("a1b2")) == sorted(expected)


def test_2():
    expected = [
        "3z4",
        "3Z4",
    ]
    assert sorted(Solution().letterCasePermutation("3z4")) == sorted(expected)
