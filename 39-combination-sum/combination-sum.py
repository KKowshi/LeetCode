class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: #[2,3,6,7]
        res = []

        def dfs(i,cur,total):  #(0,[],0)
            if total == target: 
                res.append(cur.copy())
                return 


            if i>= len(candidates)  or total > target:
                return   

            cur.append(candidates[i]) #[2,2]
            dfs(i,cur, total+candidates[i]) #(0, [2,2], [4])
            cur.pop() #[2]
            dfs(i+1, cur, total) #(1, [2], )


        dfs(0, [], 0)
        return res 


        
        
        