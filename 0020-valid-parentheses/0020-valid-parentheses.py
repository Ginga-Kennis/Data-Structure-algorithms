class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(","}":"{","]":"["}
        stack = []
        for item in s:
            if item not in dic:
                stack.append(item)
            elif len(stack) != 0 and stack[-1] == dic[item]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
    
        