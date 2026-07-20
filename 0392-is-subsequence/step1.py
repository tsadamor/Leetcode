class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        else:
            return False


def main() -> None:
    s = "oho"
    t = ""
    
    Solver = Solution()
    res = Solver.isSubsequence(s, t)
    print(res)

if __name__ == "__main__":
    main()