import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use hashmap counter
    Time Complexity: O(n) = 3n
    Space Complexity: O(n) = 2n
    """

    def findTheDifference(self, s: str, t: str) -> str:
        count_s = {}
        count_t = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            if char not in count_s:
                return char
            count_t[char] = count_t.get(char, 0) + 1
        for char in count_t:
            if count_t[char] != count_s[char]:
                return char


class Solution2:
    """
    Sort
    Time Complexity: O(n log(2, n)) = 2nlog(2, n) + 2n
    Space Complexity: O(1)
    """

    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i, j in zip(s, t):
            if i != j:
                return j
        return t[-1]


class Solution3:
    """
    Calculate relative offset of ascii value
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for i, j in zip(s, t):
            ans += ord(j) - ord(i)
        ans += ord(t[-1])
        return chr(ans)


class Solution4:
    """
    Use bitwise xor to find unique of ascii value
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for i, j in zip(s, t):
            ans ^= ord(i) ^ ord(j)
        ans ^= ord(t[-1])
        return chr(ans)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
        Solution4,
    ],
    "findTheDifference",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abcd", "abcde") == "e"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("", "y") == "y"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("a", "aa") == "a"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    s1 = "".join(
        [
            "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvt",
            "pyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvl",
            "fwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfw",
            "bvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjld",
            "prwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdox",
            "ohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxc",
            "zcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypx",
            "idkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozof",
            "ncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrr",
            "ymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweef",
            "cwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwy",
            "fzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaaua",
            "zfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszj",
            "ywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxv",
            "qrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcr",
            "ibumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvak",
            "xgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnf",
            "bgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfulua",
            "qbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpva",
            "surraqfkcmxhdapjrlrnkbklwkrvoaziznlpor",
        ]
    )
    s2 = "".join(
        [
            "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxb",
            "ufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbc",
            "jhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxh",
            "dvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwes",
            "axsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgr",
            "rfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqpt",
            "rmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhq",
            "usvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrke",
            "czjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfn",
            "etekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkris",
            "rlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdq",
            "gvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawv",
            "kivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqk",
            "jjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyi",
            "mkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqsz",
            "uwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpih",
            "avligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorud",
            "ayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzja",
            "etahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnk",
            "aiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj",
        ]
    )
    assert solution(s1, s2) == "t"
