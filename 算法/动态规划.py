"""
菲波那切数列： 1 1 2 3 5 8（当前值为前两个数之和）
动态规划爬5层楼梯问题，逐步优化 F(n) = F(N-1) + F(N-2)
"""

# 1.递归 复杂度 O（2^n）


def climb_stairs(n):
    if n < 2:
        return 1
    return climb_stairs(n-1)+climb_stairs(n-2)

# 2.非递归，列表存储到每个台阶的种类数 时间复杂度：O(n) 空间复杂度 O(n)


def climb_stairs2(n):
    if n < 2:
        return 1
    dp = [0 for x in range(n+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# 3.用2个变量接收到达上个台阶和上上个台阶的种类数  时间复杂度：O(n) 空间复杂度 O(1)


def climb_stairs3(n):
    if n < 2:
        return 1
    new = 1
    old = 1

    for i in range(2, n+1):
        new, old = new+old, new

    return new



