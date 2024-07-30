# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)

# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.

# 예제 입력 12
# 예제 출력

            #            *                        
            #           * *                       
            #          *****                      
            #         *     *                     
            #        * *   * *                    
            #       ***** *****                   
            #      *           *                  
            #     * *         * *                 
            #    *****       *****                
            #   *     *     *     *               
            #  * *   * *   * *   * *              
            # ***** ***** ***** *****             
# 참조 (https://ku-hug.tistory.com/149)

import sys
input = sys.stdin.readline

n = int(input())

stars = [[' ']*2*n for _ in range(n)] 

def draw_stars(x, y, size):
    if size == 3:
        stars[x][y] = '*'
        stars[x+1][y-1] = stars[x+1][y+1] = '*'
        for i in range(-2, 3):
            stars[x+2][y+i]='*'
    else:
        new_size = size // 2
        draw_stars(x, y, new_size)
        draw_stars(x+new_size, y-new_size, new_size)
        draw_stars(x+new_size, y+new_size, new_size)
        

draw_stars(0, n-1, n)

for star in stars:
    print(''.join(star))