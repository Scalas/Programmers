# 행렬 테두리 회전하기
# rows * columns 크기의 행렬이 주어지고
# 최대길이 10000의 테두리를 회전할 사각형의 범위를 지정하는 배열이 주어졌을때
# 배열의 각 회전을 처리할 때마다 회전되는 숫자들중 최솟값을 배열에 넣어 반환하는 문제
# 회전은 시계방향으로 1칸씩 이루어진다
def solution(rows, columns, queries):
    answer = []
    board = [[i * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    for r1, c1, r2, c2 in queries:
        tmp = board[r1 - 1][c1 - 1]
        min_val = tmp
        for i in range(r1 - 1, r2 - 1):
            board[i][c1 - 1] = board[i + 1][c1 - 1]
            min_val = min(min_val, board[i][c1 - 1])
        for i in range(c1 - 1, c2 - 1):
            board[r2 - 1][i] = board[r2 - 1][i + 1]
            min_val = min(min_val, board[r2 - 1][i])
        for i in range(r2 - 1, r1 - 1, -1):
            board[i][c2 - 1] = board[i - 1][c2 - 1]
            min_val = min(min_val, board[i][c2 - 1])
        for i in range(c2 - 1, c1, -1):
            board[r1 - 1][i] = board[r1 - 1][i - 1]
            min_val = min(min_val, board[r1 - 1][i])
        board[r1 - 1][c1] = tmp
        answer.append(min_val)

    return answer
