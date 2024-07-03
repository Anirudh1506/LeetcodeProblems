"""
This method counts the number of zeroes in the initial array
replaces all the initial elements with values which are not zero, and then modifies c zeroes at the end

T.C: O(n)
L.C: Q.283
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        n=len(nums)
        c=0
        for i in nums:
            if i==0:
                c+=1
        j=0
        for i in nums:
            if i!=0:
                nums[j]=i
                j+=1
        
        for i in range(j,len(nums)):
            nums[i]=0

