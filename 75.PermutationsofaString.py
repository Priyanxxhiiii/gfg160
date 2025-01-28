class Solution:
    def findPermutation(self, s):
        # Code here
        def backtrack(start):
            if start==len(chars):
                permutations.add(''.join(chars))
                return 
            for i in range(start,len(chars)):
                chars[start],chars[i]=chars[i],chars[start]
                backtrack(start+1)
                chars[start],chars[i]=chars[i],chars[start]
        chars=list(s)
        permutations=set()
        backtrack(0)
        return list(permutations)
sol=Solution()
print(sol.findPermutation(s = "ABC"),end='\n\n')      
print(sol.findPermutation(s = "ABSG"))
