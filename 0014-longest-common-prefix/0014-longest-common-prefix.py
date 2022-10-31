class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l_min = len(strs[0])
        min_string = strs[0]
        for string in strs:
            if len(string) <= l_min:
                l_min = len(string)
                min_string = string
        res = ""
        for i in range(l_min):
            for s in strs:
                if s[i] != min_string[i]:
                    return res
            res += min_string[i]
        return res
                
            
            
        