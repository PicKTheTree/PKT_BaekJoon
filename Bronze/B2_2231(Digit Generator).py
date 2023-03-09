#Problem Title  :   Digit Generator(분해합)
#Problem Number :   2231
#Problem Tier   :   Bronze 2
#Date           :   2023/03/09, 14:07
#URL            :   https://www.acmicpc.net/problem/2231


# Discription
# For a positive integer N, the digit-sum of N is defined as the sum of N itself and its digits. When M is the digitsum of N, we call N a generator of M.
# For example, the digit-sum of 245 is 256 (= 245 + 2 + 4 + 5). Therefore, 245 is a generator of 256.
# Not surprisingly, some numbers do not have any generators and some numbers have more than one generator.
# For example, the generators of 216 are 198 and 207.
# You are to write a program to find the smallest generator of the given integer.

# Input
# Your program is to read from standard input. The input consists of T test cases. 
# The number of test cases T is given in the first line of the input. Each test case takes one line containing an integer N, 1 ≤ N ≤ 100,000.

# Output
# Your program is to write to standard output. Print exactly one line for each test case. The line is to contain a generator of N for each test case. 
# If N has multiple generators, print the smallest. If N does not have any generators, print 0.

# Example input         Example Output
# 216                   198 


### Python Version

Flag = 0
Number_input = int( input() )
for i in range( 1, Number_input + 1 ):
    
    Check_Generator = i + sum( list( map( int, str(i) ) ) )
    
    if Check_Generator == Number_input  :
        
        Flag +=1
        print( i )
        break

if ( Flag == 0 )    :   print("0")




### Python Short Version
# F=0;N=int(input())
# for i in range(1,N+1):    
#     C=i+sum(list(map(int,str(i))))    
#     if C==N:F+=1;print(i);break
# if(F==0):print("0")

