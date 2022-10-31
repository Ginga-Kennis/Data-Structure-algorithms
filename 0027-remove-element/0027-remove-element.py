class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        k = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
                k += 1
        return k
                
        