'''
Wrangling and preprocessing the input dataset
'''

import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import random
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import KBinsDiscretizer

#function that remove the outliers
def remove_outlier(df, col):
    Q1=df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)
    IQR=Q3-Q1
    df_ro=df[~((df[col]<(Q1-1.5*IQR)) | (df[col]>(Q3+1.5*IQR)))]
    return df_ro

#merge all the valid data(rows whithout null cells)
na_d = pd.read_csv('data/a2/games/NAmatch.csv').dropna(axis=0, how='any')
kr_d = pd.read_csv('data/a2/games/KRmatch.csv').dropna(axis=0, how='any')
eu_d = pd.read_csv('data/a2/games/EUmatch.csv').dropna(axis=0, how='any')
na_d["server"] = 0
kr_d["server"] = 1
eu_d["server"] = 2
global_d = pd.concat([na_d, kr_d, eu_d], ignore_index=True)
global_d = global_d.sort_values(by = ['kda'])

#visualise global kda distribution
sns.displot(global_d['kda'], bins=10,kde=False).set(title='KDA Distribution')
plt.savefig('plots/hist_kda_dis.png',dpi=400,bbox_inches='tight')
plt.clf()
sns.boxplot(x=global_d['kda']).set(title='KDA Distribution')
plt.savefig('plots/box_kda_dis.png',dpi=400,bbox_inches='tight')
plt.clf()

#kda removing outliers
global_d_ro = remove_outlier(global_d, 'kda')

#visualise global kda distribution that removed outliers
sns.displot(global_d_ro['kda'], bins=10,kde=False).set(title='KDA Distribution')
plt.savefig('plots/hist_kda_ro_dis.png',dpi=400,bbox_inches='tight')
plt.clf()
sns.boxplot(x=global_d_ro['kda']).set(title='KDA Distribution')
plt.savefig('plots/box_kda_ro_dis.png',dpi=400,bbox_inches='tight')
plt.clf()

#output data
global_d.to_csv('wrangled_data/global_d.csv',index=False)
global_d_ro.to_csv('wrangled_data/global_d_ro.csv',index=False)
