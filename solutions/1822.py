class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if len(diff) >= 3:
                    return False
                if not diff:
                    diff.append((s1[i], s2[i]))
                else:
                    diff.append((s2[i], s1[i]))
        return not diff or (len(diff) == 2 and diff[0] == diff[1])


def test_1():
    assert Solution().areAlmostEqual("bank", "kanb") == True


def test_2():
    assert Solution().areAlmostEqual("attack", "defend") == False


def test_3():
    assert Solution().areAlmostEqual("kelb", "kelb") == True


def test_4():
    assert Solution().areAlmostEqual("batkn", "kanbt") == False


def test_5():
    assert Solution().areAlmostEqual("qweabcd", "qefabcd") == False


def test_6():
    assert Solution().areAlmostEqual("aa", "ac") == False
