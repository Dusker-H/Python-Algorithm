# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 동적 프로그래밍으로 문제를 작게 만들어서 진행을 할 수 있음
import sys
input=sys.stdin.readline

def min_operation_to_one(n):
    dp=[0] * (n+1)
    
    for i in range(2, n+1):
        # 1을 뺀 경우
        dp[i]=dp[i-1]+1
        
        # 2로 나누어 떨어지는 경우
        if i % 2==0:
            dp[i]=min(dp[i], dp[i//2]+1)
            
        # 3로 나누어 떨어지는 경우
        if i % 3==0:
            dp[i]=min(dp[i], dp[i//3]+1)
            
            
    return dp[n]

def main():
    n=int(input())
    print(min_operation_to_one(n))
    
if __name__=="__main__":
    main()