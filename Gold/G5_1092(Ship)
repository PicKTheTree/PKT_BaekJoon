#Problem Title  :   Ship (배)
#Problem Number :   1092
#Problem Tier   :   Gold 5
#Date           :   2023/03/14, 19:20
#URL            :   https://www.acmicpc.net/problem/1092


# 문제
# 지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다. 
# 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다. 넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.

# 예제 입력 1           # 예제 출력 1 
# 3                       2
# 6 8 9
# 5
# 2 5 2 4 7




### Python Version

import sys

input = sys.stdin.readline

Len_string_crane    = int( input() )
String_crane        = list( map( int, input().split() ) )
Len_string_box      = int( input() )
String_box          = list( map( int, input().split() ) )

String_crane.sort( reverse = True )
String_box.sort( reverse = True )
Time = 0

if String_crane[0] < String_box[0] : print(-1); exit()


while String_box : 
        
        
    Time += 1

    for Crane in String_crane :

        if String_box and Crane < String_box[-1] : continue

        for Box_index in range( len( String_box ) ) :
            
            if Crane >= String_box[ Box_index ] : del String_box[ Box_index ]; break

            
print( Time )


