
#Problem title  :   Sum of GCD(GCD 합)
#Problem Number :   9613
#Problem Tier   :   Sliver 4
#Date           :   2023/03/13, 16:38
#URL            :   https://www.acmicpc.net/problem/9613


# 문제
# Given n positive integers, you have to find the summation of GCD (greatest common divisor) of 
# every possible pair of these integers. 
 
# 입력
# The first line of input is an integer n (1< n <100) that determines the number of test cases. 
# The following n lines are the n test cases. Each test case contains 2 parts:
# first part is the number m (1< m <100) indicating the number of input integers, 
# second part includes m positive integers. The input integers do not exceed 1000000. 

# 출력
# For each test case, show the summation of GCDs of every possible pair. 

# 예제 입력 
# 3
# 4 10 20 30 40
# 3 7 5 12
# 3 125 15 25

# 예제 출력 
# 70
# 3
# 35

### Python Version 

# 'Definition GCD Function ( GCD를 구하는 함수 정의, 유클리드 호제법 참조 )'

def GCD( Num_small, Num_big ) :

  while Num_small != 0 : Num_big, Num_small = Num_small, Num_big % Num_small
  return Num_big



# 'Case input ( 케이스 수 입력받고 그만큼 반복하기 )'

for _ in range( int( input() ) ) : 
  

  # 'Case init ( 각 케이스마다 필요한 변수 초기화 )'

  String_num = list( map( int, input().split() ) )
  String_num.pop( 0 ); String_num = sorted( String_num )
  GCD_sum = 0


  # 'Sum of GCD ( 입력받은 배열의 GCD 합 구하기 )'

  while ( len( String_num ) > 1 ) :

    # '끝에 있는 숫자를 Pop하여, 저장하고 나머지 숫자들과 GCD를 계산'
    Num_big  = String_num.pop()

    for index in range( len( String_num ) ) :

      Num_small = String_num[ index ]
      GCD_sum += GCD( Num_small, Num_big )
    


  # 'Print Result ( GCD 합 출력 )'
  print( GCD_sum ) 






### Python Short Version
# def GCD( x, y ):
#   while x != 0 :  y, x = x, y % x
#   return y

# for _ in range( int( input( ) ) ) : 
  
#   S = list( map( int, input().split() ) )
#   S.pop(0); S = sorted( S )
#   Result = 0

#   while ( len( S ) > 1 ) :

#     Y = S.pop()

#     for index in range( len( S ) ) :

#       X = S[ index ]
#       Result += GCD( X, Y )
    
    
#   print( Result ) 
    

  
    
        
      



    
  
  
  
    # if ( String_len < 2 )   :    

    # while( Num_rest != 0 ):

    #     Num_B = Num_A; Num_A = Num_rest
    #     Num_rest = Num_B % Num_A
    
  
  



