class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 法1.二分法 O(logn) and O(1)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

        
                
