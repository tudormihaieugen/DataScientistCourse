import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


publisher_stats = pd.read_excel("publisher_stats.xlsx")

publisher_stats.isna().sum()  # check if there is missing data
publisher_stats.dropna(inplace=True)  # delete missing data
publisher_stats.isna().sum()

publisher_stats['Widget Id'] = publisher_stats['Widget Id'].astype('string')
publisher_stats.describe()  # shows all the data calculated
publisher_stats.corr()  # calculate the correlation between data
publisher_stats.info()  # data type string, int, float
publisher_stats.hist()  # histogram of all variables
publisher_stats.hist('Net')  # histogram of Net values
publisher_stats.hist('Net', 'Trk Clicks', 'Conv')  # histogram for 3 values

publisher_stats.Net.quantile(0.1)  # the 10% quantile
q_min_Net = publisher_stats.Net.qunatile(0.1)
q_max_Net = publisher_stats.Net.quantile(0.9)
publisher_stats_filtered_net = publisher_stats[(publisher_stats.Net > q_min_Net) & (publisher_stats.Net < q_max_Net)]   # filtering 10%-90%
publisher_stats.boxplot('Net')  # boxplot by Net
publisher_stats_filtered_net.boxplot('Net')  # boxplot by filtered Net
publisher_stats.boxplot('CTR')  # boxplot by CTR (click to rate)

z_score = StandardScaler()
net_scaler = z_score.fit_transform(publisher_stats.Net.values.reshape(-1, 1))  # calculate the z score of the net value
# it needs a 2 dimensional array : .values.reshape(-1, 1)
publisher_stats['Net Scaler'] = net_scaler  # adding a column for net scaler
print(publisher_stats)
publisher_stats['Net Scaler'].describe()
publisher_stats['Net'].describe()

MinMax = MinMaxScaler()
Trk_Clicks_std = MinMax.fit_transform(publisher_stats['Trk Clicks'].values.reshape(-1, 1))  # calculate de minmax scaler
publisher_stats['Trk Clicks Std'] = Trk_Clicks_std
print(publisher_stats)
publisher_stats['Trk Clicks Std'].describe()
publisher_stats['Trk Clicks'].describe()
