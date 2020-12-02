import pandas as pd
import matplotlib.pyplot as plt


# # creating data from scratch
# data = {
#     'Mathematic': [8, 10, 9, 9],
#     'Computer Science': [10, 8, 7, 8]
# }
# print(data)
#
# df = pd.DataFrame(data)
# print(df)
#
# df = pd.DataFrame(data, index=["Andrei", "Florentina", "Adriana", "Emiliano"])
# print(df)
# print(df.loc["Andrei"])
#
# df.to_csv("data_frame_example.csv")

# data frame operations
publisher_stats = pd.read_excel("publisher_stats.xlsx")
print(publisher_stats.head(5))      # get the first 5 rows
print(publisher_stats.tail(4))      # get the last 4 rows
print(publisher_stats.info())       # get information about data
print(publisher_stats.shape)        # get the dimension

exp_df = publisher_stats.append(publisher_stats)
print(exp_df)
print(exp_df)
exp_df.drop_duplicates()  # get rid of duplicates but don't change the data
print(exp_df)
exp_df.drop_duplicates(inplace=True)  # replaces the data
print(exp_df)

print(publisher_stats.columns)
publisher_stats.rename(columns={'Conv': 'Number of Conversion',
                                'Rev': 'Revenue(Dollars)'}, inplace=True)
print(publisher_stats)
print(publisher_stats['Trk Clicks'].value_counts().head(10))

subset = publisher_stats[['Revenue(Dollars)', 'Trk Clicks']]  # getting only 2 collumns
print(subset.head(10))

fox = publisher_stats.iloc[1]  # iloc get the information by index
print(fox)

# conditional selection
con_positive = (publisher_stats['Number of Conversion'] > 0)  # get only those rows where the number of conversion greater than 0
print(con_positive.head(10))
publisher_stats[publisher_stats['Widget Id'].isin(['Fox News', 'Worldation', 'Cellular Carrier US (Life Wireless)', 'WTVM'])].head()

con_positive_mask = publisher_stats['Number of Conversion'] > 0
con_df = publisher_stats[con_positive_mask]
print(con_df.head(10))
con_df['Payout'] = con_df['Revenue(Dollars)'] / con_df['Number of Conversion']  # create a new column
print(con_df.head())
print(con_df.describe())
con_df['Cost per Conversion'] = con_df['Cost'] / con_df['Number of Conversion']
print(con_df.head())

# plot
y_payout = con_df['Payout']
y_cpcon = con_df['Cost per Conversion']
plt.plot(y_payout, label='Payout', color='green')
plt.plot(y_cpcon, label='Cost per Conversion', color='red')
plt.legend()
plt.show()
plt.hist(y_cpcon)
plt.show()

percent_mask = con_df['Cost per Conversion'] < 70
good_data = con_df[percent_mask]
print(good_data)
print(len(good_data))

y_payout = good_data['Payout']
y_cpcon = good_data['Cost per Conversion']
plt.plot(y_payout, label='Payout', color='green')
plt.plot(y_cpcon, label='Cost per Conversion', color='red')
plt.legend()
plt.show()
plt.hist(y_cpcon)
plt.show()

# another example
print(publisher_stats['LP CTR'].quantile(0.5))
good_lpctr = publisher_stats[(publisher_stats['LP CTR'] > publisher_stats['LP CTR'].quantile(0.5)) &
                             (publisher_stats['LP CTR'] <= 1)]
good_lpctr['LP CTR'].hist()
plt.show()

# # the pandas series objects
# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
# print(data.values)
# print(pd.Series(5, index=[100, 200, 300]))
# print(pd.Series({2: 'a', 1: 'b', 3: 'c'}, index=[3, 1, 2]))
# print(pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]))
#
# indA = pd.Index([1, 3, 5, 7, 9])
# indB = pd.Index([2, 3, 5, 7, 11])
# print(indA & indB)  # intersection
# print(indA | indB)  # union
# print(indA ^ indB)  # symmetric difference
