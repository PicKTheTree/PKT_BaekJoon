#Problem Title  :   K number(K번째 수)
#Problem Number :   1300
#Problem Tier   :   Gold 1
#Date           :   2025/03/27, 15:40
#URL            :   https://www.acmicpc.net/problem/1300

# 알고리즘 분류 : 
# 이분 탐색
# 매개 변수 탐색

# 문제
# 세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.
# 배열 A와 B의 인덱스는 1부터 시작한다.

# 입력
# 첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(109, N2)보다 작거나 같은 자연수이다.

# 출력
# B[k]를 출력한다.

# 예제 입력           # 예제 출력 
# 3                    6
# 7





### Python Version


N, K = int(input()), int(input())
start, end, answer = 1, K, 1

while start <= end :
    
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N + 1): 
        temp += min(mid // i, N)
        
    if temp >= K :  answer = mid; end = mid - 1
    else :          start = mid + 1

print(answer)

