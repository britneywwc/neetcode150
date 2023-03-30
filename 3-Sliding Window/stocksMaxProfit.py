def maxProfit(prices) -> int:
    profit = 0
    if len(prices) < 2:
        return profit

    currMin = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < currMin:
            currMin = prices[i]

        currProfit = prices[i] - currMin
        if currProfit > profit:
            profit = currProfit

    return profit


# p = [7, 1, 5, 3, 6, 4]
# p = [7,6,4,3,1]
p = [2, 1, 4]

print(maxProfit(p))

