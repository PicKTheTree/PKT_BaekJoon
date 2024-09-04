# 일자 : 23.07.26
# 내용 : Python 모듈 'matplotlib'를 연습하기 위한 코드이다. 
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.plot([16, 17, 18, 19, 20, 21, 22, 23, 24], [31, 30, 30, 29, 28, 27, 27, 27, 26], 'o-')
plt.title('Temperture')

plt.subplot(2, 1, 2)
plt.plot([16, 17, 18, 19, 20, 21, 22, 23, 24], [70, 70, 70, 75, 80, 85, 90, 90, 95], '2-')
plt.title('Humidity')
plt.xlabel('time (h)')


plt.show()