# 문제
# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

# 입력
# 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

# 이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

# 출력
# 강의실의 개수를 출력하라.

import sys
import heapq
input = sys.stdin.readline


n = int(input())
classes = []

for _ in range(n):
    s, t = map(int, input().strip().split())
    classes.append((s,t))
    
# 시작시간이 빠른 순서로 정렬
classes.sort()

# 우선순위 큐 (최소힙) 사용
classrooms = []

# 첫 번째 수업이 끝나는 시간을 최소힙에 추가
heapq.heappush(classrooms, classes[0][1])

for i in range(1, n):
    # 가장 빨리 끝나는 수업의 끝나는 시간을 확인
    if classrooms[0] <= classes[i][0]:
        # 기존 수업이 끝났다면 그 강의실을 현재 수업에 사용
        heapq.heappop(classrooms)
    # 현재 수업의 끝나는 시간을 힙에 추가
    heapq.heappush(classrooms, classes[i][1])
        
print(len(classrooms))

    
