# Maximal Score After Applying K Operations with a Max-Heap Approach

- ### Intuition
    - The goal is to select the largest `k` elements from an array, adding them to a score while applying a reduction (dividing by 3 and rounding up) to each selected element before it can be selected again. This requires an efficient way to keep track of and retrieve the largest elements repeatedly.

- ### Approach
    1. **Max-Heap**: Utilize a max-heap to efficiently retrieve and manage the largest elements. In Python, this is done using the `heapq` library by storing negative values to simulate a max-heap.
    2. **Negation**: Negate the values of the elements when adding them to the heap, as Python's `heapq` implements a min-heap by default.
    3. **Selection and Reduction**:
        - Pop the largest (negated) element from the heap.
        - Add the original value to the total score.
        - Reduce the value by dividing it by 3 and rounding up using `math.ceil`.
        - Push the reduced value (negated) back into the heap.
    4. **Repeat** this process until `k` elements have been selected.

- ### Time Complexity
    - The time complexity is O(n + k log n):
    - O(n) for building the heap from `n` elements.
    - Each of the `k` iterations involves O(log n) for both the pop and push operations.

- ### Space Complexity
    - The space complexity is O(n) since we maintain a heap that can store up to `n` elements.

- ### Code
    ```python3 []
    class Solution:
        def maxKelements(self, nums: List[int], k: int) -> int:
            max_Score = 0  # Initialize the score to accumulate the maximum score.
            
            # Convert the list to a max-heap by negating the elements.
            nums = [-1 * x for x in nums]
            heapq.heapify(nums)  # Create a heap from the list.

            while k > 0:  # Continue until we've selected k elements.
                x = -heapq.heappop(nums)  # Pop the largest element (negated back to positive).
                max_Score += x  # Add the largest element to the score.
                
                x = math.ceil(x / 3)  # Reduce the element by a factor of 3 and round up.
                heapq.heappush(nums, -x)  # Push the reduced value back into the heap (negated).
                k -= 1  # Decrement k as we've processed one element.

            return max_Score  # Return the accumulated maximum score.
    ```