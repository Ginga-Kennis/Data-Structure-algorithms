class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        l = len(digits)
        
        for i,elm in enumerate(digits):
            num += elm * (10**(l - i - 1))
            
        num += 1
        output = []
        for _ in range(len(str(num))):
            output.append(num % 10)
            num = num//10
            
        return reversed(output)
        
        