class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity O(nlogn + mlogm)
        # time taken to sort both
        Sorted_S = sorted(s)
        Sorted_T = sorted(t)
        if Sorted_S == Sorted_T:
            return True
        return False
        