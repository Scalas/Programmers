from heapq import heappush, heappop, heapify


# 더 맵게
# 음식들의 스코빌지수 scoville과 매운 정도의 마지노선 K가 주어지고
# 가진 음식중 가장 덜 매운 음식과 두 번째로 덜 매운 음식을 섞어
# (가장 덜 매운 음식의 스코빌지수) + (두 번째로 덜 매운 음식의 스코빌 지수 * 2) 만큼의
# 스코빌 지수를 가진 음식을 만들 수 있을 때
# 모든 음식의 스코빌지수가 k 이상이 되도록 하기위해 음식을 섞어야할 최소 횟수를 구하는 문제
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    try:
        # heap을 사용하여 가장 덜 매운 음식이 k 이상의 스코빌 지수를 가질 때 까지
        # 가장 덜 매운 두 음식을 계속 섞어준다
        while scoville and scoville[0] < K:
            answer += 1
            heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
    # heappop에서 exception이 발생할 경우 모든 음식의 스코빌 지수를 k 이상으로 만들 수 없음
    except:
        return -1

    return answer