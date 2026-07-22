class Solution:
    def firstUniqChar(self, s: str) -> int:
        appearences: dict[str, int] = {}
        
        for c in s:
            if c in appearences:
                appearences[c] += 1
            else:
                appearences[c] = 1
                
        for c in s:
            if appearences[c] == 1:
                return s.index(c)
        
        return -1
    

def main() -> None:
    Solver = Solution()
    s = "loveleetcode"
    res = Solver.firstUniqChar(s)
    print(res)
    

if __name__ == "__main__":
    main()