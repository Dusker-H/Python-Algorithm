# 문제
# N개의 강의가 있다. 우리는 모든 강의의 시작하는 시간과 끝나는 시간을 알고 있다. 이때, 우리는 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.

# 물론, 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다. 필요한 최소 강의실의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 강의의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 줄마다 세 개의 정수가 주어지는데, 순서대로 강의 번호, 강의 시작 시간, 강의 종료 시간을 의미한다. 강의 번호는 1부터 N까지 붙어 있으며, 입력에서 꼭 순서대로 주어지지 않을 수 있으나 한 번씩만 주어진다. 강의 시작 시간과 강의 종료 시간은 0 이상 10억 이하의 정수이고, 시작 시간은 종료 시간보다 작다.

# 출력
# 첫째 줄에 필요한 최소 강의실 개수를 출력한다.

import sys
import heapq

n = int(input())
lectures = []

for _ in range(n):
    _, start, end = map(int, input().strip().split())
    lectures.append((start,end))

lectures.sort()

# 우선순위 큐
min_heap = []

# 첫 번째 강의의 종료 시간을 힙에 넣음
heapq.heappush(min_heap, lectures[0][1])

# 나머지 강의들 처리
for i in range(1, n):
    start, end = lectures[i]
    
    # 가장 빨리 끝나는 강의실의 종료 시간이 현재 강의의 시작 시간보다 작거나 같으면 그 강의실 사용
    if min_heap[0] <= start:
        heapq.heappop(min_heap)  # 해당 강의실에서 강의를 끝냄
        
    # 새로운 종료 시간을 힙에 추가
    heapq.heappush(min_heap, end)        
            
print(len(min_heap))

        
