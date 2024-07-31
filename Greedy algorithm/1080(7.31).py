# 문제
# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

# 입력
# 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

import sys

input = sys.stdin.readline

def flip(matrix, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix[i][j] = 1 - matrix[i][j]
            
def min_operations_to_transform(A, B, N, M):
    operations = 0
    
    # 범위를 다음과 같이 조절
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j]!=B[i][j]:
                flip(A, i, j)
                operations +=1                 
            
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return -1
    
    return operations
            

N, M = map(int, input().strip().split())
A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]

print(min_operations_to_transform(A, B, N, M))