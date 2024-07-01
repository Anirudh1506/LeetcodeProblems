"""
This code provides a 2 pointer approach to deciding whether a string is palidrome or not by removing any special 
symbols if present

L.C: Q.125
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        st=s.lower()
        i=0
        j=len(st)-1
        while i<j:
            if (st[i] >='a' and st[i]<='z') or (st[i]>='0' and st[i]<='9'):
                if (st[j]>='a' and st[j]<='z') or (st[j]>='0' and st[j]<='9'):
                    if (st[i]!=st[j]):
                        return False
                    else:
                        i+=1
                        j-=1
                else:
                    j-=1
            else:
                i+=1
        return True
        
        