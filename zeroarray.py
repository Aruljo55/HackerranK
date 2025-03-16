class Solution:
    def minOperations(self, nums, queries):
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array for efficient range updates
        cur_nums = nums[:]  # Copy of the original array
        
        for k, (l, r, val) in enumerate(queries, 1):
            # Apply the decrement operation in the difference array
            diff[l] -= val
            diff[r + 1] += val

            # Apply the difference array to the original array
            curr_decrement = 0
            zero_array = True
            
            for i in range(n):
                curr_decrement += diff[i]
                cur_nums[i] += curr_decrement  # Apply net decrement
                
                if cur_nums[i] < 0:
                    cur_nums[i] = 0  # Values can't go below zero
                
                if cur_nums[i] > 0:
                    zero_array = False  # At least one nonzero remains
            
            if zero_array:
                return k  # We found the minimum k that makes nums zero
        
        return -1  # If we never make nums zero
