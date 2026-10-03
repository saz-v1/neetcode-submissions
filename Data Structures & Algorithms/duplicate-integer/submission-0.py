class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # slightly longer as needs to do sorting nlogn 
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False