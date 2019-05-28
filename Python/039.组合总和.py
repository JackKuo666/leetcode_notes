class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 法1.dfs
        def dfs(remain, stack, index):
            if remain == 0:
                result.append(stack)
                return
            
            for i in range(index, len(candy)):
                if candy[i] > remain:
                    break
                dfs(remain - candy[i], stack + [candy[i]], i)
       
        candy = sorted(candidates)
        result = []
        dfs(target, [], 0)
        return result
        
