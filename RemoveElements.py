"""
The given below solution only gives the count of elements after removing
the val in array. The time complexity of the solution is: O(n)
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i=0
        for x in nums:
            if x!=val:
                nums[i]=x
                i+=1
        return i

"""
The given below solution is a 2 pointer approach to the problem which is still O(n) in worst cases but faster 
for average and best time complexity cases
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i,j=0,len(nums)-1
        while i<=j:
            if nums[i]==val:
                t=nums[i]
                nums[i]=nums[j]
                nums[j]=t
                j-=1
            else:
                i+=1
        print(nums)
        return i

        