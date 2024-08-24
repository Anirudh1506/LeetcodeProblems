class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j=0,len(nums)-1
        ans=[]
        while i<=j:
            if nums[i]*nums[i]>nums[j]*nums[j]:
                ans.append(nums[i]*nums[i])
                i+=1
            else:
                ans.append(nums[j]*nums[j])
                j-=1
            print(ans)
        return ans[::-1]