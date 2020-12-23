import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing, tree
from sklearn import metrics
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.utils import resample
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

rcParams['figure.figsize'] = 12, 4

data = pd.read_csv("Optimization_Algo_Example.csv")

print(data)
print(data.tr_clicks.describe())

# CLEAN DATA
mask = (data.tr_clicks > 4) & (data.cost > 0.2)
data_new = data[mask]
print(data_new)
print(data_new.Bid_suggestion.describe())

# Logistic Regression method
x = data_new[['tr_clicks', 'lp_clicks', 'impressions', 'TR.NET', 'TR.ROI', 'EPC']]
y = data_new[['Bid_suggestion']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

model_lreg = LogisticRegression()
x_res, y_res = x_train, y_train
model_lreg.fit(x_res, y_res)
y_pred = model_lreg.predict(x_test)

# Confusion matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
