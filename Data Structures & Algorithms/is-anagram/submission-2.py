class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashtable version lowest complexity and memory (only 26 as assume all lowercase)
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 # ord = ordinal unicode for the character
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False # the val should be 0 as the letters cancel out           
        return True     

        