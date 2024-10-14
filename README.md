# 2530. Maximal Score After Applying K Operations

__Type:__ Medium <br>
__Topics:__ Array, Greedy, Heap (Priority Queue) <br>
__Companies:__ TikTok, Mckinsey <br>
__Leetcode Link:__ [Maximal Score After Applying K Operations](https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/)
<hr>

You are given a __0-indexed__ integer array `nums` and an integer `k`. You have a __starting score__ of `0`.

In one operation:

1. choose an index `i` such that `0 <= i < nums.length`,
2. increase your __score__ by `nums[i]`, and
3. replace `nums[i]` with `ceil(nums[i] / 3)`.

Return _the maximum possible __score__ you can attain after applying **exactly**_ `k` _operations_.

The ceiling function `ceil(val)` is the least integer greater than or equal to `val`.
<hr>

### Examples

__Example 1:__ <br>
__Input:__ nums = [10,10,10,10,10], k = 5 <br>
__Output:__ 50 <br>
__Explanation:__ Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

__Example 2:__ <br>
__Input:__ nums = [1,10,3,3,3], k = 3 <br>
__Output:__ 17 <br>
__Explanation:__ You can do the following operations: <br>
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10. <br>
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4. <br>
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3. <br>
The final score is 10 + 4 + 3 = 17.
<hr>

### Constraints:
- <code>1 <= nums.length, k <= 10<sup>5</sup></code>
- <code>1 <= nums[i] <= 10<sup>9</sup></code>
<hr>

### Hints:
- It is always optimal to select the greatest element in the array.
- Use a heap to query for the maximum in O(log n) time.