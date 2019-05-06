class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 法1.双指针 O(n^2) O(1)
        # max_area = area = 0
        # left, right = 0, len(height) - 1
        # while left < right:
        #     l, r = height[left], height[right]
        #     if l < r:
        #         area = (right - left) * l
        #         while height[left] <= l:
        #             left += 1
        #     else:
        #         area = (right - left) * r
        #         while right > left  and height[right] <= r :
        #             right -= 1
        #     if area > max_area:
        #         max_area = area
        # return max_area
        
