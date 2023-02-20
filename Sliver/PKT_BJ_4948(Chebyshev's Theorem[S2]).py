#Problem title  :   Chebyshev's Theorem(베르트랑 공준)
#Problem Number :   4948
#Problem Tier   :   Sliver 2
#Date           :   2023/02/16, 13:51
#URL            :   https://www.acmicpc.net/problem/4948


# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

# 제한
# 1 ≤ n ≤ 123,456

# 예제 입력     예제 출력 
# 1             1
# 10            4
# 13            3
# 100           21   
# 1000          135
# 10000         1033
# 100000        8392
# 0


# 기독성 버전
while True:
    Number_Min=int(input())
    
    if Number_Min==0: break

    Number_Max=2*Number_Min; 
    String_primes=[]
    String_primes=[True]*(Number_Max+1)
    String_primes[1]=False
    
    for i in range(2,int(Number_Max**0.5)+1):
        if String_primes[i]==True:
            for j in range(i+i,Number_Max+1,i): 

                String_primes[j]=False
    
    
    print(String_primes[Number_Min+1:Number_Max+1].count(True))


# 숏 코딩 버전
# while True:
#     N=int(input());M=2*N
#     if N==0: break
#     e=[];e=[True]*(M+1);e[1]=False;[e.__setitem__(j,False)for i in range(2,int(M**0.5)+1)if e[i] for j in range(i+i,M+1,i)];print(e[N+1:M+1].count(True))




