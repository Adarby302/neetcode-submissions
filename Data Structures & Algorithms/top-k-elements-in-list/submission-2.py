class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first iteration is a dictionary 
        res = defaultdict(int)
        sol = []
        #sorted method which is terrible
        for i in nums:
            res[i] += 1
        sorted_res = dict(sorted(res.items(), key = lambda item: item[1], reverse= True))

        for key in sorted_res:
            if len(sol) != k:
                sol.append(key)

        return sol
        


            

                

        
  

                
