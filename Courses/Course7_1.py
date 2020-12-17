import pandas as pd
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

rcParams['figure.figsize'] = 12, 4

data = pd.read_csv("Optimization_Algo_Example.csv")
print(data.head(10))

x = data[['tr_clicks', 'lp_clicks', 'impressions', 'TR.NET', 'TR.ROI', 'EPC']]
y = data[['Bid_suggestion']]

# Step 1 create 3 clusters for X data
# reduce dimensions by using PCA
pca = PCA(n_components=2)
pca.fit(x)
x_pca = pca.transform(x)
print(pca.explained_variance_ratio_)

plt.scatter(x_pca[:, 0], x_pca[:, 1])
plt.show()

kmeans = KMeans(n_clusters=3, random_state=0).fit(x_pca)
kmeans_classes = kmeans.predict(x_pca)
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=kmeans_classes)
plt.show()

# Step 2 predict the bid suggestion by using decision tree method
# Labelencoder for y
le = preprocessing.LabelEncoder()
y = y.values.reshape(1, -1)[0]
y[y == 'No sugg'] = 'No Sugg'
y[y == 'Increase Bid 3'] = 'increase'
y[y == 'Increase Bid 2'] = 'increase'
y[y == 'Increase Bid 1'] = 'increase'
y[y == 'Decrease Bid 3'] = 'decrease'
y[y == 'Decrease Bid 2'] = 'decrease'
y[y == 'Decrease Bid 1'] = 'decrease'
y = le.fit_transform(y)
# check for nulls
nans = data.isnull().sum()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
print(x_train)
print(y_test)

a = ADASYN()
x_res, y_res = x_train, y_train
model = tree.DecisionTreeClassifier()
model.fit(x_res, y_res)
y_pred = model.predict(x_test)

confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
print(classification_report(y_test, y_pred))

predictions = pd.DataFrame({'true_y_values': y_test, 'predicted_y_values': y_pred})
print(predictions)
