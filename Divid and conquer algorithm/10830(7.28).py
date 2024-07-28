# 문제
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

# 입력
# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

import sys
input = sys.stdin.readline

# 두 행렬 A와 B를 반환하는 함수        
def matrix_mult(A, B, size):
    result = [[0]*(size) for _ in range(size)]
    for i in range(size):
        for j in range(size):
            element_sum = 0
            for k in range(size):
                element_sum += A[i][k] * B[k][j] # 행렬 곱셈 처리 방법
            result[i][j] = element_sum % 1000
            
    return result

# 행렬의 거듭제곱을 계산하는 함수
def matrix_power(matrix, power, size):
    
    if power == 1:
        return [[element % 1000 for element in row] for row in matrix]
    elif power %2 ==0:
        half_power_matrix = matrix_power(matrix, power//2, size)
        return matrix_mult(half_power_matrix, half_power_matrix, size)
    else:
        return matrix_mult(matrix, matrix_power(matrix, power - 1, size), size)
    
n, b = map(int, input().strip().split())

matrix = [list(map(int, input().strip().split())) for _ in range(n)]

result = matrix_power(matrix, b, n)

for row in result:
    print(' '.join(map(str, row)))