class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrpyted_s = ""
        a_ord_offset = ord("a") - 1
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                decrpyted_s += chr(int(s[i : i + 2]) + a_ord_offset)
                i += 3
            else:
                decrpyted_s += chr(int(s[i]) + a_ord_offset)
                i += 1
        return decrpyted_s


def test_1():
    assert Solution().freqAlphabets("10#11#12") == "jkab"


def test_2():
    assert Solution().freqAlphabets("1326#") == "acz"
