class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


class Solution2:
    def toLowerCase(self, s: str) -> str:
        lower_s = ""
        A_ord, Z_ord = ord("A"), ord("Z")
        for char in s:
            if A_ord <= ord(char) <= Z_ord:
                lower_s += chr(ord(char) + 32)
            else:
                lower_s += char
        return lower_s


def test_1():
    assert Solution().toLowerCase("Hello") == "hello"


def test_2():
    assert Solution().toLowerCase("here") == "here"


def test_3():
    assert Solution().toLowerCase("LOVELY") == "lovely"


def test_4():
    assert Solution2().toLowerCase("Hello") == "hello"


def test_5():
    assert Solution2().toLowerCase("here") == "here"


def test_6():
    assert Solution2().toLowerCase("LOVELY") == "lovely"
