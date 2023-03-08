# Problem Title  :   Is_Palindrome(팰린드롬인지 구분하기)
# Problem Number :   10988
# Problem Tier   :   Bronze 2
# Date           :   2023/03/08, 02:34 
# URL            :   https://www.acmicpc.net/problem/10988


# 문제 :
# 알파벳 소문자로만 이루어진 단어가 주어진다. 
# 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 
# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# 입력 :
# 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며,
# 알파벳 소문자로만 이루어져 있다.

# 출력 : 
# 첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

# 예제 입력 1       예제 출력 1
# level            1
# baekjoon         0

### Python Version

Word = input()
is_Palindrome = 0

for Word_index in range( len( Word ) ):

    if Word[ Word_index ] != Word[ len( Word ) - Word_index - 1 ] : is_Palindrome += 1; break

if is_Palindrome == 0   :   print('1')
else                    :   print('0')