class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        l = len(x_string)
        l,r = 0,l-1
        
        while l < r:
            if x_string[l] == x_string[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        