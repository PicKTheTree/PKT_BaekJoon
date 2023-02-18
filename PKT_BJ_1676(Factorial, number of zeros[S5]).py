#Problem title  :   Factorial, number of zeros(팩토리얼 0의 개수)
#Problem Number :   1676
#Problem Tier   :   Sliver 5
#Date           :   2023/02/20, 10:21
#URL            :   https://www.acmicpc.net/problem/1676

# 문제 :
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
 
# 출력 :
# 첫째 줄에 구한 0의 개수를 출력한다.

# 예제 입력         예제 출력 :
# 10               2
# 3                0


N=(int(input()));N//=5;print(N+N//5+N//25)

#discription 
# N == 10 == 2 * 5
# N = factorial(N) == 3,628,800 , print(2)

# The number of zeros is eventually determind by the number of 10 (2 * 5), when a given number is prime-factorized.
# In this case, The number of 2 is sufficiently obtained by even numbers. Therefore, Only need to count the number of 5
# However, when 'N' is more than the square of 5, the number of 5 further increases, and thus a calculation accordingly is required
# So, the value obtaied by dividing "N" by "5" is stored in N again, and an additional calculation formula is required.

