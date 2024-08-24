class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        i,j=0,len(n)-1
        while i<j:
            if n[i]+n[j] == target:
                return [i+1,j+1]
            elif n[i]+n[j]>target:
                j-=1
            else:
                i+=1
        return [-1,-1]