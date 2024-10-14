from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_Score = 0  # Initialize the score to accumulate the maximum score.
        
        # Convert the list to a max-heap by negating the elements.
        nums = [-1 * x for x in nums]
        heapq.heapify(nums)  # Create a heap from the list.

        while k:  # Continue until we've selected k elements.
            x = -heapq.heappop(nums)  # Pop the largest element (negated back to positive).
            max_Score += x  # Add the largest element to the score.
            
            x = math.ceil(x / 3)  # Reduce the element by a factor of 3 and round up.
            heapq.heappush(nums, -x)  # Push the reduced value back into the heap (negated).
            k -= 1  # Decrement k as we've processed one element.

        return max_Score  # Return the accumulated maximum score.

# Time Complexity: O(k log n)
# - heapify takes O(n)
# - each of the k iterations involves a pop and a push operation, each taking O(log n).
# Therefore, the overall time complexity is O(n + k log n).

# Space Complexity: O(n)
# - We use space for the heap which contains n elements in the worst case.