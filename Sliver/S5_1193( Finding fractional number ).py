#Problem Title  :   Build Bridge
#Problem Number :   1010
#Problem Tier   :   Sliver 5
#Date           :   2023/01/26, 13:03
#URL            :   https://www.acmicpc.net/problem/1193


# 문제
# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

# 1/1	1/2	 1/3	1/4	    1/5
# 2/1	2/2	 2/3	2/4	    
# 3/1	3/2	 3/3	    
# 4/1	4/2      
# 5/1	     		

# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

# 예제 입력    예제 출력  
# 1           1/1 
# 2           1/2
# 4           3/1


### Python Version
X=int(input())
i=1

while X > i:
  X-=i
  i+=1
  
if i%2!=0:  print ((i+1)-X,"/",X,sep='')
else: print(X,"/",(i+1)-X,sep='')