# Problem title  :   Least common multiple(최소 공배수)
# Problem Number :   1934
# Problem Tier   :   Bronze 1
# Date           :   2023/03/06, 10:17 
# URL            :   https://www.acmicpc.net/problem/1934

# 문제
# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
# 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다.
# 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

# 출력
# 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.


#예제 입력      예제 출력
# 3
# 1 45000       45000
# 6 10          30
# 13 17         221

###Python Version

for _ in range( int( input() ) ):

    Num_A, Num_B = sorted( map( int,input().split() ) )
    Num_AB = Num_A * Num_B
    Num_rest = Num_B % Num_A

    while( Num_rest != 0 ):

        Num_B = Num_A; Num_A = Num_rest
        Num_rest = Num_B % Num_A
    
    print( Num_AB // Num_A )

    





