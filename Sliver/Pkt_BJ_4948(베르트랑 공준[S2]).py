#Problem title  :   Chebyshev's Theorem(베르트랑 공준)
#Problem Number :   4948
#Problem Tier   :   Sliver 2
#Date           :   2023/02/16, 13:51



# 숏 코딩 버전
while True:
    N=int(input());M=2*N
    if N==0: break
    e=[];e=[True]*(M+1);e[1]=False;[e.__setitem__(j, False) for i in range(2,int(M**0.5)+1)if e[i] for j in range(i+i,M+1,i)];print(e[N+1:M+1].count(True))




# 기독성 버전
# while True:
#     Number=int(input())
    
#     if Number==0: break

#     Max_number=2*Number; 
#     String_primes=[]; String_primes=[True]*(Max_number+1); String_primes[1]=False
    
#     for i in range(2,int(Max_number**0.5)+1):
#         if String_primes[i]==True:
#             for j in range(i+i,Max_number+1,i): 

#                 String_primes[j]=False
    
    
#     print(e[N+1:M+1].count(True))



