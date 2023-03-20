#Problem title  :   Cording is PE Class
#Problem Number :   25314
#Problem Tier   :   Bronze 5
#Date           :   2023/03/20, 20:27
#URL            :   https://www.acmicpc.net/problem/25314

# 입력
# 첫 번째 줄에는 문제의 정수 N이 주어진다. (4 <= N <= 1000, N은 4의 배수)

# 출력
# 혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

# 예제 입력 2 
# 20
# 예제 출력 2 
# long long long long long int

###Python version 

Len_int = int( input() )
print( "long " * ( Len_int  // 4 ) + "int" ) 