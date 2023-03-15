#Problem title  :   GCD (최대공약수)
#Problem Number :   1850
#Problem Tier   :   Sliver 1
#Date           :   2023/03/15, 23:03
#URL            :   https://www.acmicpc.net/problem/1850



### Python Version
def GCD( Num_small, Num_big ) :

  while Num_small != 0 : Num_big, Num_small = Num_small, Num_big % Num_small
  return Num_big

Num_small, Num_big = sorted( map( int, input().split() ) )

print( "1" * GCD(Num_small, Num_big) )