class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m={}
        for i in nums:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        n=len(nums)
        for i in nums:
            if m[i]>n//2:
                return i
        return -1