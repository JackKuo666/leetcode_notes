class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         count = 0
#         tmp = nums[0]
#         for i in range(1, len(nums)):      # 注意1.这道题的nums大小是变化的，不能用for循环，得用while
#             if tmp == nums[i]:
#                 nums.pop(i)                # 注意2.这道题的nums大小是变化的，不能用pop，得用del
#                 continue
#             else:
#                 count += 1
#                 tmp = nums[i]
                
#         return nums
            
    
        # 法1. del 法
        i = 0
        
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
                i -= 1
            i += 1
            
        return len(nums)
