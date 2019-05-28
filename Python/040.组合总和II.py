class Solution(object):
    def combinationSum2(self, candidates, target):
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
            
            for i in range(index  , len(candy)):
                
                if i > index and candy[i] == candy[i - 1]: # 为了避免重复 [[1,1,6],[1,2,5],[1,7],[1,2,5],[1,7],[2,6]]
                    continue
                
                if candy[i] > remain:
                    break
                dfs(remain - candy[i], stack + [candy[i]], i + 1)

        candy = sorted(candidates)
        result = []
        dfs(target, [], 0)
        return result
        
        
