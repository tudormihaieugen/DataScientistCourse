import numpy as np
import pandas as pd
from scipy import stats
from scipy import linalg
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy import optimize

# Array = np.array([1, 2, 3])
# print(Array + 1)
#
# Array1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(Array1 + Array)
# print(Array1)
# print(Array1[0, 2])
#
# greater3_mask = Array1 > 3  # boolean array
# print(greater3_mask)
# print(Array1[greater3_mask])  # print only true values
#
# publisher_stats = pd.read_excel("publisher_stats.xlsx")
# net_positive_mask = publisher_stats.Net > 0
# net_negative_mask = publisher_stats.Net < 0
# print(publisher_stats[net_positive_mask])
# print(publisher_stats[net_negative_mask])
#
# print((Array1 > 3) & (Array1 % 2 == 0))
# print(Array1[(Array1 > 3) & (Array1 % 2 == 0)])
#
# mask = Array1 > 2
# print(Array1[mask])
# print(mask.sum())  # print the length of the Array1[mask], not the sum
# Array_exm = np.array([-2, -3, 0, 1, -3, 9, 8, 6, -4])
# sign_mask = np.where(Array_exm >= 0, "Positive", "Negative")
# print(sign_mask)
# print(np.where(Array_exm >= 0, 1, 0))
#
# Array = np.array([1, 2, 3, 4, 5])
# print(Array)
# print(Array[~((Array > 3) | (Array < 2))])
#
# Array1d = np.array([1, 2, 3, 4, 5, 6])
# Array2d = Array1d.reshape(3, 2)  # need 6 elements
# print(Array2d)
# Array2d = Array1d.reshape(2, 3)
# print(Array2d)
#
# print(Array1d.reshape(-1, 2))  # array with 2 columns and 3 elements
# print(np.concatenate([Array1d, Array1d]))
#
# row_vector = np.array([1, 2, 3])
# print(row_vector)
# column_vector = np.array([1, 2, 3]).reshape(-1, 1)
# print(column_vector)
# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print(matrix)
# print(matrix.transpose())
# print(np.matmul(matrix, column_vector))
#
#
# """ Scipy examples """
# arr = np.array([[1, 2], [3, 4]])
# print(linalg.det(arr))  # determinant of array
# inv_arr = linalg.inv(arr)  # inverse of array
# print(inv_arr)
# matrix_sing = np.array([[5, 4], [25, 20]])
# print(linalg.det(matrix_sing))  # determinant = 0, can't calculate the inverse
#
# # interpolation method
# interpolation_time = np.linspace(0, 1, 50)
# measured_time = np.linspace(0, 1, 10)
# noise = (np.random.random(10) * 2 - 1) * 1e-1
# measures = np.sin(2 * np.pi * measured_time) + noise
#
# linear_interp = interp1d(measured_time, measures)
# linear_results = linear_interp(interpolation_time)
#
# cubic_interp = interp1d(measured_time, measures, kind="cubic")
# cubic_result = cubic_interp(interpolation_time)
#
# plt.scatter(measured_time, measures, label="values", color="red")  # scatter = points
# plt.plot(interpolation_time, linear_results, label="linear interpolation", color="blue")
# plt.plot(interpolation_time, cubic_result, label="cubic interpolation", color="green")
# plt.legend()
# plt.show()
#
# # optimization and fit
# def f(x):
#     return x**2 + 10 * np.sin(x)
#
# x = np.arange(-10, 10, 0.1)
# plt.plot(x, f(x))
# plt.show()
#
# result = optimize.minimize(f, x0=0)  # getting the global min
# print(result)  # show all the stats
# print(result.x)  # show only the result
#
# root1 = optimize.root(f, x0=1)
# print(root1.x)
# root2 = optimize.root(f, x0=-2.5)
# print(root2.x)

# normal distribution
samples = np.random.normal(size=1000)
bins = np.arange(-4, 5)
print(bins)
histogram = np.histogram(samples, bins=bins, density=True)[0]
print(histogram)
pdf = stats.norm.pdf(bins)  # norm is a distribution object
plt.plot(bins, histogram, label="histogram", color="red")
plt.plot(bins, pdf, label="normal distribution", color="blue")
plt.legend()
plt.show()
