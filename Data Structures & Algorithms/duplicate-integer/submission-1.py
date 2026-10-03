class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # this solution uses a hashset to check if the same value
        # appears more than once
        # better time complexity o(n)
        # uses more memory (hashset)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False