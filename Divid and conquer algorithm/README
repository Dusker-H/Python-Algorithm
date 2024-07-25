# 입력
# 첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

# 출력
# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

import sys
input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, list(input().strip().split()))) for _ in range(n) ]
white_count = 0
blue_count = 0
    
def check_tile(x, y, n):
    global white_count, blue_count # 전역변수 선언
    
    color = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != matrix[i][j]:
                check_tile(x, y, n//2)
                check_tile(x, y+n//2, n//2)
                check_tile(x+n//2, y, n//2)
                check_tile(x+n//2, y+n//2, n//2)
                return # return 으로 반복문을 끝내주어야함
    if color == 0:
        white_count+=1
    else:
        blue_count+=1

check_tile(0, 0, n)

print(white_count)
print(blue_count)
            
    