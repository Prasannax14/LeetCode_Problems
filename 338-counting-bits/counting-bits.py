class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [] 

        for i in range(n + 1):
            num=i
            count=0
            while num>0:
                if num%2 == 1:
                    count+=1
                num//=2
            ans.append(count)

        return ans
