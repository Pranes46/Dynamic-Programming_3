class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [[0 for _ in range (amount+1)] for i in range(len(coins)+1)]  #creating a dp matrix
        
        for j in range(1,amount+1):   #iterating all the nums in list 
            dp[0][j] = amount+1        #setting all values to infinityi.e amount+1 cause that is maximum here
                       
        for i in range(1,len(coins)+1):  #iterating thorugh rows
            for j in range(amount+1):     #iterating through columns
                if j < coins[i-1]:         #if the amount is less than j we are adding the previous value 
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1+ dp[i][j-coins[i-1]])  #else we are finding the min between last dp value and current value 
                       
                       
        if dp[-1][-1] == amount+1:
            return -1       #if the last value in dp is amount+1 we are rturning -1
                       
        return dp[-1][-1]   #return dp arrays last value
                       
                    
        