# 일자 : 23.07.26
# 내용 : Python 모듈 'matplotlib'를 연습하기 위한 코드이다. 
import matplotlib.pyplot as plt


plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = (12)

ax1 = plt.subplot()

ax1.plot([16, 17, 18, 19, 20, 21, 22, 23, 24], [31, 30, 30, 29, 28, 27, 27, 27, 26], 'bo-', color='blue', label='Tem')
ax1.set_xlabel('Time(h)')
ax1.set_ylabel('Temperture')
ax1.tick_params(axis='both', direction='in')

ax2 = ax1.twinx()
ax2.bar( [16, 17, 18, 19, 20, 21, 22, 23, 24], [70, 70, 70, 75, 80, 85, 90, 90, 95], color='orange', label='Hum', alpha=0.7, width=0.85)
ax2.set_ylabel('Humidity')
ax2.tick_params(axis='y', direction='in')

ax1.set_zorder( ax2.get_zorder() + 10 )
ax1.patch.set_visible(False)

ax1.legend(loc = 'upper left')
ax2.legend(loc = 'upper right')

plt.show()