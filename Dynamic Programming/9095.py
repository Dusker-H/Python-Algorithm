# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.


import sys
input=sys.stdin.readline

def count_ways_to_sum(n):
    
    dp=[0] * (n+1)
    
    # 기저 사례를 설정
    dp[0]=1
    
    for i in range(1, n+1):
        if i>=1:
            dp[i]+=dp[i-1]
        if i>=2:
            dp[i]+=dp[i-2]
        if i>=3:
            dp[i]+=dp[i-3]
            
    return dp[n]
        

t=int(input())
n=[int(input().strip()) for _ in range(t)]
results=[]

for i in range(t):
    results.append(count_ways_to_sum(n[i]))

for result in results:
    print(result)