# 타겟 넘버
# 0이상의 정수 수열 numbers와 만들려는 수 target이 주어지고
# numbers의 수를 빼거나 더하여 target을 만들려 할 때
# target을 만들 수 있는 경우의 수를 구하는 문제
def solution(numbers, target):
    n = len(numbers)

    # 주어진 수의 합에서 target의 절댓값을 뺀 나머지를 구함
    remain = sum(numbers) - abs(target)

    # 나머지가 0 미만이거나 홀수라면 target을 만들 방법이 없음
    if remain < 0 or remain % 2:
        return 0

    # 나머지가 0 이라면 방법은 하나뿐
    if not remain:
        return 1

    # 주어진 수 중에서 일부를 골라 그 합이 remain // 2 가 되는 경우의 수를 구함
    remain //= 2
    dp = [[-1] * (remain + 1) for _ in range(n)]

    def dfs(cur, total):
        if cur == n:
            if total == remain:
                return 1
            return 0

        if dp[cur][total] < 0:
            res = 0

            if total + numbers[cur] <= remain:
                res += dfs(cur + 1, total + numbers[cur])

            res += dfs(cur + 1, total)
            dp[cur][total] = res

        return dp[cur][total]

    return dfs(0, 0)
