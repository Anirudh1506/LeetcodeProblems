"""
This approach merges two strings alternatively using two pointers i and j which travel across both the strings
This has a time complexity of O(max(n,m)) 
L.C: Q.1768
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        j=0
        n=len(word1)
        m=len(word2)
        ans=''
        while i<n and j<m:
            ans+=word1[i]+word2[j]
            i+=1
            j+=1
        if i!=n:
            ans+=word1[i:n]
        if j!=m:
            ans+=word2[j:m]
        return ans
        