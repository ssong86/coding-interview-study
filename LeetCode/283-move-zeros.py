# easy
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) # len is in-place, so if you update in the loop, this can be affected
        for i in xrange(n):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
            else:
                continue
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        
