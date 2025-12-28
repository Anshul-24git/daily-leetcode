class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            current_price = prices[i]

            if current_price < min_price:
                min_price = current_price

            current_profit = current_price - min_price

            if current_profit > max_profit:
                max_profit = current_profit

            # max_profit = max(max_profit, current_profit)

            # min_price = min(min_price, current_price)

        return max_profit
        '''
        prices
            price[i] - price of a stock on ith day
        maximize profit
            one day to buy
            different day to sell
        Return
            max profit
        Return
            0 if no profit

        Input: prices = [7,1,5,3,6,4]
        Output: 5

        min_price
        max_profit = 0
            profit = cur_price - min_price
            update max_profit
            update min_price
        For prices = [7, 1, 5, 3, 6, 4]:

        Day 0: price=7, min_price=7, max_profit=0
        Day 1: price=1, min_price=1, max_profit=0
        Day 2: price=5, profit=5-1=4, max_profit=4
        Day 3: price=3, profit=3-1=2, max_profit=4
        Day 4: price=6, profit=6-1=5, max_profit=5
        Day 5: price=4, profit=4-1=3, max_profit=5
        '''
        # if len(prices) <= 1:
        #     return 0
        
        # min_price = float('inf')
        # max_profit = 0

        # for price in prices:
        #     if price < min_price:
        #         min_price = price
            
        #     current_profit = price - min_price
        #     max_profit = max(max_profit, current_profit)

        # return max_profit

'''
Input: prices = [7,1,5,3,6,4]
Output: 5

min_price = infinity, max_profit = 0
p = 7: min_price = 7, profit = 0, max_profit = 0
p = 1: min_price = 1, profit = 0, max_profit = 0
p = 5: min_price = 1, profit = 4, max_profit = 4
p = 3: min_price = 1, profit = 2, max_profit = 4
p = 6: min_price = 1, profit = 5, max_profit = 5
.....
return max_profit = 5
''' 
