class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic={}
        if(len(nums)==0):
            return 0
        
        dic[0] = 1
        rSum =  0
        count = 0
        for i in range(len(nums)):
            rSum = rSum + nums[i]
            print(rSum, rSum - k)
            if (rSum - k) in dic:
                count = count + dic[rSum  -  k]
            if (rSum) in dic:
                dic[rSum] += 1
            else:
                dic[rSum] = 1
                
        return count