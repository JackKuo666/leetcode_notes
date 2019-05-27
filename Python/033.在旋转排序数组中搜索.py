class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 法1.二分法：将所有可能在mid左边的情况列举出来 O(logn)
        """
        Only three cases when we need to choose the left part (m = (left + right + 1) // 2):
            left = 0, m = 3, right = 6
            [4,5,6,7,0,1,2] target 5: nums[left] <= target <= nums[m]
            [6,7,0,1,2,4,5] target 7: nums[m] <= nums[left] <= target
            [6,7,0,1,2,4,5] target 0: target <= nums[m] <= nums[left]
        """
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             m = (left + right + 1) // 2
#             if nums[m] == target:
#                 return m
#             elif nums[m] <= nums[left] <= target or nums[left] <= target <= nums[m] or target <= nums[m] <= nums[left]:
#                 right = m - 1
#             else:
#                 left = m + 1
#         return -1
    
        # 法2.二分法：常规操作 O(logn)
        if not nums:
            return -1
        
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high + 1) // 2
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        
