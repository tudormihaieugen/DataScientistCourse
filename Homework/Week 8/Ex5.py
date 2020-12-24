import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Optimization_Algo_Example.csv")

mask = (data['ts_clicks'] > 20) & (data['tr_revenue'] > 0) & (data['status'] == 'RUNNING')
new_data = data[mask]
print(new_data)

data_test = new_data
lower_lim = data_test['cost'].quantile(0.1)
upper_lim = data_test['cost'].quantile(0.9)
print("10% quantile:", lower_lim)
print("90% quantile:", upper_lim)
data_test = data_test[(data_test['cost'] < upper_lim) & (data_test['cost'] > lower_lim)]
print(data_test)

plt.figure(1)
data_test['lp_clicks'].hist()
plt.figure(2)
plt.boxplot(data_test['lp_clicks'])
plt.figure(3)
plt.scatter(data_test['tr_clicks'], data_test['lp_clicks'])
plt.show()
