class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i,cur,total):  #(0,[],0)
            if total == target: 
                res.append(cur.copy())
                return 


            if i== len(candidates)  or total > target:
                return   

            

            cur.append(candidates[i]) #[2,2]
            dfs(i+1,cur, total+candidates[i]) #(0, [2,2], [4])
            cur.pop() #[2]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)
    
        dfs(0, [], 0)
        return res 
        