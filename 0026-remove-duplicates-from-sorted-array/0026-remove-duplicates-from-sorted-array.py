class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        already_found = set()
        p = 0
        count = 0
        while p < len(nums):
            if nums[p] not in already_found:
                already_found.add(nums[p])
                p += 1
                count += 1
            else:
                del nums[p]
        return count
                

                
        
        