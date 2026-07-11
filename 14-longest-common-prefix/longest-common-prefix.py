class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        start = strs[0]
        end = strs[-1]
        i=0
        while i < len(start) and start[i]==end[i]:
            i+=1
        return start[:i]    
