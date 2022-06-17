from math import ceil


# 기능 개발
# n개의 기능의 개발 진행도와 개발 속도가 주어지고
# 이전 기능들이 모두 배포되고 진행도가 100이 될 때 배포 가능하며
# 배포는 하루에 한번만 가능하다고 할 때
# 모든 기능을 배포할 때 까지 각 배포마다 배포된 기능의 수를 구하는 문제
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    day = 0
    for i in range(n):
        # 남은 진도
        remain = 100 - progresses[i] - day * speeds[i]

        # 남은 진도가 0 이하라면 이미 끝난 작업이므로 마지막 배포와 함께 배포
        if remain <= 0:
            answer[-1] += 1

        # 아직 진도가 남았다면 그만큼 일수를 진행 후 배포
        else:
            day += ceil(remain / speeds[i])
            answer.append(1)

    return answer
