class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans=[]
        val=0
        for i in nums:
            val=(val*2+i)%5
            ans.append(val==0)
        return ans
        