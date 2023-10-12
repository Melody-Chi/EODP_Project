'''
Find champions with top kda in different server
'''

import pandas as pd
from matplotlib import pyplot as plt
na_d = pd.read_csv('data/a2/games/NAmatch.csv').dropna(axis=0, how='any')
kr_d = pd.read_csv('data/a2/games/KRmatch.csv').dropna(axis=0, how='any')
eu_d = pd.read_csv('data/a2/games/EUmatch.csv').dropna(axis=0, how='any')

#get top10 champion with highest average kda, visualise it
def get_top10(df):
    count = df.groupby('champion').size()
    avg = df.groupby('champion').agg({'kda':'mean'})
    sort = avg.sort_values(['kda'])
    sort['number'] = df.groupby('champion').size()
    sort1 = sort.loc[sort['number']>=5]
    top10 = sort1.tail(10)
    top10.plot.barh(y='kda',figsize=(5,10),legend = None)
    plt.yticks()
    plt.xlabel("Average KDA", size = 15)
    plt.ylabel("Champion", size = 15)
    plt.xticks(size=12)
    plt.yticks(size=12)

get_top10(na_d)
plt.title("top 10 high kda champions in NA server",size = 15)
plt.savefig("plots/NAtop10.png", bbox_inches="tight")
plt.close()

get_top10(kr_d)
plt.title("top 10 high kda champions in KR server",size = 15)
plt.savefig("plots/KRtop10.png", bbox_inches="tight")
plt.close()

get_top10(eu_d)
plt.title("top 10 high kda champions in EU server",size = 15)
plt.savefig("plots/EUtop10.png", bbox_inches="tight")
plt.close()
