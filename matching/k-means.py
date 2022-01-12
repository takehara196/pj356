from matplotlib import pyplot as plt
from sklearn import datasets, preprocessing
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

cust_df = pd.read_csv("input/Survey.csv")
cust_df = cust_df.drop(["id", "city_code"], axis=1)

print(cust_df)
cust_array = np.array([cust_df['preference1'].tolist(),
                       cust_df['preference2'].tolist(),
                       cust_df['preference3'].tolist(),
                       cust_df['preference4'].tolist(),
                       cust_df['preference5'].tolist(),
                       cust_df['preference6'].tolist(),
                       cust_df['preference7'].tolist(),
                       cust_df['preference8'].tolist(),
                       cust_df['preference9'].tolist(),
                       ], np.int32)

cust_array = cust_array.T
pred = KMeans(n_clusters=5).fit_predict(cust_array)
print(pred)

cust_df['cluster_id'] = pred
print(cust_df)

print(cust_df['cluster_id'].value_counts())

clusterinfo = pd.DataFrame()
for i in range(5):
    clusterinfo['cluster' + str(i)] = cust_df[cust_df['cluster_id'] == i].mean()
clusterinfo = clusterinfo.drop('cluster_id')

my_plot = clusterinfo.T.plot(kind='bar', stacked=True, title="Mean Value of 4 Clusters")
my_plot.set_xticklabels(my_plot.xaxis.get_majorticklabels(), rotation=0)

plt.show()
