class Solution(object):
    def solve(self,amount,coins,i,memo):
        if (amount==0): return 1
        if (amount<0 or i<0): return 0
        if (memo[i][amount]!=-1):
            return memo[i][amount]

        include=self.solve(amount-coins[i], coins, i, memo)
        exclude=self.solve(amount, coins, i-1, memo)

        memo[i][amount]=include+exclude
        return memo[i][amount]

    def change(self, amount, coins):
        n=len(coins)
        memo = [[-1] * (amount + 1) for _ in range(n)]
        return self.solve(amount, coins, n - 1, memo)
