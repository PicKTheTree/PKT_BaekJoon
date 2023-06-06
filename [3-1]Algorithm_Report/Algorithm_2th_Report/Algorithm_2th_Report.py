from matplotlib.table import Table
import pandas as pd
import matplotlib.pyplot as plt

def Pattern_select(column,pattern_choice): # 각 패턴을 입력하면, 해당 패턴을 인식하고 그 패턴의 값을 반환

    if      ( pattern_choice == 0 ) : return insert_table[column][0]
    elif    ( pattern_choice == 1 ) : return insert_table[column][1]
    elif    ( pattern_choice == 2 ) : return insert_table[column][2]
    else                            : return insert_table[column][0] + insert_table[column][2]

def Patttern_isture(this_column, pre_column):   # 이번 열의 패턴과 이전 열의 패턴이 양립 가능한지 체크하는 함수
    
    if (this_column == pre_column) : return False

    if      (this_column == 0 and pre_column == 3)  : return False
    elif    (this_column == 1 and pre_column != 3)  : return False
    elif    (this_column == 2 and pre_column == 3)  : return False
    elif    (this_column == 3 and pre_column != 1)  : return False
    else                                            : return True

def find_maxvalue_in_column(column): # DP테이블의 각 행의 최댓값 위치를 리스트에 저장하는 함수
    
    column_maxvalue_pos = [0,0]

    for _ in range(4):  # DP테이블의 n번째 행의 최댓값 위치를 저장 

        if max(DP_table[column]) == DP_table[column][_] : 

            column_maxvalue_pos = [column,_]
            column_maxvalue_pos_list.append(column_maxvalue_pos)
            break
    
    return 0

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
        
                    if Patttern_isture(this_column_pattern, pre_column_pattern) == True :

                        value = DP_table[column-1][pre_column_pattern] + DP_table[column][this_column_pattern]

                        if (value > maxvalue) : 
                            
                            maxvalue = value
    
                DP_table[column][this_column_pattern] = maxvalue

        find_maxvalue_in_column(column) # GUI을 그릴 때, 최댓값을 색깔로 칠하기 위한 위치 저장
                            
    print("DP Table\n\n")
    for print_index in range(n):                  
        
        print(DP_table[print_index])

    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n")


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 사용자 입력

n = None
while True: 
# 입력값 범위 초과시의 예외처리 

    try:

        n = int(input("테이블의 열(N)을 입력해주세요. (이때 n은 정수이며, 0 < N < 10이다.): "))
        if n < 0 or n > 10: raise ValueError
        break

    except ValueError: 
        
        print("0과 10 사이의 정수 값을 입력해주세요.")

DP_table = [[0] * 4 for _ in range(n)]  # table의 '열'마다 가능한 각 패턴의 값을 기록한 테이블
insert_table = []
column_maxvalue_pos_list = [] # insert_table의 각 열에 최댓값의 위치를 저장하는 list
column_maxvalue_pos = [] # 위의 리스트에 저장될 최댓값 위치 정보


for i in range(n):

    col = list(map(int, input(f"{i+1}열의 숫자를 입력하세요: ").split()))
    insert_table.append(col)

    if i == 0:

        df = pd.DataFrame({ 'col 1': [insert_table[i][0], insert_table[i][1], insert_table[i][2]]}, 
                            index=["row 1", "row 2", "row 3"])
        
    else:

        temp_df = pd.DataFrame({ 'col '+ str(i+1): [insert_table[i][0], insert_table[i][1], insert_table[i][2]]}, index=df.index)
        df = pd.concat([df, temp_df], axis =1)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n")

Pebble(n)

fig, ax = plt.subplots(figsize=(4, 2))
ax.axis('off')
table = ax.table(cellText=df.values.tolist(), colLabels=df.columns, rowLabels=df.index, cellLoc='center', loc='center')

# 특정 셀 색깔 변경
for _ in range(n):
    
    this_column_pattern = column_maxvalue_pos_list[_][1]

    if this_column_pattern == 0 : table[1,_].set_facecolor('green')
    elif this_column_pattern == 1 : table[2,_].set_facecolor('green')
    elif this_column_pattern == 2 : table[3,_].set_facecolor('green')
    else : 

        table[1,_].set_facecolor('green')
        table[3,_].set_facecolor('green')

plt.show()