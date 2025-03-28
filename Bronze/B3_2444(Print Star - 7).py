#Problem title  :   Print Star - 7(별찍기 - 7)
#Problem Number :   2444
#Problem Tier   :   Bronze 3
#Date           :   2025/03/28, 12:27
#URL            :   https://www.acmicpc.net/problem/2444

# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1 
# 5

# 에제 출력 1
#     *         1 
#    ***        2       
#   *****       3
#  *******      4
# *********     5
#  *******      6
#   *****       7
#    ***        8
#     *         9


### Python Version

N = int(input())

for N_index in range(1, N): # 1 ~ 4, 시작 ~ 중간 -1 

    for space_index in range(N - N_index): print(" ", end='')
    print("*" * (2 * N_index - 1))

for N_index in range(N, 0, -1): # 5 ~ 9, 중간 ~ 끝

    for space_index in range(N - N_index): print(" ", end='')
    print("*" * (2 * N_index - 1))
