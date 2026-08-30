LeetCode Challenge

Objective

The objective of this task was to solve five leetcode problems using efficient alogrithms and clearly explain the approach,logic,implementation and complexity of each solution

I solved the recommended combination of:

3 Easy-level problems
2 Medium-level problems

All five solutions were implemented in Python 3 and successfully submitted on LeetCode.
Problem 1 — Two Sum

LeetCode: #1
Difficulty: Easy
Language: Python 3
Approach: Hash Map

Problem

Given an array of integers nums and an integer target, find two different elements whose sum is equal to target.

The required output is the indices of those two elements.

Example:
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Approach

I used a dictionary to store numbers that I had already encountered along with their indices.

For every number, I calculated:
needed = target - current number

Then I checked whether needed was already present in the dictionary.

If it was present, I had found the required pair.

Code:
class Solution:
    def twoSum(self, nums, target):
        box = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in box:
                return [box[needed], i]

            box[num] = i
For every number, instead of checking every other number, I directly calculate the number needed to reach the target.

For example:

target = 9
current number = 2


needed = 9 - 2
       = 7

If 7 has already been seen, the answer is found.
Complexity
Time Complexity: O(n)
Space Complexity: O(n)

Result

Accepted — all test cases passed. ✅

Problem 2 — Valid Parentheses

LeetCode: #20
Difficulty: Easy
Language: Python 3
Approach: Stack

Problem

Given a string containing:

( )
{ }
[ ]

determine whether the brackets are correctly matched and properly ordered.

Example
Input:
"()[]{}"


Output:
true

Input:
"(]"

Output:
false

Approach

I used a stack.

When an opening bracket appears, I store the corresponding closing bracket in the stack.

For example:

(

means I expect:

)

So I push ) into the stack.

When a closing bracket appears, I check whether it matches the bracket expected at the top of the stack.

Code:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            elif not stack or stack.pop() != c:
                return False

        return not stack

This is exactly the Last In, First Out (LIFO) behavior of a stack.

If a mismatch occurs, the string is immediately invalid.

At the end, the stack must also be empty.

Complexity
Time Complexity: O(n)
Space Complexity: O(n)

Result

Accepted — all test cases passed. ✅

Problem 3 — Best Time to Buy and Sell Stock

LeetCode: #121
Difficulty: Easy
Language: Python 3
Approach: Greedy / One-pass

Problem

Given stock prices for different days, choose one day to buy and a later day to sell so that the profit is maximized.

Example
Input:
[7, 1, 5, 3, 6, 4]


Output:
5

The best transaction is:

Buy at 1
Sell at 6


Profit = 6 - 1
       = 5
Approach

I keep track of two things:

The lowest buying price seen so far.
The maximum profit found so far.

Initially:

buy_price = prices[0]
profit = 0

For every price:

If the current price is cheaper, update buy_price.
Otherwise, calculate the possible profit.
Use max() to keep the best profit.

Code:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                current_profit = price - buy_price
                profit = max(profit, current_profit)

        return profit

max() function

Suppose:

previous best profit = 4
current possible profit = 2
 therefore,
     max(4,2) gives 4 as output
Therefore profit always stores the maximum profit found so far.
Complexity
Time Complexity: O(n)
Space Complexity: O(1)

Only two variables are needed regardless of the size of the input.

Result

Accepted — all test cases passed. 

Problem 4 — Binary Search

LeetCode: #704
Difficulty: Medium
Language: Python 3
Approach: Binary Search

Problem

Given a sorted array and a target value, return the index of the target.

If the target does not exist, return -1.
Example
Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 9

Output:
4

Approach

I used three variabiables:

left
right
middle
Initially:

left = 0
right = len(nums) - 1

I calculate the middle:

middle = (left + right) // 2

Then I compare the middle value with the target.

There are three possibilities:

Middle value is greater:

nums[middle] > target

The target must be on the left side.

Therefore:

right = middle - 1

Middle value is smaller

Target found

nums[middle] == target

Return:

middle
nums[middle] < target

The target must be on the right side.

Therefore:

left = middle + 1

Code :

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1

Instead of checking every element, Binary Search eliminates approximately half of the remaining elements after every comparison.Therefore, the algorithm is much faster than a linear search for large sorted arrays.

Complexity
Time Complexity: O(log n)
Space Complexity: O(1)

Result

Accepted — all test cases passed.

## Problem 5: Longest Substring Without Repeating Characters

* LeetCode:#3
* Problem: Longest Substring Without Repeating Characters
* Language:Python
* Difficulty:Medium
* Status: Accepted

### Approach

I used the "sliding window" technique with a set.

The set stores the characters currently present in the substring. Two pointers are used:
- `l` represents the left side of the window.
- `r` represents the right side of the window.

For every character at position `r`, I check whether it is already present in the set. If it is present, I remove characters from the left side until the duplicate is removed.

Then I add the current character to the set and calculate the length of the current substring.

I keep updating the maximum length using `max()`.

### Code


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1

            charset.add(s[r])
            res = max(res, r - l + 1)

        return res
        

Example

Input:
"pwwkew"

Output:
3

The longest substring without repeating characters is "wke", which has length 3.

Complexity:

Time Complexity: O(n)
Space Complexity: O(n)
What I Learned

I learned how the sliding window technique can be used to solve substring problems efficiently. I also learned how a set can be used to keep track of unique characters and how max() helps maintain the longest valid substring found so far.







