class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 法1. 双指针 O(n) and O(1)
        # if not nums:
        #     return [-1,-1]
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     if nums[left] == target and nums[right] == target:
        #         return [left, right]
        #     if nums[left] != target:
        #         left += 1
        #     if nums[right] != target:
        #         right -= 1
        # return [-1, -1]
        
        # 法2.二分法 O(logn) and O(1)
        def binarySearch(nums, target, flag):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right + 1) // 2
                if target > nums[mid] or (flag and target == nums[mid]):
                    left = mid + 1
                else:
                    right = mid - 1
            return right if flag else left
        
        left, right = binarySearch(nums, target, False), binarySearch(nums, target, True)
        return [left, right] if left <= right else [-1, -1]
                    
