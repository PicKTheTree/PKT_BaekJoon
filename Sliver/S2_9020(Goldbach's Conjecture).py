#Problem title  :   Goldbach's Conjesture(골드바흐의 추측)
#Problem Number :   9020
#Problem Tier   :   Sliver 2
#Date           :   2023/02/15, 12:31
#URL            :   https://www.acmicpc.net/problem/9020


# 문제
# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 
# 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

# 제한
# 4 ≤ n ≤ 10,000

# 예제 입력 1   예제 출력 1 
# 3             
# 8             3 5
# 10            5 5
# 16            5 11




### Python Version



# Init array of size 10001 contains prime number list.
String_Primes=[]
String_Primes=[True]*(10001)
String_Primes[1]=False
    
# Prime_Number = True       Not_Prime_Number = False 
for i in range(2,101):
    if String_Primes[i]==True:
        for j in range(i+i,10000+1,i): String_Primes[j]=False


#   ex) Number_inputed = 32
#   small     big (Must be Prime Number and Small + Big == Number_inputed)     
 
#   16    +   16  (Small == False , Big == False and Small + Big is 32) 
#   13    +   16  (Small == True  , Big == False and Small + Big is small than 32) 
#   13    +   17  (Small == True  , Big == True  and Small + Big is small than 32)
#   13    +   19  >> break

for i in range(int(input())):

    Number_inputed=int(input())
    Number_Half_Small, Number_Half_Big= Number_inputed//2,Number_inputed//2

    while ( String_Primes[Number_Half_Big]==False ) or ( String_Primes[Number_Half_Small] == False ) or ( Number_Half_Small + Number_Half_Big != Number_inputed ):

        if Number_Half_Small + Number_Half_Big >= Number_inputed:   Number_Half_Small-=1
        else:                                                       Number_Half_Big+=1

    print(Number_Half_Small, Number_Half_Big)
       


### Python Short Version

# e=[];e=[True]*10001;e[1]=False;[e.__setitem__(j,False)for i in range(2,101)if e[i] for j in range(i+i,10001,i)]
# for i in range(int(input())):
#     I=int(input())
#     M=N=I//2 
#     while e[M]==False or e[N]==False or M+N!=I:
#         if M+N>=I:N-=1                
#         else:M+=1
#     print(N,M)



