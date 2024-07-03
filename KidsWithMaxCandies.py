"""
This code solves the problem of kids with highest candies, after adding the extra candies.
Time Complexity: O(n)
L.C: Q.1431
"""

class Solution(object):
    def kidsWithCandies(self, candies, extra):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_ele=max(candies)

        res=[]

        for i in range(0,len(candies)):
            if candies[i]+extra >=max_ele :
                res.append(True)
            else:
                res.append(False)
        return res