class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 法1.暴力遍历法
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [-1, -1]
        
        # 法2.hashmap
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i
        return [-1, -1]
        
        # 法3.sort and 两个指针
#         new_nums = [(v, index) for index, v in enumerate(nums)]
#         new_nums.sort()
#         left, right = 0, len(nums) - 1
#         while left < right:
#             if new_nums[left][0] + new_nums[right][0] < target:
#                 left += 1
#             elif new_nums[left][0] + new_nums[right][0] > target:
#                 right -= 1
#             else:
#                 return [new_nums[left][1], new_nums[right][1]]
#         return [-1, -1]
                
                
                
