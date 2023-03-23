# Problem title  :   Study of Word(단어 공부)
# Problem Number :   1157
# Problem Tier   :   Bronze 1
# Date           :   2023/03/22, 15:09 
# URL            :   https://www.acmicpc.net/problem/1157


# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


# 예제 입력 1 
# Mississipi

# 예제 출력 1 
# ?

# 예제 입력 2 
# zZa

# 예제 출력 2 
# Z

# String_word = list( map( str, input() ) ) ; String_word.upper()
# String_alphabet=[]

String_word = input().upper()
String_letter = list( set( String_word ) )
String_cnt_letter = []

for letter in String_letter : 
    
    String_cnt_letter.append( String_word.count( letter ) )


Result = max( String_cnt_letter )

if String_cnt_letter.count( Result ) > 1 : 
    
    print("?")

else :

    print( String_letter[ String_cnt_letter.index( Result) ] )

