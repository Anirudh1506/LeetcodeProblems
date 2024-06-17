"""
This uses a time complexity of O(n^2) which iters through the array and also removes elements using the pop
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        while i<len(nums):
            if nums[i-1]==nums[i]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
    

"""
This uses a time complexity of O(nlogn) with the sorting
It sorts the set of elements present in set of nums
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:]=sorted(set(nums))
        print(nums)
        return len(nums)
        