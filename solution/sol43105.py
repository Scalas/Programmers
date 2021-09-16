def solution(triangle):
    def dfs(i, j):
        if dp[i][j] == -1:
            res = [0]
            if i - 1 >= 0:
                if j - 1 >= 0:
                    res.append(dfs(i - 1, j - 1))
                if j <= i - 1:
                    res.append(dfs(i - 1, j))
            dp[i][j] = max(res) + triangle[i][j]
        return dp[i][j]

    i = len(triangle)
    dp = [[-1] * (j + 1) for j in range(i)]

    return max([dfs(i-1, j) for j in range(i)])
