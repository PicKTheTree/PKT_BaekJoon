#Problem title  :   Sugar Delivery(설탕 배달)
#Problem Number :   2839
#Problem Tier   :   Sliver 4
#Date           :   2023/02/20, 10:28
#URL            :   https://www.acmicpc.net/problem/2839



# Description
# Mirko works in a sugar factory as a delivery boy. He has just received an order: he has to deliver exactly N kilograms of sugar to a candy store on the Adriatic coast. 
# Mirko can use two types of packages, the ones that contain 3 kilograms, and the ones with 5 kilograms of sugar.
# Mirko would like to take as few packages as possible. For example, if he has to deliver 18 kilograms of sugar, he could use six 3-kilogram packages.
# But, it would be better to use three 5-kilogram packages, and one 3-kilogram package, resulting in the total of four packages.
# Help Mirko by finding the minimum number of packages required to transport exactly N kilograms of sugar.

# Input
# The first and only line of input contains one integer N (3 ≤ N ≤ 5000).

# Output
# The first and only line of output should contain the minimum number of packages Mirko has to use. If it is impossible to deliver exactly N kilograms, output -1.

# Sample Input 1    Sample Output 1 
# 18                4                
# 4                 -1               
# 6                 2
# 9                 3
# 11                3               




# Legibility Version

 #   Amount_of_Sugar = 30 >> for _ in range(6,-1,-1) >> 6~0
 #   30 - ( 5 * 6) % 3 == 0 >> return  
 #   retrun  6 ( Count of 5kg package ) + 0 ( Count of 3kg package )
 #   else : return -1

def Calculation(Amount_of_Sugar):

    for _ in range(Amount_of_Sugar//5,-1,-1):  
                                                                
        if ( Amount_of_Sugar - 5 * _ ) % 3 == 0:    
                                                                  
            return _ + ( Amount_of_Sugar - 5 * _ ) // 3
                                                                 
    return -1                                                   



print(Calculation(int(input())))
        

     
     
     

# Short Version
    
# N=int(input());a=0
# while N%5!=0:N-=3;a+=1
# if N<0:print(-1)
# else:print(a+N//5)
    
    


    
    


