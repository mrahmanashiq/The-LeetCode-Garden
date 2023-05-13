class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hashmap:
                return [i, hashmap[key]]
            hashmap[nums[i]] = i

        return []

"""
 --Algorithm --
1. traverse the list
2. for each element, check if the difference between the target and the current element exists in the hashmap
3. if it exists, return the current index and the index of the element that is the difference between the target and the current element
4. if it does not exist, add the current element to the hashmap
"""
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
