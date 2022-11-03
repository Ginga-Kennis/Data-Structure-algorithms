class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def bin_to_dec(a:str):
            ans = 0
            l = len(a)
            for i in range(l):
                ans += int(a[i]) * (2**(l-i-1))
            return ans
        
        def dec_to_bin(num:int):
            res = ""
            if num >= 1:
                while num >= 1:
                    res = str(num%2) + res
                    num = num//2
            else:
                return "0"
            return res
             

    
        a_dec,b_dec = bin_to_dec(a),bin_to_dec(b)
        res = a_dec+b_dec
        return dec_to_bin(res)
        
        
        
        
        