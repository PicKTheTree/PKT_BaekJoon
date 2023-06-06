import pandas as pd

# 기존 DataFrame 생성
df = pd.DataFrame({'A': [1, 2], 'B': [4, 5]}, index = ["1열","2열"])

# 새로운 행 생성
new_row = pd.DataFrame({'A': [7], 'B': [8]}, index =["4열"])

# 행 추가
df = pd.concat([df, new_row], ignore_index=False)

print(df)

# # 문제 해결
# max_value, max_pattern = pe(n, table)

# # 결과 출력을 위한 DataFrame 생성
# df = pd.DataFrame({'열': range(1, n+1), '조약돌 패턴': max_pattern})
# df.set_index('열', inplace=True)

# # GUI로 표시
# fig, ax = plt.subplots(figsize=(6, 4))
# ax.axis('off')
# tbl = Table(ax, cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# for i, cell in tbl._cells.items():
#     cell.set_fontsize(14)
#     cell.set_edgecolor('black')
#     if i[0] == 0:
#         cell.set_text_props(weight='bold')

# ax.add_table(tbl)
# plt.title(f"최대값: {max_value}")
# plt.show()

            # this_column_df = pd.DataFrame({ 'P1': [DP_table[column][0]], 'P2': [DP_table[column][1]], 
            #                                 'P3': [DP_table[column][2]], 'P4': [DP_table[column][3]]}, index=[str(column+1) + "열"])
            # df = pd.concat([df, this_column_df], ignore_index=False)