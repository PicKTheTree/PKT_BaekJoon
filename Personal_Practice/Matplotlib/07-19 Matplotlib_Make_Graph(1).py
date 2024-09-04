# 일자 : 23.07.19
# 내용 : Python 모듈 'matplotlib'를 연습하기 위한 코드이다. 
import matplotlib.pyplot as plt


plt.plot(['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun'], [30, 25, 15, 15, 30, 40, 35], 'r', label = 'A' )
plt.plot(['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun'], [37, 27, 10, 47, 30, 37, 20], 'g', label = 'B' )
plt.plot(['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun'], [45, 32, 10, 12, 10, 12, 27], 'b', label = 'C' )
plt.legend( loc = 'right')

plt.show()