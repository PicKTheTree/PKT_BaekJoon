#Problem Title  :   Color Paper(색종이)
#Problem Number :   2563
#Problem Tier   :   Sliver 5
#Date           :   2023/03/06, 20:36
#URL            :   https://www.acmicpc.net/problem/2563


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