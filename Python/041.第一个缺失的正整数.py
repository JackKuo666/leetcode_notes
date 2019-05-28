class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 法1.使用in xrange()
#         if not nums:
#             return 1
#         for i in xrange(1, max(max(nums) + 2, 2)):  # 注意 这里要使用xrange()，返回生成器；不能使用range(),会超出内存
#             if i not in nums:
#                 return i
        
        # 法2.使用in 计数    
        # index = 1
        # while True:
        #     if index not in nums:
        #         return index
        #     else:
        #         index += 1
        
        # 法3.# O(n) time
        """
        解析见：https://www.cnblogs.com/clnchanpin/p/6727065.html
        """
        for i in xrange(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in xrange(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

        # 法4. O(nlgn) time
        # nums.sort()
        # res = 1
        # for num in nums:
        #     if num == res:
        #         res += 1
        # return res
