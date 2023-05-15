# bruce force solution
def two_sum(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

""" The code above does the following:
    1. Traverse the list.
    2. For each element, check if the sum of the current element and the next element is equal to the target.
    3. If the sum of the current element and the next element is equal to the target, return the indices of the current element and the next element.
    4. If the sum of the current element and the next element is not equal to the target, continue traversing the list.
    5. If the sum of the current element and the next element is not equal to the target and the current element is the last element in the list, return an empty list.

    # time complexity: O(n^2)
        - The for loop is O(n) and the nested for loop is O(n).
    # space complexity: O(1)
        - amount of space used is independent of the size of the input.
"""

# hash table solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hashmap:
                return [i, hashmap[key]]
            hashmap[nums[i]] = i

        return []


""" The code above does the following:
    1. Create a hash table.
    2. Traverse the list.
    3. For each element, check if the difference between the target and the current element is in the hash table.
    4. If the difference between the target and the current element is in the hash table, return the indices of the current element and the difference.
    5. If the difference between the target and the current element is not in the hash table, add the current element and its index to the hash table.
    6. If the difference between the target and the current element is not in the hash table and the current element is the last element in the list, return an empty list.

    # time complexity: O(n)
        - The for loop is O(n) and the get method is O(1).
    # space complexity: O(n)
        - The space used by the hash table is equal to the number of elements in the hash table.
"""
