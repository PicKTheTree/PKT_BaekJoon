#Problem Title  :   Color Paper(색종이)
#Problem Number :   2563
#Problem Tier   :   Sliver 5
#Date           :   2023/03/06, 20:36
#URL            :   https://www.acmicpc.net/problem/2563


# 문제
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 
# 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 
# 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 
# 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 
# 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

# 출력
# 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.

# 예제 입력   예제 출력
# 3           260
# 3 7
# 15 7
# 5 2



###Python Version


# int String_white_paper[101][101] = [ [ 0, 0, 0 ..., 0 ], ... ] 

# String_white_paper = [ ]
# for _ in range(101): 
#     row = [ ]
#     for j in range(101):
#         row.append(0)
#     String_white_paper.append(row)

String_white_paper = [ [ 0 ] * 101 for i in range( 101 ) ] 


# Acoording to Input data, Covering black paper
for _ in range( int( input() ) ):
    
    Num_X, Num_Y = map( int, input().split() )

    for x in range( 10 ) : 
        for y in range( 10 ) : 
            String_white_paper[ Num_X + x ][ Num_Y + y] = 1
    

# print Size_of_black_paper
Size_of_black_paper = 0
for _ in String_white_paper : Size_of_black_paper += sum( _ )

print( Size_of_black_paper )