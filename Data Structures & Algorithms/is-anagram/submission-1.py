class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solve using hashmap lower time complexity
        # only have to iterate once through each string o(n + m)
        if len(s) != len(t):
            return False
        
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT