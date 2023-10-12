'''
Analysing the preprocessed dataset
'''

import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import random
import seaborn as sns
from sklearn import preprocessing
from sklearn import metrics
from sklearn.preprocessing import KBinsDiscretizer
from IPython.display import display

#function that get the nmi martrix
def get_nmi(df):
    col = df.shape[1]
    List = []
    Name = []
    for n in range(col):
        Name.append(df.columns[n])
    for i in range(col):
        A = []
        X = df[df.columns[i]] 
        for j in range(col):
            Y = df[df.columns[j]]
            A.append(metrics.normalized_mutual_info_score(X, Y))
        List.append(A)
    return pd.DataFrame(List, index=Name, columns=Name)

#function make binned data
def binned(cell):
    return equal_width.fit_transform(cell).astype(int)

#discrete data set
def discrete(df):
    for col in df.columns[4:18]:
        df[col] = binned(df[[col]])

#read prepocessed data
global_d = pd.read_csv('wrangled_data/global_d.csv')
global_d_ro = pd.read_csv('wrangled_data/global_d_ro.csv')


#visualise level distribution
sns.countplot(global_d['level']).set(title='Level Distribution')
plt.savefig('plots/hist_level_dis.png',dpi=400,bbox_inches='tight')
plt.clf()

#get the majority parts of levels(13,14) and seperate it by role
mj = global_d_ro.loc[(global_d_ro['level'] == 13) | (global_d_ro['level'] == 14)]
mj_t = mj.loc[mj['role'] == 'TopLane_Jungle'].drop(columns=['role'])
mj_o = mj.loc[mj['role'] == 'Other'].drop(columns=['role'])
mj_t.to_csv('wrangled_data/mj_t.csv',index=False)
mj_o.to_csv('wrangled_data/mj_o.csv',index=False)

#visualise correlation
corr_d_tj = mj_t.corr(method='pearson')
corr_d_tj.to_csv('analysis_data/corr_d_tj.csv')
sns.heatmap(corr_d_tj, cmap='seismic')
plt.savefig('plots/heat_corr_tj.png',dpi=400,bbox_inches='tight')
plt.clf()
corr_d_o = mj_o.corr(method='pearson')
corr_d_o.to_csv('analysis_data/corr_d_other.csv')
sns.heatmap(corr_d_o, cmap='seismic')
plt.savefig('plots/heat_corr_other.png',dpi=400,bbox_inches='tight')
plt.clf()

#visualise the correlation btween different variables and kda
corr_d_tj['index'] = corr_d_tj.index
corr_d_o['index'] = corr_d_o.index
corr_d_tj['hue'] = 'TopLane_Jungle'
corr_d_o['hue'] = 'Other'
res=pd.concat([corr_d_tj,corr_d_o])
res=res[~res['index'].isin(['kda'])]
sns.barplot(x='index', y='kda', data=res, hue='hue')
plt.xlabel('Variables ')
plt.ylabel('Correlation with kda')
plt.xticks(rotation=-90) 
plt.savefig('plots/kda_corr.png',dpi=400,bbox_inches='tight')
plt.clf()

#data discretization
binned_d_tj = mj_t.copy()
binned_d_o = mj_o.copy()
equal_width = KBinsDiscretizer(n_bins=3,encode='ordinal', strategy='uniform')
discrete(binned_d_tj)
discrete(binned_d_o)

#visualise nmi
nmi_d_tj = get_nmi(binned_d_tj.drop(columns=['champion']))
nmi_d_tj.to_csv('analysis_data/nmi_d_tj.csv')
display(nmi_d_tj)
sns.heatmap(nmi_d_tj)
plt.savefig('plots/heat_nmi_tj.png',dpi=400,bbox_inches='tight')
plt.clf()
nmi_d_o = get_nmi(binned_d_o.drop(columns=['champion']))
nmi_d_o.to_csv('analysis_data/nmi_d_other.csv')
display(nmi_d_o)
sns.heatmap(nmi_d_o)
plt.savefig('plots/heat_nmi_other.png',dpi=400,bbox_inches='tight')
plt.clf()

#visualise the nmi of btween different binned variables and kda
nmi_d_tj['index'] = nmi_d_tj.index
nmi_d_o['index'] = nmi_d_o.index
nmi_d_tj['hue'] = 'TopLane_Jungle'
nmi_d_o['hue'] = 'Other'
res=pd.concat([nmi_d_tj,nmi_d_o])
res=res[~res['index'].isin(['kda'])]
sns.barplot(x='index', y='kda', data=res, hue='hue')
plt.xlabel('Variables ')
plt.ylabel('NMI with kda')
plt.xticks(rotation=-90) 
plt.savefig('plots/kda_nmi.png',dpi=400,bbox_inches='tight')
plt.clf()

#visualise relationship between kda, kills, deaths and assists, group by minions_killed
sns.pairplot(mj_t, x_vars=['kda', 'kills', 'deaths', 'assists'], y_vars=['kda', 'kills', 'deaths', 'assists'], hue='minions_killed', kind='reg', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}})
plt.savefig('plots/pair_kda_tj.png')
plt.clf()
sns.pairplot(mj_o, x_vars=['kda', 'kills', 'deaths', 'assists'], y_vars=['kda', 'kills', 'deaths', 'assists'], hue='minions_killed', kind='reg', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}})
plt.savefig('plots/pair_kda_other.png')
plt.clf()

#visualise relationship between kda, damage_building, turret_kills and gold_earned
sns.pairplot(mj_t, x_vars=['kda', 'damage_building', 'turret_kills', 'gold_earned'], y_vars=['kda', 'damage_building', 'turret_kills', 'gold_earned'], kind='reg', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}})
plt.savefig('plots/pair_kda_dmg_tj.png')
plt.clf()
sns.pairplot(mj_o, x_vars=['kda', 'damage_building', 'turret_kills', 'gold_earned'], y_vars=['kda', 'damage_building', 'turret_kills', 'gold_earned'], kind='reg', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}})
plt.savefig('plots/pair_kda_dmg_other.png')
plt.clf()
