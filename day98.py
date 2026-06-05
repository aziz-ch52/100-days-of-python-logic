# LeetCode 4: Median of Two Sorted Arrays

# Time Complexity: O(log(min(m, n))) - Binary search on the smaller array.
# Space Complexity: O(1) - Only a few pointers are used.

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search time complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            partition_A = (low + high) // 2
            partition_B = total_left - partition_A
            
            # Edge cases: If the partition is at the boundaries, use infinity
            max_left_A = float('-inf') if partition_A == 0 else nums1[partition_A - 1]
            min_right_A = float('inf') if partition_A == m else nums1[partition_A]
            
            max_left_B = float('-inf') if partition_B == 0 else nums2[partition_B - 1]
            min_right_B = float('inf') if partition_B == n else nums2[partition_B]
            
            # Check if we found the correct partition
            if max_left_A <= min_right_B and max_left_B <= min_right_A:
                # If the total number of elements is odd
                if (m + n) % 2 != 0:
                    return float(max(max_left_A, max_left_B))
                # If total number of elements is even
                else:
                    return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2.0
            
            # Tune the binary search range
            elif max_left_A > min_right_B:
                high = partition_A - 1
            else:
                low = partition_A + 1
                
        raise ValueError("Input arrays are not sorted or invalid.")
