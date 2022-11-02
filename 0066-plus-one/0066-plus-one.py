class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        l = len(digits)
        
        for i,elm in enumerate(digits):
            num += elm * (10**(l - i - 1))
        
        return [int(i) for i in str(num+1) ]
        
        