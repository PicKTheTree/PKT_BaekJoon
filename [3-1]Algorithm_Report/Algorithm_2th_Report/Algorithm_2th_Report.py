import pandas as pd
import matplotlib.pyplot as plt

def Pattern_select(column,pattern_choice): # 각 패턴을 입력하면, 해당 패턴을 인식하고 그 패턴의 값을 반환

    if      ( pattern_choice == 0 ) : return insert_table[column][0]
    elif    ( pattern_choice == 1 ) : return insert_table[column][1]
    elif    ( pattern_choice == 2 ) : return insert_table[column][2]
    else                            : return insert_table[column][0] + insert_table[column][2]

def Pattern_isture(this_column, pre_column):   # 이번 열의 패턴과 이전 열의 패턴이 양립 가능한지 체크하는 함수
    
    if      (this_column == pre_column)             : return False
    elif    (this_column == 0 and pre_column == 3)  : return False
    elif    (this_column == 2 and pre_column == 3)  : return False
    elif    (this_column == 3 and pre_column != 1)  : return False
    else                                            : return True

def Paint_pattern(column, pattern): # 최대값을 도출하는 패턴을 칠하는 함수

    if      pattern == 0 : table[1, column].set_facecolor('green')
    elif    pattern == 1 : table[2, column].set_facecolor('green')
    elif    pattern == 2 : table[3, column].set_facecolor('green')
    else: 

        table[1, column].set_facecolor('green')
        table[3, column].set_facecolor('green')

def Print_Output(n):    # 결과물을 출력하는 함수

    for index_column in range(n-1, -1, -1): # 특정 셀 색깔 변경(역추적 기법)
    
        if index_column == n-1 :

            row = DP_table[index_column]
            maxValue = max(row)
            maxValue_pattern = row.index(int(maxValue))
            Paint_pattern(index_column, maxValue_pattern)

        else :
            
            for i in range(4):
                
                if DP_table[index_column][i] == maxValue - Pattern_select(index_column+1, maxValue_pattern) : 

                    if Pattern_isture(maxValue_pattern, i) : 
                        
                        Paint_pattern(index_column, i)
                        maxValue = DP_table[index_column][i]
                        maxValue_pattern = i
                        break
    plt.show()

def Pebble(n):

    for column in range(n) :
        
        # DP 테이블의 행을 insert_table의 각 패턴에 따른 값으로 초기화
        DP_table[column][0] = Pattern_select(column, 0)
        DP_table[column][1] = Pattern_select(column, 1)
        DP_table[column][2] = Pattern_select(column, 2)
        DP_table[column][3] = Pattern_select(column, 3)

        if column > 0 : # 각 패턴의 최댓값을 구하기 위한 탐색

            for this_column_pattern in range(0,4): 
                
                maxvalue = -999999 # 큰 반복문이 끝난 후 maxvaule 초기화

                for pre_column_pattern in range(0,4): # 이전의 열의 패턴 중 양립이 가능하고 가장 큰 패턴 탐색
        
                    if Pattern_isture(this_column_pattern, pre_column_pattern) == True :

                        value = DP_table[column-1][pre_column_pattern] + DP_table[column][this_column_pattern]

                        if (value > maxvalue) : 
                            
                            maxvalue = value
    
                DP_table[column][this_column_pattern] = maxvalue
                            
    print("DP Table")
    for print_index in range(n):                  
        
        print(DP_table[print_index])

    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n")

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 사용자 입력

n = None
while True: 
# 입력값 범위 초과시의 예외처리 

    try:

        n = int(input("행의 길이(n)를 입력해주세요. (이때 n은 정수이며, 0 < N < 10이다.): "))
        if n < 0 or n > 10: raise ValueError
        break

    except ValueError: 
        
        print("0과 10 사이의 정수 값을 입력해주세요.")

DP_table = [[0] * 4 for _ in range(n)]  # table의 '열'마다 가능한 각 패턴의 값을 기록한 테이블
insert_table = []

print("\n(입력 예시)")
print("2")
print("6 -8 11")
print("7 10 12\n")

for i in range(n):

    while True: # 열의 입력 범위를 벗어났을 때의 

            try:
                
                col = list(map(int, input(f"{i+1}열의 값을 입력하세요: ").split()))
                
                if len(col) != 3 or (max(col) > 100 or min(col) < -100 )  :  raise ValueError    
                break
                
            

            except ValueError: 
                
                    print("입력 범위를 다시 확인 해주세요.")

    insert_table.append(col)

    if i == 0:

        df = pd.DataFrame({ 'col 1': [insert_table[i][0], insert_table[i][1], insert_table[i][2]]}, 
                            index=["row 1", "row 2", "row 3"])
        
    else:

        temp_df = pd.DataFrame({ 'col '+ str(i+1): [insert_table[i][0], insert_table[i][1], insert_table[i][2]]}, index=df.index)
        df = pd.concat([df, temp_df], axis =1)

# matplotlib에서 표를 그리기 위해 선언하는 코드
fig, ax = plt.subplots(figsize=(4, 2))
ax.axis('off')
table = ax.table(cellText=df.values.tolist(), colLabels=df.columns, rowLabels=df.index, cellLoc='center', loc='center')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n")

Pebble(n)
Print_Output(n)