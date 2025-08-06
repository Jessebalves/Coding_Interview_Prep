# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highest_wealth = 0 
        wealth = 0 

        if len(accounts) == 1:
            for value in accounts[0]:
                wealth += value
            return wealth

        for i in range(len(accounts)):
            if wealth > highest_wealth:
                highest_wealth = wealth
            wealth = 0 
            for value in accounts[i]:
                wealth += value
        return highest_wealth
