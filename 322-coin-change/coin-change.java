class Solution {
    public int coinChange(int[] coins, int amount) {
        int inf = 1000000009;
        int[] dp = new int[amount + 1];
        for(int i = 1; i <= amount; i++) dp[i] = inf;
        dp[0] = 0;
        for(int coin : coins){
            for(int i = coin; i <= amount; i++){
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return (dp[amount] == inf ? -1 : dp[amount]);
    }
}