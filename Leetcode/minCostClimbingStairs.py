def minCostClimbingStairs(cost):
    if len(cost) == 2:
        return min(cost[0], cost[1])
    
    cache = {}

    def dp(n):
        if n in cache:
            return cache[n]
        
        if n <= 1:
            return cost[n]
        
        val = min(dp(n-1), dp(n-2)) + cost[n]
        cache[n] = val
        return val
    
    return min(dp(len(cost) - 1), dp(len(cost) - 2))


if __name__ == '__main__':
    cost = [10,15,20]
    print(minCostClimbingStairs(cost))