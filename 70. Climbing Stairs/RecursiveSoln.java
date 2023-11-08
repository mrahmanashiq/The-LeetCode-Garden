class Solution {
    public int climbStairs(int n) {
        return totalWays(0, n);
    }

    private int totalWays(int currentStairs, int targetStairs) {
        if (currentStairs == targetStairs) return 1;

        if (currentStairs > targetStairs) return 0;

        int oneJump = totalWays(currentStairs + 1, targetStairs);
        int twoJump = totalWays(currentStairs + 2, targetStairs);

        return oneJump + twoJump;
    }
}

// above code will give TLE  because of large values of n
// TC: O(2^n)