import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = "https://www.datacamp.com/community/tutorials"
# html = urlopen(url)
# soup = BeautifulSoup(html, features="html.parser")
#
# pages = [i.text for i in soup.find_all('a') if 'community/tutorials?page=' in str(i)]
# lastpage = pages[-1]
# print(lastpage)
#
# description = []
# upvote = []
# author = []
# publishdate = []
# title = []
#
# for cp in np.arange(1, int(lastpage) + 1):
#     url = "https://www.datacamp.com/community/tutorials?page=" + str(cp)
#     html = urlopen(url)
#     soup = BeautifulSoup(html, features="html.parser")
#     description.append([i.text for i in soup.find_all(class_='jsx-2625178925 blocText description')])
#     upvote.append([i.text for i in soup.find_all(class_='jsx-1727309017 voted')])
#     author.append([i.text for i in soup.find_all(class_='jsx-886169423 name')])
#     publishdate.append([i.text for i in soup.find_all(class_='jsx-886169423 date')])
#     title.append([i.text for i in soup.find_all(class_='jsx-2625178925 blue')])
#     time.sleep(3)
# print("Done!")
#
# descriptionflat = [y for x in description for y in x]
# upvoteflat = [y for x in upvote for y in x]
# authorflat = [y for x in author for y in x]
# publishdateflat = [y for x in publishdate for y in x]
# titleflat = [y for x in title for y in x]
# publishdateformatted = [datetime.strptime(re.sub('rd, ', ', ', re.sub('st, ', ', ', re.sub('nd, ', ', ', re.sub('th, ', ', ', a)))), "%B %d, %Y") for a in publishdateflat]
#
# cdata = {"author": authorflat, "publishdate": publishdateformatted, "title": titleflat, "description": descriptionflat, "upvote": upvoteflat}
# df = pd.DataFrame(data=cdata)
# df.to_csv("datacamp.csv", header=True, index=False)

datacamp = pd.read_csv("datacamp.csv", parse_dates=["publishdate"], infer_datetime_format=True)
print(datacamp.head(10))

datacamp['publishyymm'] = datacamp['publishdate'].dt.strftime("%Y-%b")
datacamp["posts"] = 1

# datacamp.groupby([datacamp['publishdate'].dt.year, datacamp['publishdate'].dt.month]).size().plot(kind='bar', figsize=(15, 7), color='b')
# plt.show()
#
# datacamp[datacamp["publishdate"] >= '2017-01-01'].sort_values(by="publishdate", ascending=True).groupby([datacamp['publishyymm']], sort=False).size().plot(kind='bar', figsize=(15, 7), color='b')
# plt.show()
#
# datacamp[datacamp["publishdate"] >= '2017-01-01']["author"].value_counts(sort=True, ascending=False)[:10].plot(kind='bar')
# plt.show()


topauthors = datacamp[datacamp["publishdate"] >= '2017-01-01']["author"].value_counts(sort=True, ascending=False)[:10].index

dh = datacamp[datacamp["publishdate"] >= '2017-01-01'].sort_values(by="publishdate", ascending=True).set_index(["publishdate"], drop=False)
dh["publishdateone"] = pd.to_datetime(dh.publishdate.astype(str).str[0:7]+'-01')


dhp = dh[dh["author"].isin(topauthors)].pivot_table(index="publishdateone", values="posts", columns="author", aggfunc=np.sum)
fig, ax = plt.subplots(figsize=(15, 7))
dhp.plot(ax=ax, kind='bar', stacked=True)
ticklabels = [item.strftime('%Y %b') for item in dhp.index]
ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
plt.show()


upvotes = dh[dh["author"].isin(topauthors)].groupby(['author'], as_index=False).agg({'posts':"sum", 'upvote': "sum"})
sns.lmplot('posts',
           'upvote',
           data=upvotes,
           fit_reg=False,
           hue="author",
           scatter_kws={"marker": "D",
                        "s": 100})
plt.show()
