# brute force solution
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

""" The code above does the following:
    1. Check if the length of the two strings are equal or not. If not, return False.
    2. If the length of the two strings are equal, check if the count of each character in s is equal to the count of each character in t.
    3. If the count of each character in s is equal to the count of each character in t, return True. Otherwise, return False.

    # time complexity: O(n^2) 
        - s.count(i) and t.count(i) are both O(n) operations.
    # space complexity: O(1)
        - amount of space used is independent of the size of the input.
"""

# hash table solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        return count_s == count_t

""" The code above does the following:
    1. Check if the length of the two strings are equal or not. If not, return False.
    2. If the length of the two strings are equal, create two hash tables to store the count of each character in s and t.
    3. Check if the two hash tables are equal. If yes, return True. Otherwise, return False.

    # time complexity: O(n)
        - The for loop is O(n) and the get method is O(1).
    # space complexity: O(n)
        - The space used by the hash table is equal to the number of elements in the hash table.
"""