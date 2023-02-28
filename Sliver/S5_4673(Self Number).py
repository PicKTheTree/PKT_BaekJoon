#Problem title  :   Self Number(셀프 넘버)
#Problem Number :   4673
#Problem Tier   :   Sliver 5
#Date           :   2023/02/21, 12:01
#URL            :   https://www.acmicpc.net/problem/4673

# 문제
# In 1949 the Indian mathematician D.R. Kaprekar discovered a class of numbers called self-numbers. 
# For any positive integer n, define d(n) to be n plus the sum of the digits of n. (The d stands for digitadition, a term coined by Kaprekar.) For example, d(75) = 75 + 7 + 5 = 87. 
# Given any positive integer n as a starting point, you can construct the infinite increasing sequence of integers n, d(n), d(d(n)), d(d(d(n))), ....
#  For example, if you start with 33, the next number is 33 + 3 + 3 = 39, the next is 39 + 3 + 9 = 51, the next is 51 + 5 + 1 = 57, and so you generate the sequence

# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

# The number n is called a generator of d(n). In the sequence above, 33 is a generator of 39, 39 is a generator of 51, 51 is a generator of 57, 
# and so on. Some numbers have more than one generator: for example, 101 has two generators, 91 and 100. A number with no generators is a self-number. 
# There are thirteen self-numbers less than 100: 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, and 97.
# Write a program to output all positive self-numbers less than 10000 in increasing order, one per line.

# 예제 입력 1        예제 출력 1 
                    # 1
                    # 3
                    # 5
                    # 7
                    # 9
                    # 20
                    # 31
                    # 42
                    # 53
                    # 64
                    #  |
                    #  |       <-- a lot more numbers
                    #  |  
                    # 9903
                    # 9914
                    # 9925
                    # 9927
                    # 9938
                    # 9949
                    # 9960
                    # 9971
                    # 9982
                    # 9993

def self_number(Number_Inputed):

    Generaotr_Of_Number = Number_Inputed

    while (Number_Inputed != 0):

        Generaotr_Of_Number += Number_Inputed %10
        Number_Inputed //= 10

    return Generaotr_Of_Number

List_Generator =[]

for _ in range(1,10001):

    List_Generator.append(self_number(_))
    
    if not _ in List_Generator:     print(_)


# Short Version

# r=range(10000)
# print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))
