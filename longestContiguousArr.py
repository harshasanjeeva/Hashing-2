class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        dic = {}
        if (len(nums)==0):
            return 0
        rSum = 0
        dic[0] = -1
        m = 0
        for i in range(len(nums)):
            rSum = rSum - 1 if nums[i] == 0 else rSum + 1
            if rSum in dic:
                m = max(m,i-dic[rSum])
            else:
                dic[rSum]  =  i
        
        return m