import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# publisher_stats = pd.read_excel("publisher_stats.xlsx")
#
# print(publisher_stats.head(5))
#
# publisher_stats.Net.hist()
# plt.show()
#
# plt.boxplot(publisher_stats.Net)
# plt.show()
#
# x = publisher_stats['Trk Clicks']
# y = publisher_stats['TS Clicks']
# plt.scatter(x, y)
# plt.show()
#
# plt.plot([1, 2, 3, 4])
# plt.ylabel('Values')
# plt.show()
#
# List = [1, 2, 3, 4, 5, 6, 7, 8]
# List_sq = [1, 4, 9, 16, 25, 36, 49, 64]
# plt.plot(List, List_sq)
# plt.show()
#
# List = [1, 2, 3, 4, 5, 6, 7, 8]
# List_sq = [1, 4, 9, 16, 25, 36, 49, 64]
# plt.plot(List, List_sq, color='green', label='X square values')
# plt.legend()
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # red circle
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
#
#
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
#
# data['b'] = data['a'] + 10 * np.random.randn(50)
# print(data)
# data['d'] = np.abs(data['d']) * 100
# print(data)
#
# # c=color, s=size
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()
#
#
# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]
#
# plt.figure(figsize=(9, 3))
# plt.subplot(131)  # 1 row, 3 columns, number of plot
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()
#
# plt.figure(figsize=(20, 10))
# plt.subplot(311)
# plt.bar(names, values)
# plt.subplot(312)
# plt.scatter(names, values)
# plt.subplot(313)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()
#
#
# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure()
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot(212)
# plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
# plt.show()
#
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot([1, 2, 3])
# plt.subplot(212)
# plt.plot([4, 5, 6])
# plt.figure(2)
# plt.plot([4, 5, 6])
# plt.figure(1)
# plt.subplot(211)
# plt.title("Title")
# plt.show()
#
#
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)  # the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
# plt.xlabel('Smart')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()
#
#
# plt.figure(figsize=(20, 10))
# ax = plt.subplot(111)
#
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# line, = plt.plot(t, s, lw=2)
#
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))
# plt.ylim(-2, 2)
# plt.show()
#
#
# np.random.seed(19680801)
#
# y = np.random.normal(loc=0.5, scale=0.4, size=1000)
# y = y[(y > 0) & (y < 1)]
# y.sort()
# x = np.arange(len(y))
#
# plt.figure()
#
# # Linear
# plt.subplot(221)
# plt.plot(x, y)
# plt.yscale('linear')
# plt.title('linear')
# plt.grid(True)
#
# # Log
# plt.subplot(222)
# plt.plot(x, y)
# plt.yscale('log')
# plt.title('log')
# plt.grid(True)
#
# # symmetric Log
# plt.subplot(223)
# plt.plot(x, y - y.mean())
# plt.yscale('symlog')
# plt.title('symlog')
# plt.grid(True)
#
# # Logit
# plt.subplot(224)
# plt.plot(x, y)
# plt.yscale('logit')
# plt.title('logit')
# plt.grid(True)
#
# plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
# plt.show()
