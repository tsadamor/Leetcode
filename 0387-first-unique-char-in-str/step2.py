from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        appearences = Counter(s)
        
        for i, c in enumerate(s):
             if appearences[c] == 1:
                 return i
        
        return -1
    

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        seen_index:dict[str, int] = {}
        duplicated = -1

        for i, c in enumerate(s):
            if c in seen_index:
                seen_index[c] = duplicated
            else:
                seen_index[c] = i

        for idx in seen_index.values():
            if idx != duplicated:
                return idx

        return -1      
